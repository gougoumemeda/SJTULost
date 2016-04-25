/**
 * Created by gougoumemeda on 16/4/25.
 */



var EventEmitter = require('events').EventEmitter;
var assign = require('object-assign');

var FindingStore = assign({}, EventEmitter.prototype, {

    /*
     Each finding format:
     {
        description: string
        img: string
        user_phone: string
        lost_time:
        lost_place:
        state:
     }
     */

    findings: [],

    getFindingsWithAmount: function(amount=this.findings.count) {
        return this.findings.slice(0, amount);
    },

    setFindings: function(array) {
        this.findings = array;
    },

    appendNewFinding: function(json) {
        this.findings.append(json)
    },

    emitChange: function () {
        this.emit('change');
    },

    addChangeListener: function(callback) {
        this.on('change', callback);
    },

    removeChangeListener: function(callback) {
        this.removeListener('change', callback);
    }
});

module.exports = FindingStore;