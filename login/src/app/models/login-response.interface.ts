export interface LoginResponse {
    token: string;
    username: string;
    email: string;
    created: Date;
    active: boolean;
}