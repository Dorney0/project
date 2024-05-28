export default class Flower {
  id?: number
  name?: string
  imageUrl?: string
  price?: number

  static fromJson(data: any) {
    const result = new Flower()
    result.id = data.id
    result.name = data.name
    result.imageUrl = data.image_url
    console.log('begin')
    console.log(data)
    console.log(result)
    console.log('end')
    result.price = data.price
    return result
  }

  static fromJsonArray(data: any[]) {
    return data.map((flower) => Flower.fromJson(flower))
  }
}

const response = {
  data: [
    { id: 1, name: 'Rose', image_url: '', price: 200 },
    { id: 2, name: 'Rose', image_url: '', price: 200 }
  ]
}

const flowersData = response.data
const flowers: Flower[] = Flower.fromJsonArray(flowersData)
