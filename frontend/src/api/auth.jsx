import api from "./axios";


export const signup = async (form) => {
    return await api.post("/auth/signup", {
        username: form.username,
        email: form.email,
        password: form.password
    },
     {
    headers: {
      "Content-Type": "application/json"
    }
  })
}

export const login = async (data) => {
    return await api.post("/auth/login", data)
}