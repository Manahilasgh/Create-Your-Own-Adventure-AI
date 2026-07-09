import "./auth.css"
import { useState } from "react"
import { Form, useNavigate } from "react-router-dom"
import { signup } from "../api/auth"

const SignUp = () => {
    const [form, setForm] = useState({username: "", email: "", password: ""})
    const navigate = useNavigate()

    const hadleSubmit = async (e) =>{
        e.preventDefault()
        try {
        await signup(form);
        alert("Check your email for verification");
        navigate("/login");
    } catch (err) {
        console.error(err.response?.data);
        alert("SignUp failed");
  }
    }

    return (
        <div className="auth-container">
            <h1>Create an Account</h1>
            <form className="auth-form" onSubmit={hadleSubmit}>
                <input type="text" placeholder="Username" onChange={e => setForm({...form, username: e.target.value})}/>
                <input type="text" placeholder="Email" onChange={e => setForm({...form, email: e.target.value})}/>
                <input type="password" onChange={e => setForm({...form, password: e.target.value})}/>
                <button>SignUp</button>
            </form>
        </div>
    )
    }
export default SignUp;