import { Link } from 'react-router-dom'
import { ItemGrid, ItemList } from "../components/ItemComponents"
import CategorySelection from "../components/CategorySelection"

function TopBar() {
    return (
    <>
        <button>Undo</button>
        <button>Redo</button>
        <CategorySelection />
    </>
    )
}

function RightSide() {
    return (
    <>
        <TopBar />
        <ItemGrid />
        <Link to="/buttons">Save and Go Back</Link>
    </>
    )
}

function ConfigPage() {
    return (
        <>
            <>Config Page</>
            <ItemList />
            <RightSide />
        </>
    ) 
}


export default ConfigPage