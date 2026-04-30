describe('R8 - Todo list manipulation', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000')
    cy.get('input[type=text]').first().type('jane.doe@gmail.com')
    cy.get('input[type=submit]').click()
    cy.get('.container-element a').first().click()
  })

  // R8UC1 - TC1: add a todo when there is a discription
  it('TC1: add a new todo-item', () => {
    cy.get('input[placeholder="Add a new todo item"]').type('my new todo', {force: true})
    cy.get('input[value="Add"]').click({force: true})
    cy.get('.todo-list').should('contain.text', 'my new todo')
  })

  // R8UC1 - TC2: Add-button is disabled when input is empty
  it('TC2: Add-button is disabled when input is empty', () => {
    cy.get('input[value="Add"]').should('be.disabled')
  })

  // R8UC2 - TC3: Toggle an active todo -> done
  it('TC3: toggle an active todo -> done', () => {
    cy.get('.checker').first().click()
    cy.get('.checker').first().should('have.class', 'checked')
    })

    // R8UC2 - TC4: Toggle a done todo-item back to active
  it('TC4: toggle a done todo-item back to active', () => {
    cy.get('.checker').first().click() // done
    cy.get('.checker').first().click() // toggla back to active
    cy.get('.checker').first().should('have.class', 'unchecked')
    })

  it('TC5: removes a todo-item', () => {
    cy.get('.remover').first().click()
    cy.get('.todo-list').should('not.contain.text', 'Watch video')
    })
})

