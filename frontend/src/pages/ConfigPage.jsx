import { Link } from 'react-router-dom'
import { ItemGrid, ItemList, ItemListQuery } from "../components/ItemComponents"
import CategorySelection from "../components/CategorySelection"
import "./ConfigPage.css"


function TopBar() {
    return (
    <div className='config-page-topbar'>
        <button>Undo</button>
        <button>Redo</button>
        <CategorySelection />
    </div>
    )
}

function RightSide() {
    return (
    <div className='config-page-rs'>
        <TopBar />
        <ItemGrid />
        <Link to="/buttons">Save and Go Back</Link>
    </div>
    )
}

function ConfigPage() {
    return (
        <>
            <h1>Config Page</h1>
            <div className='config-page-body'>
                <ItemListQuery />
                <RightSide />
            </div>
        </>
    ) 
}


export default ConfigPage