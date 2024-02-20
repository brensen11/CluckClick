import { Link } from 'react-router-dom'
import { useQuery } from 'react-query'
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

function GridQuery() {
    const ITEMS_ADDRESS = "http://127.0.0.1:8090/api/collections/item/records"
    const { data, isLoading, error } = useQuery({
        queryKey: ["items"],
        queryFn: () => (
          fetch(ITEMS_ADDRESS) // item records
            .then((response) => response.json())
        ),
      });
    // get JSON
    // if no JSON, return empty grid ...
    
    if(isLoading || error) {
        return <>Loading...</>
    } else if(error){
        return <>{error.message}</>
    } else {
        return <ItemGrid items={data.items.slice(0, 12)}/>
    }
}

function GridSide() {
    return (
    <div className='config-page-rs'>
        <TopBar />
        <GridQuery />
        <Link to="/buttons">Save and Go Back</Link>
    </div>
    )
}

function ConfigPage() {
    return (
        <div className='config-page'>
            <h1>Config Page</h1>
            <div className='config-page-body'>
                <ItemListQuery />
                <GridSide />
            </div>
        </div>
    ) 
}


export default ConfigPage