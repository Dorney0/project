import axios from 'axios'
import Flower from './domain/Flower'

const API_URL = 'http://127.0.0.1:8000'

export async function getFlowers() {
  try {
    const response = await axios.get(`http://localhost:8000/flowers/`)
    const flowersData = response.data
    const flowers = Flower.fromJsonArray(flowersData)
    return flowers
  } catch (error) {
    console.error('Error fetching flowers:', error)
    return []
  }
}
