import { useQuery } from "react-query";
import "./ItemComponents.css"

//  `http://127.0.0.1:8090/api/files/items/${item.id}/${item.image}`
export function Item({item,  onClick}) {
    let click = () => {console.log(`${item.name} was clicked with no op`)}
    if(onClick) {
        click = onClick
    }
    
    return(
        <div className="item" onClick={click}>
            <div>{`${item.image}`}</div>
            <div>{`'${item.name}' `}</div>
        </div>
    )
}

export function ItemList({items, onClick}) {
    return(
        <div className="item-list">
            {items.map((item) => (
                <Item key={item.id} item={item} />
                ))}
        </div>
    )
}

export function ItemListQuery() {
    const { data } = useQuery({
        queryKey: ["items"],
        queryFn: () => (
          fetch("http://127.0.0.1:8090/api/collections/item/records") // item records
            .then((response) => response.json())
        ),
      });
    if(data?.items) {
        return (
            <div className="item-list">
                <ItemList items={data.items}/>
            </div>
        )
    }
    return (
        <div>
            No Items available...
        </div>
    )

}

// todo research how css grid works, if list then simple
export function ItemGrid({items, onClick}) {
    return (
    <>
        Item Grid
    </>
    )
}