from db import db

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),unique=True, nullable=False)
    bank_requisites = db.Column(db.String(255))
    password_hash = db.Column(db.String(255), nullable= False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    role =  db.Column(db.String(20), nullable=False, default ='user')
   
    is_active = db.Column(db.Boolean, nullable=False, default = True)
    __table_args__ = (
       db.CheckConstraint("role IN ('user', 'admin')", name="users_role_check"),
    )



class Balance(db.Model):
    __tablename__= "balances"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False 
    )
    currency = db.Column(db.String(3),nullable=False)
    amount = db.Column(db.Numeric(18,3), nullable= False, default=0)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    
    
    
    __table_args__ = (
       db.UniqueConstraint("user_id","currency", name="balances_user_id_currency_key"),
    )



class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False 
    )
    from_currency = db.Column(db.String(3),nullable=False)
    to_currency = db.Column(db.String(3),nullable=False)
    amount_sent = db.Column(db.Numeric(18,3), nullable= False)
    amount_get = db.Column(db.Numeric(18,3))
    rate=db.Column(db.Numeric(18,6))
    status_transaction=db.Column(db.String(20),nullable=False, default="pending")
    admin_comment= db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    __table_args__ = (
        db.CheckConstraint("status_transaction IN ('pending', 'approved', 'rejected','modified')", name="transactions_status_transaction_check"),
    )    


class Adminlog(db.Model):

    __tablename__= "admin_log"    
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(
        db.Integer, 
        db.ForeignKey("users.id")
        
    )
    transaction_id = db.Column(
            db.Integer, 
            db.ForeignKey("transactions.id", ondelete="CASCADE")
        )

    admin_action=db.Column(db.String(20), nullable=False)
    admin_comment=db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    __table_args__ = (
        db.CheckConstraint("admin_action IN ('approve', 'reject', 'modify')", name="admin_log_admin_action_check"),
    )    

class History(db.Model):

    __tablename__= "history"    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey("users.id",ondelete="SET NULL")
        
        
    )
    table_name = db.Column(db.String(20), nullable=False)
    doing = db.Column(db.String(20), nullable=False)

    old_data=db.Column(db.JSON)
    new_data=db.Column(db.JSON)

    created_at=db.Column(db.DateTime, server_default=db.func.now(),nullable=False)
    __table_args__ = (
        db.CheckConstraint("doing IN ('insert', 'update', 'delete')", name="history_doing_check"),
    )        
