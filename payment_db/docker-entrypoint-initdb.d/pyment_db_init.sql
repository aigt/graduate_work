CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE SCHEMA IF NOT EXISTS payments;

CREATE TABLE IF NOT EXISTS payments.payments(

    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid NOT NULL,
    amount decimal NOT NULL,
    external_id text NOT NULL,
    external_payment JSONB NOT NULL,
    refunded boolean NOT NULL,
    system_id text NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS payments.subscribers(

    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id uuid NOT NULL,
    subscriber_status boolean NOT NULL,
    date_subscribe TIMESTAMP WITH TIME ZONE NOT NULL

);
