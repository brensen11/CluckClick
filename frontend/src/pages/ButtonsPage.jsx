import { Link } from "react-router-dom"
import { ItemGrid } from "../components/ItemComponents"
import CategorySelection from "../components/CategorySelection"
import { useQuery } from "react-query";

function ConfigLink() {
    return (
        <Link to="/config">CONFIG</Link>
    )
}

function UndoPrompt({name}) {
    return (
        <>
            {name} recorded!
            <button onClick={() => {
                // delete request
                // change text to be "action undone" and disable button
                console.log("It do be undid?")
            }}>
                Undo?
            </button>
        </>
    )
}

function RightSide() {
    return (
    <>
        <CategorySelection />
        <UndoPrompt />
        <ConfigLink />
    </>
    )
}

function ButtonsPage() {
    return (
        <>
            <ItemGrid />
            <RightSide />
        </>
    )
}

export default ButtonsPage