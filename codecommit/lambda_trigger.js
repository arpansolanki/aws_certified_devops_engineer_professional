var aws = require('aws-sdk');
var codecommit = new aws.CodeCommit({ apiVersion: '2015-04-13' });

exports.handler = function(event, context) {
    
    //Log the updated references from the event
    var references = event.Records[0].codecommit.references.map(function(reference) {return reference.ref;});
    console.log('References:', references);
    
    //Get the repository from the event and show its git clone URL
    var repository = event.Records[0].eventSourceARN.split(":")[5];
    var params = {
        repositoryName: repository
    };
    codecommit.getRepository(params, function(err, data) {
        if (err) {
            console.log(err);
            var message = "Error getting repository metadata for repository " + repository;
            console.log(message);
            context.fail(message);
        } else {
            console.log('Clone URL:', data.repositoryMetadata.cloneUrlHttp);
            context.succeed(data.repositoryMetadata.cloneUrlHttp);
        }
    });
};
