import * as ort from 'onnxruntime-node';

const session = await ort.InferenceSession.create('./HousePricer.onnx');

const results = await session.run({
    'SquareFootage': new ort.Tensor('int64', BigInt64Array.from([1300n, 2300n]), [2, 1]),
});

console.log(results.variable.cpuData);