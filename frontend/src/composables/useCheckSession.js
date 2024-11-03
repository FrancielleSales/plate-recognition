export default function useCheckSession() {
    const userSession = localStorage.getItem("user_id");
  
    if (!userSession) {
      return false;
    }

    return true;
}
  