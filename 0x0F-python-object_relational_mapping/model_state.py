#!/usr/bin/python3
"""
Modules: This Module models the table of state class
"""
from sqlalchemy import Column, Integer, String
from  sqlalchemy.ext.declarative import declarative_base


# Create declarative base class of sqlalchemy
Base = declarative_base()

# Inherit from Base class
class State(Base):
    """
    Models the table for state class
    """
    __tablename__ = 'states'
    id = column(Integer,
                unique=true,
                autoincrement=true,
                nullable=false,
                primary_key=true
                )
    name = column(String(128),
                nullable=false,
                )
