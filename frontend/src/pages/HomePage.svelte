<script lang="ts">
    import ItemGrid from '../lib/ItemGrid.svelte'
    import type {ItemData} from '../api/entities.ts';

    let items: Array<ItemData> = [
        {name:'hello1', image:'beans'},
        {name:'hello2', image:'beans'},
        {name:'hello3', image:'beans'},
        {name:'hello4', image:'beans'},
        {name:'hello5', image:'beans'},
        {name:'hello6', image:'beans'},
        {name:'hello7', image:'beans'},
        {name:'hello8', image:'beans'},
        {name:'hello9', image:'beans'},
        {name:'hello10', image:'beans'},
        {name:'hello11', image:'beans'},
        {name:'hello12', image:'beans'},
    ]

//   do some queries for items and columns
let onClick = (item: ItemData) => {console.log(item.name)}
</script>

<div class="flex flex-row h-full w-full justify-left">
  <ItemGrid classes="flex-5" data={items} onClick={onClick}></ItemGrid>
  <div class="flex-2 h-full">Other stuff</div>
</div>
