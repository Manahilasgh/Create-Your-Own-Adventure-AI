import { Navigate } from "react-router-dom";
import Login from "./LogIn";
import StoryGenerator from "../components/StoryGenerator";


const ProtectedRoute = ({children}) => {
    const token = localStorage.getItem("token")

    if(!token){
        return <Navigate to={Login} />
    }

    return children
}

export default ProtectedRoute;