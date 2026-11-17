from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, String, Integer, DateTime, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DATABASE_URL = "sqlite:///./poseguru.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass

class Profile(Base):
    __tablename__ = "profiles"
    user_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    display_name: Mapped[str] = mapped_column(String(120), default="")
    language: Mapped[str] = mapped_column(String(32), default="en")
    model_preference: Mapped[str] = mapped_column(String(24), default="female")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class FavoriteCategory(Base):
    __tablename__ = "favorite_categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    name: Mapped[str] = mapped_column(String(80))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class FavoritePose(Base):
    __tablename__ = "favorite_poses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    pose_id: Mapped[str] = mapped_column(String(128))
    title: Mapped[str] = mapped_column(String(160), default="")
    category_name: Mapped[str] = mapped_column(String(80), default="My Favorites")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    __table_args__ = (UniqueConstraint("user_id", "pose_id", name="uq_user_pose"),)

class FavoriteOutfit(Base):
    __tablename__ = "favorite_outfits"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    outfit_id: Mapped[str] = mapped_column(String(128))
    title: Mapped[str] = mapped_column(String(160), default="")
    notes: Mapped[str] = mapped_column(Text, default="")

class BackgroundRecord(Base):
    __tablename__ = "backgrounds"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    label: Mapped[str] = mapped_column(String(160), default="")
    location_text: Mapped[str] = mapped_column(String(200), default="")
    image_reference: Mapped[str] = mapped_column(String(300), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class ShootHistory(Base):
    __tablename__ = "shoot_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    shoot_mode: Mapped[str] = mapped_column(String(32), default="solo")
    pose_id: Mapped[str] = mapped_column(String(128), default="")
    pose_title: Mapped[str] = mapped_column(String(160), default="")
    outfit_label: Mapped[str] = mapped_column(String(160), default="")
    background_label: Mapped[str] = mapped_column(String(160), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

Base.metadata.create_all(bind=engine)
app = FastAPI(title="PoseGuru Profile & Favorites API", version="0.8.0")

class ProfileIn(BaseModel):
    user_id: str = Field(min_length=1, max_length=128)
    display_name: str = Field(default="", max_length=120)
    language: str = Field(default="en", max_length=32)
    model_preference: str = Field(default="female", max_length=24)

class FavoritePoseIn(BaseModel):
    user_id: str
    pose_id: str
    title: str = ""
    category_name: str = "My Favorites"

class CategoryIn(BaseModel):
    user_id: str
    name: str = Field(min_length=1, max_length=80)

class FavoriteOutfitIn(BaseModel):
    user_id: str
    outfit_id: str
    title: str = ""
    notes: str = ""

class BackgroundIn(BaseModel):
    user_id: str
    label: str = ""
    location_text: str = ""
    image_reference: str = ""

class HistoryIn(BaseModel):
    user_id: str
    shoot_mode: str = "solo"
    pose_id: str = ""
    pose_title: str = ""
    outfit_label: str = ""
    background_label: str = ""

def serialize(row):
    result = {}
    for col in row.__table__.columns:
        value = getattr(row, col.name)
        result[col.name] = value.isoformat() if isinstance(value, datetime) else value
    return result

@app.get("/health")
def health():
    return {"ok": True, "service": "poseguru-profile-api", "storage": "sqlite_demo"}

@app.get("/profile/{user_id}")
def get_profile(user_id: str):
    with SessionLocal() as db:
        row = db.get(Profile, user_id)
        if not row:
            row = Profile(user_id=user_id)
            db.add(row)
            db.commit()
            db.refresh(row)
        return serialize(row)

@app.put("/profile")
def save_profile(payload: ProfileIn):
    with SessionLocal() as db:
        row = db.get(Profile, payload.user_id)
        if row is None:
            row = Profile(user_id=payload.user_id)
            db.add(row)
        row.display_name = payload.display_name
        row.language = payload.language
        row.model_preference = payload.model_preference
        row.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(row)
        return serialize(row)

@app.post("/favorite-categories")
def create_category(payload: CategoryIn):
    with SessionLocal() as db:
        exists = db.query(FavoriteCategory).filter_by(user_id=payload.user_id, name=payload.name).first()
        if exists:
            return serialize(exists)
        row = FavoriteCategory(user_id=payload.user_id, name=payload.name)
        db.add(row); db.commit(); db.refresh(row)
        return serialize(row)

@app.get("/favorite-categories/{user_id}")
def list_categories(user_id: str):
    with SessionLocal() as db:
        return [serialize(x) for x in db.query(FavoriteCategory).filter_by(user_id=user_id).order_by(FavoriteCategory.name).all()]

@app.post("/favorites/poses")
def add_favorite_pose(payload: FavoritePoseIn):
    with SessionLocal() as db:
        row = db.query(FavoritePose).filter_by(user_id=payload.user_id, pose_id=payload.pose_id).first()
        if row:
            row.title = payload.title
            row.category_name = payload.category_name
        else:
            row = FavoritePose(**payload.model_dump())
            db.add(row)
        db.commit(); db.refresh(row)
        return serialize(row)

@app.get("/favorites/poses/{user_id}")
def list_favorite_poses(user_id: str):
    with SessionLocal() as db:
        return [serialize(x) for x in db.query(FavoritePose).filter_by(user_id=user_id).order_by(FavoritePose.created_at.desc()).all()]

@app.delete("/favorites/poses/{user_id}/{pose_id}")
def delete_favorite_pose(user_id: str, pose_id: str):
    with SessionLocal() as db:
        row = db.query(FavoritePose).filter_by(user_id=user_id, pose_id=pose_id).first()
        if not row:
            raise HTTPException(404, "Favorite pose not found")
        db.delete(row); db.commit()
        return {"deleted": True}

@app.post("/favorites/outfits")
def add_favorite_outfit(payload: FavoriteOutfitIn):
    with SessionLocal() as db:
        row = FavoriteOutfit(**payload.model_dump())
        db.add(row); db.commit(); db.refresh(row)
        return serialize(row)

@app.get("/favorites/outfits/{user_id}")
def list_favorite_outfits(user_id: str):
    with SessionLocal() as db:
        return [serialize(x) for x in db.query(FavoriteOutfit).filter_by(user_id=user_id).order_by(FavoriteOutfit.id.desc()).all()]

@app.post("/backgrounds")
def add_background(payload: BackgroundIn):
    with SessionLocal() as db:
        row = BackgroundRecord(**payload.model_dump())
        db.add(row); db.commit(); db.refresh(row)
        return serialize(row)

@app.get("/backgrounds/{user_id}")
def list_backgrounds(user_id: str):
    with SessionLocal() as db:
        return [serialize(x) for x in db.query(BackgroundRecord).filter_by(user_id=user_id).order_by(BackgroundRecord.created_at.desc()).all()]

@app.post("/history")
def add_history(payload: HistoryIn):
    with SessionLocal() as db:
        row = ShootHistory(**payload.model_dump())
        db.add(row); db.commit(); db.refresh(row)
        return serialize(row)

@app.get("/history/{user_id}")
def list_history(user_id: str):
    with SessionLocal() as db:
        return [serialize(x) for x in db.query(ShootHistory).filter_by(user_id=user_id).order_by(ShootHistory.created_at.desc()).limit(100).all()]

@app.delete("/account-data/{user_id}")
def delete_account_data(user_id: str):
    # Demo-only deletion endpoint. Production deletion must be authorized
    # against the authenticated account and include object storage/provider data.
    with SessionLocal() as db:
        for model in [Profile, FavoriteCategory, FavoritePose, FavoriteOutfit, BackgroundRecord, ShootHistory]:
            db.query(model).filter_by(user_id=user_id).delete()
        db.commit()
        return {"deleted": True, "user_id": user_id}
