import React from 'react';
import merge from '../assets/merge.png';
import grow from '../assets/grow.png';
import build from '../assets/build.png';

const Home = () => {
  return (
    <div name='Home' className='w-full h-screen bg-[#0a192f] text-gray-300'>
      {/* Container */}
      <div className='max-w-[1000px] mx-auto p-4 flex flex-col justify-center w-full h-full'>
          <div>
              <p className='text-5xl font-bold inline border-b-4 border-[#789cf2] '>COVID-19 Sorting Algorithm Efficiency</p>
              <p className='py-4'>By Drew Reisner, Ritika Samanta, and Simran Merchant</p>
              <p className='py-4'>Click words below to analyze each sort</p>
          </div>

          <div className='w-full grid grid-cols-2 sm:grid-cols-4 gap-4 text-center py-8'>
              <div className='shadow-md shadow-[#040c16] hover:scale-110 duration-500'>
                  <img className='w-40 mx-auto' src={merge} alt="HTML icon" />
                  <a href= 'https://www.youtube.com/watch?v=T6YrE0LJhJU'>Merge Sort</a>
              </div>
              <div className='shadow-md shadow-[#040c16] hover:scale-110 duration-500'>
                  <img className='w-40 mx-auto' src={grow} alt="HTML icon" />
                  <a href= 'https://youtu.be/-jdvyvm3zaI'>Quick Sort</a>
              </div>
              <div className='shadow-md shadow-[#040c16] hover:scale-110 duration-500'>
                  <img className='w-40 mx-auto' src={build} alt="HTML icon" />
                  <a href= 'https://youtu.be/yZw_ruc2Z7Q'>std :: Sort</a>
              </div>
              
                   
             
             
          </div>
      </div>
    </div>
  );
};
export default Home


              