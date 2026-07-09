import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";
import "./auth.css"

const Login = () => {
    const [form, setForm] = useState({email: "", password: ""})
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault()
        const res = await login(form)
        localStorage.setItem("token", res.data.access_token)
        navigate("/story")
    }

    return (
        <div className="auth-container">
            <h1>Login to your account</h1>
            <form className="auth-form" onSubmit={handleSubmit}>
                <input type="text" placeholder="Email" onChange={e => setForm({...form, email: e.target.value})}/>
                <input type="password" onChange={e => setForm({...form, password: e.target.value})}/>
                <button>LogIn</button>
            </form>
        </div>
    )
}

export default Login;