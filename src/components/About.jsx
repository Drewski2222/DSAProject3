import React from 'react';

const About = () => {
  return (
    <div name='about' className='w-full h-screen bg-[#0a192f] text-gray-300'>
      <div className='flex flex-col justify-center items-center w-full h-full'>
        <div className='max-w-[1000px] w-full grid grid-cols-2 gap-4'>
          <div className='sm:text-right pb-8 pl-4'>
            <p className='text-2xl font-bold inline border-b-4 border-[#789cf2]'>
            The data set contains daily reports of Covid-19 cases and deaths in countries worldwide.
            </p>
          </div>
          </div>
          <div className='max-w-[1000px] w-full grid sm:grid-cols-2 gap-8 px-4'> 
            <div className='sm:text-left text-2xl font-bold'>  
            </div>
            <div>
              <p>Sorting algorithms are necessary in many real-world applications such as database management, analytics, and information retrieval. Over time, datasets in general have been increasing in size, and the need for sorting algorithms in large scale environments is increasing.</p>  
            </div>
            <div className='flex flex-col justify-center items-center w-full h-full'>
        <div className='max-w-[1000px] w-full grid grid-cols-2 gap-4'>
          <div className='sm:text-right pb-8 pl-4'>
            <p className='text-2xl font-bold inline border-b-4 border-[#789cf2]'>
            Why is this important?
            </p>
          </div>
          </div>
          <div className='max-w-[1000px] w-full grid sm:grid-cols-2 gap-8 px-4'>
            <div className='sm:text-left text-2xl font-bold'>  
            </div>
            <div>
              <p>  Efficiently sorting large scale data is vital to draw conclusions and extrapolate the data to find trends and patterns. </p>  
             
            </div>
            
      </div>
    </div>
</div>
</div>
</div>
  );
};
          
export default About;