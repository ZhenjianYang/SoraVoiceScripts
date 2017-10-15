from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0111_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_3CF",          # 01, 1
        "Function_2_4ED",          # 02, 2
        "Function_3_21F4",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    ChrTalk(    #0
        0xF,
        "#4PHmmm... Damn it all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "#4PIt just HAD to go missing right as we\x01",
            "were ready to get back to work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000FLooks like you have a problem,\x01",
            "Chief!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xF)
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #3
        0xF,
        "#4PAhhh! You all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        "#4PYou saw the board, didn't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1011FYeah, we did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x103,
        "#022FYou say something was stolen, Gaton?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x103, 400)

    ChrTalk(    #7
        0xF,
        "#4PYeah, I'm worried about what's happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "#4PI'd like you to get on this right away.\x01",
            "Is this a good time?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2")
    Call(1, 2)
    Jump("loc_3CE")

    label("loc_2C2")


    ChrTalk(    #9
        0x101,
        (
            "#1015FEr, sorry, right this SECOND isn't\x01",
            "so great, as it happens.\x02\x03",

            "We'll hear you out when we come back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #10
        0xF,
        "#4PMm. Sounds like you're pretty busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        (
            "#4PNothing for it.\x01",
            "Come back when you can, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x103,
        "#020FWe'll be back, don't worry.\x02",
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x8000)
    OP_8C(0xF, 90, 0)

    label("loc_3CE")

    Return()

    # Function_0_AA end

    def Function_1_3CF(): pass

    label("Function_1_3CF")

    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #13
        0xF,
        "#4PAh, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        (
            "#4PHow about it?\x01",
            "Can you hear me out now?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B")
    Call(1, 2)
    Jump("loc_4EC")

    label("loc_46B")


    ChrTalk(    #15
        0x101,
        "#1007FSorry, not yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "#4PMm. Sounds like you're pretty busy.\x02\x03",

            "Nothing for it.\x01",
            "Come back when you can, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 0)

    label("loc_4EC")

    Return()

    # Function_1_3CF end

    def Function_2_4ED(): pass

    label("Function_2_4ED")


    ChrTalk(    #17
        0x101,
        "#1006FSure, lay it on us, Chief.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #18
        0xF,
        "#4PExcellent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "#4PWell, then, before I get into the meat\x01",
            "of it...\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xE, 255)
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #20
        0xF,
        "#4PHey, Anya.\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_59B():
        TurnDirection(0xF9, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_59B)

    def lambda_5A9():
        TurnDirection(0xF6, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_5A9)
    Sleep(120)

    def lambda_5BC():
        TurnDirection(0xF7, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5BC)

    def lambda_5CA():
        TurnDirection(0xF8, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5CA)
    TurnDirection(0xE, 0xF, 400)

    ChrTalk(    #21
        0xE,
        "What is it, Papa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xF,
        (
            "#4PPapa's got some very important things\x01",
            "to talk about with Miss Estelle and her\x01",
            "friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "#4PHow about you go have Mama read\x01",
            "you a book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "Okaaay!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #25
        0xE,
        (
            "Mamaaa!\x01",
            "Can you read for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1001FHaha. Needed a moment to get\x01",
            "ready too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#525FWell, there goes the blood sugar\x01",
            "again. I'll go diabetic at this rate.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetChrPos(0x101, 1850, 0, 31530, 90)
    SetChrPos(0x103, 1160, 0, 32390, 90)
    SetChrPos(0xF8, 520, 0, 30850, 90)
    SetChrPos(0xF9, 100, 0, 31910, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C2")
    SetChrPos(0xF9, 520, 0, 30850, 90)
    SetChrPos(0xF8, 100, 0, 31910, 90)

    label("loc_7C2")

    SetChrPos(0xF, 3600, 0, 31530, 270)
    SetChrPos(0xE, -5340, 0, 35800, 0)
    OP_6D(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0xF,
        "Right! Let's start over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        (
            "So, let me start from the very beginning.\x01",
            "I know the posting wasn't too clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1006F#6PYeah, if you could.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#020F#6PIt will help to know everything\x01",
            "in the case of a missing object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xF,
        (
            "So...what's gone missing is the Royal\x01",
            "Letter of Commission for the Malga Mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        (
            "Letters of commission come from\x01",
            "the desk of the queen herself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xF,
        (
            "They authorize, and record the authorizing of,\x01",
            "a mine chief for a given excavation site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xF,
        (
            "The Malga Mine's actually the technical\x01",
            "property of the crown, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xF,
        (
            "We can legally mine there only because\x01",
            "we have the commission from Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1004F#6POh, okay.\x02\x03",

            "#1015FI never actually knew the mine...\x01",
            "I guess the whole mountain...\x01",
            "was the queen's property!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(    #38
        0x104,
        (
            "#030FWhile Liberl is, in practice, a democracy,\x01",
            "remember that it is still a constitutional\x01",
            "monarchy.\x02\x03",

            "It follows that at least a portion of the\x01",
            "kingdom's resources would remain property\x01",
            "of the crown, and thus the government.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED9")

    label("loc_C17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF3")

    ChrTalk(    #39
        0x108,
        (
            "#070FWell, Liberl is a democracy now,\x01",
            "but it has historically been a kingdom,\x01",
            "and still retains its queen.\x02\x03",

            "It makes sense that the royal family\x01",
            "would still control some of the country's\x01",
            "resources.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED9")

    label("loc_CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E06")

    ChrTalk(    #40
        0x105,
        (
            "#040FYes, the royal family retained significant\x01",
            "amounts of land even after the constitution\x01",
            "establishing the mayoralties was written.\x02\x03",

            "In truth, though, it IS a mere formality, in many\x01",
            "ways. The Auslese family can hardly work a\x01",
            "mine alone, for example!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED9")

    label("loc_E06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED9")

    ChrTalk(    #41
        0x106,
        (
            "#050FWell, Liberl is technically a kingdom\x01",
            "still, even if the queen's the only\x01",
            "person we don't elect these days.\x02\x03",

            "Ain't no surprise the Ausleses would own\x01",
            "a mountain or two from the old days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED9")


    ChrTalk(    #42
        0x103,
        (
            "#020F#6PEither way, I think I follow the problem.\x02\x03",

            "Even if it is a formality on some level,\x01",
            "the Malga Mine IS Queen Alicia's\x01",
            "property.\x02\x03",

            "As such, if you mine there without a\x01",
            "commission...it's still technically theft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        "That's it exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "Do you understand why that letter is\x01",
            "so important now? To the whole town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002F#6PYeah, no kidding it's important.\x02\x03",

            "So with that out of the way...\x02\x03",

            "What EXACTLY happened?\x01",
            "When did you notice the letter was\x01",
            "missing? Where is it supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xF,
        "It was just this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "I noticed the little strongbox I keep\x01",
            "the commission in was open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xF,
        (
            "When I looked inside...no letter.\x01",
            "Anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x103,
        (
            "#027F#6PSo there hasn't been much time since\x01",
            "you discovered the letter was missing.\x02\x03",

            "I'll be honest, Gaton, I'm a little unsure\x01",
            "this is even a crime at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1295")

    ChrTalk(    #50
        0x106,
        (
            "#053FYeah, I agree.\x02\x03",

            "#050FThere's a good chance it's a kid's\x01",
            "prank or something. You ask your\x01",
            "daughter about this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1408")

    label("loc_1295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F7")

    ChrTalk(    #51
        0x108,
        (
            "#070FI have to agree.\x02\x03",

            "Could this, forgive me, sir,\x01",
            "not be a child's prank?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1408")

    label("loc_12F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(    #52
        0x104,
        (
            "#030FHeh, I must say the same.\x02\x03",

            "This sounds to me more like an innocent\x01",
            "child's prank than a deathly crime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1408")

    label("loc_1379")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1408")

    ChrTalk(    #53
        0x105,
        (
            "#042FYes, I have to agree.\x02\x03",

            "Sir, are you certain your daughter or\x01",
            "her friends did not take the letter and\x01",
            "then misplace it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1408")


    ChrTalk(    #54
        0xF,
        (
            "I wish I could say it was.\x01",
            "It'd make things easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        "This time, though, it ain't that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1011F#6PWhy are you so sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        (
            "#022F#6PWait, that look on your face.\x02\x03",

            "You have a reason beyond the letter\x01",
            "itself to think this was a crime, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xF,
        (
            "Good intuition.\x01",
            "As a matter of fact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xF,
        "Well, take a look.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #60
        (
            "\x07\x05'Oh, my beauteous princess and her band of heroes!\x01",
            "The words of the queen lie in my hand.'\x02\x03",

            "'Should you desire their return,\x01",
            "then sift ye through the chaos to find the truth!'\x02\x03",

            "'The first key lies within the city.\x01",
            "Search they who sit beside the Goddess.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #61
        0xF,
        "So that card was inside the box instead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        (
            "This HAS to be a theft.\x01",
            "No kid wrote that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1709")
    OP_A2(0xA)

    label("loc_1709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1798")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Saw a Bleu-questo in CH2 or 3\x01",      # 0
            "Haven't had the pleasure\x01",           # 1
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_END)),
        (0, "loc_178F"),
        (1, "loc_1795"),
        (SWITCH_DEFAULT, "loc_1798"),
    )


    label("loc_178F")

    OP_A2(0xA)
    Jump("loc_1798")

    label("loc_1795")

    Jump("loc_1798")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C5")

    ChrTalk(    #63
        0x106,
        "#053F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17C5")

    label("loc_17C5")

    Jump("loc_17D9")

    label("loc_17C8")


    ChrTalk(    #64
        0x103,
        "#025F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_17D9")


    ChrTalk(    #65
        0x101,
        "#1007F#6PAidios. Just. Kill. Me.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1821")

    ChrTalk(    #66
        0x105,
        "#047FOh, no...\x02",
    )

    CloseMessageWindow()

    label("loc_1821")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183E")

    ChrTalk(    #67
        0x104,
        "#032FOho.\x02",
    )

    CloseMessageWindow()

    label("loc_183E")

    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #68
        0xF,
        "Wh-What in the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xF,
        (
            "Why do you all look like you've seen\x01",
            "a naughty dog?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1932")

    ChrTalk(    #70
        0x101,
        (
            "#1016F#6PYou could say we kinda have.\x02\x03",

            "#1007F#6PBleublanc, you opera-fetish maniac...\x02\x03",

            "Do you EVER know when to give up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2C")

    label("loc_1932")


    ChrTalk(    #71
        0x101,
        "#1016F#6PN-Nooo, it's just, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#025F#6PIt's nothing, Gaton. Don't worry.\x02\x03",

            "Well. At least we know who our criminal\x01",
            "is. That's...something. Kind of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#6PBleublanc, you opera-fetish maniac...\x02\x03",

            "...do you EVER know when to give up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    Jump("loc_1C6A")

    label("loc_1A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1AE6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(    #74
        0x106,
        (
            "#057FTch. A riddle on a card.\x02\x03",

            "I think we know what this shit's about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A93")


    ChrTalk(    #75
        0x101,
        (
            "#1007F#6PA riddle. On a card.\x02\x03",

            "Aidios. Just. Kill. Me.\x01",
            "Why again? Why NOW?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE3")

    Jump("loc_1B2A")

    label("loc_1AE6")


    ChrTalk(    #76
        0x103,
        (
            "#027F#6PA riddle on a card.\x02\x03",

            "We've certainly seen this before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B67")

    ChrTalk(    #77
        0x105,
        "#042FEstelle, do you think this is...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCD")

    label("loc_1B67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B94")

    ChrTalk(    #78
        0x104,
        "#032FCould this be...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCD")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BCD")

    ChrTalk(    #79
        0x103,
        "#023F#6PYou know what this is talking about?\x02",
    )

    CloseMessageWindow()

    label("loc_1BCD")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1002F#4PTrust me, I wish I didn't.\x02\x03",

            "Bleublanc, the Phantom Thief...\x01",
            "That Ouroboros agent we told you about.\x02\x03",

            "I'm pretty sure this is his doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6A")

    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0xF,
        "Who the hell is 'Bleublanc'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xF,
        "Is he the one who stole my letter?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1015F#6PI can't be absolutely certain,\x01",
            "but I think it's very likely.\x02\x03",

            "#1002FWe can guess about it later. Right now\x01",
            "we need to track down this letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#022F#6PYes, that seems wise.\x02\x03",

            "Let's try finding the place on the\x01",
            "card first.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5F")

    ChrTalk(    #85
        0x104,
        (
            "#032FWe must seek out 'those who sit beside the\x01",
            "Goddess.'\x02\x03",

            "#034FHmmm... The Phantom Thief has something\x01",
            "of a fixation with Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F76")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED2")

    ChrTalk(    #86
        0x106,
        (
            "#050FWe have to find 'they who sit beside the\x01",
            "Goddess,' huh?\x02\x03",

            "#053FNice and poetic, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F76")

    label("loc_1ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2A")

    ChrTalk(    #87
        0x107,
        (
            "#062FSo we need to find 'they who sit beside\x01",
            "the Goddess,' right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F76")

    label("loc_1F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F76")

    ChrTalk(    #88
        0x108,
        (
            "#072FSo we search for 'they who sit beside\x01",
            "the Goddess.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F76")


    ChrTalk(    #89
        0x101,
        (
            "#1003F#6PI'm guessing it's some kind of allusion.\x02\x03",

            "The only place that remotely comes to\x01",
            "mind would be the town church.\x01",
            "Maybe we should start there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        "Sounds like a good place to start to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xF,
        "Anyway, Estelle, good luck and be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1006F#6PYeah! We'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        "#020F#6PWe'll get to the bottom of this, Gaton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xF,
        (
            "Please! The town needs that letter back,\x01",
            "not just me!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x4, 0x4)
    OP_28(0x77, 0x4, 0x8)
    OP_28(0x77, 0x1, 0x1)
    OP_28(0x77, 0x1, 0x2)
    OP_28(0x77, 0x1, 0x4)
    OP_A2(0xB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1850, 0, 31530, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 1850, 0, 31530, 90)
    SetChrPos(0x1, 1850, 0, 31530, 90)
    SetChrPos(0x2, 1850, 0, 31530, 90)
    SetChrPos(0x3, 1850, 0, 31530, 90)
    SetChrPos(0xF, 4600, 0, 31530, 90)
    SetChrPos(0xE, 3140, 0, 32100, 180)
    OP_69(0x0, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0xE, 255)
    ClearChrFlags(0xF, 0x10)
    EventEnd(0x4)
    Return()

    # Function_2_4ED end

    def Function_3_21F4(): pass

    label("Function_3_21F4")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0xF, 4600, 0, 31530, 90)
    OP_4A(0xF, 255)
    SetChrPos(0x101, 1850, 0, 31530, 90)
    SetChrPos(0x103, 1300, 0, 32390, 90)
    SetChrPos(0xF8, 520, 0, 30850, 90)
    SetChrPos(0xF9, 100, 0, 31910, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2288")
    SetChrPos(0xF9, 520, 0, 30850, 90)
    SetChrPos(0xF8, 100, 0, 31910, 90)

    label("loc_2288")

    SetChrPos(0xE, -5340, 0, 35800, 0)
    OP_4A(0xE, 255)
    OP_6D(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #95
        0xF,
        "And...good!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)
    OP_8E(0xF, 0xE10, 0x0, 0x7B2A, 0x7D0, 0x0)

    ChrTalk(    #96
        0xF,
        (
            "*pheeew* Estelle, if you were older, I would\x01",
            "owe you a pitcher of beer the size of your head.\x01",
            "You saved my butt today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xF,
        (
            "I didn't think you'd get it back so\x01",
            "quickly, either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        (
            "Guess that's why they call you the\x01",
            "great hope of Rolent's young people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1008F#6PAh, haha... C'mon, that's embarrassing.\x02\x03",

            "We just did the job, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        "Hahaha! Actin' all humble, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xF,
        (
            "C'mon, young people have a right to be\x01",
            "puffed up and proud sometimes.\x01",
            "Let loose a little!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        "That aside, though, I'd like to know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xF,
        (
            "That Bleublanc maniac. Please tell me\x01",
            "you caught him and put him in irons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1015F#6PI really wish we had...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x103,
        (
            "#025F#6PSadly, he's evaded capture for years,\x01",
            "far beyond the borders of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #106
        (
            "\x07\x05Estelle explained all she knew of Bleublanc's history,\x01",
            "and how this was a crime of pleasure, not gain.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0xF,
        (
            "This guy's internationally famous?\x01",
            "What a son of a...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xF,
        (
            "So, what, he just came all the way out\x01",
            "here for the sole purpose of messing\x01",
            "with our lives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xF,
        (
            "He really is a maniac. I can't understand\x01",
            "that kind of thinking at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        (
            "#026F#6PTrust me, I think everyone here agrees\x01",
            "with you.\x02\x03",

            "#020F#6PStill, I think you should be a little more\x01",
            "careful with that letter, regardless.\x02\x03",

            "This time it actually was a prank, of sorts.\x01",
            "But he proved the letter could be stolen\x01",
            "for blackmail or the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xF,
        (
            "That's a good point... I'll think of some\x01",
            "way to secure the letter better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "Problem is, there's no real safe place\x01",
            "in my house to store it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xF,
        (
            "Maybe I should do as I thought when\x01",
            "I first got this, and just ask Mayor\x01",
            "Klaus to put it in his safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1018F#6PYeah, that should work, right?\x02\x03",

            "#1016FIt'd be perf...ect... Well, depending on\x01",
            "the thief, it MIGHT still get stolen,\x01",
            "but it's...safer? I guess?\x02\x03",

            "(The problem is, Mayor Klaus ALREADY\x01",
            "got robbed once in recent memory...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ABF")

    ChrTalk(    #115
        0x106,
        (
            "#051FStill be safer there than lyin' around here.\x02\x03",

            "It's a good idea.\x01",
            "You should ask the man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B4C")

    ChrTalk(    #116
        0x108,
        (
            "#070FIt would still be more secure than a small\x01",
            "strongbox in a mid-city residence.\x02\x03",

            "You should ask the mayor, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD5")

    ChrTalk(    #117
        0x104,
        (
            "#031FHa-ha! Come, there's no need to dwell\x01",
            "on that.\x02\x03",

            "It is a capital idea.\x01",
            "You should ask your mayor at once, sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2BD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(    #118
        0x105,
        (
            "#040FIt would still, ultimately, be more secure\x01",
            "than simply having the letter here.\x02\x03",

            "Sir, I do think you should ask Mayor Klaus.\x01",
            "I cannot imagine he would not do\x01",
            "everything he can to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")


    ChrTalk(    #119
        0xF,
        (
            "Yeah... Didn't want to trouble him,\x01",
            "but I'll go ahead and ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xF,
        (
            "For today, though, it's back to the\x01",
            "mine with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#023F#6POh, my, right back to work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xF,
        (
            "Yeah, the septium export market\x01",
            "never slows down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xF,
        (
            "No matter how much we dig out,\x01",
            "we can't keep up with demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xF,
        (
            "I mean, hell, you use orbments.\x01",
            "You know how important septium is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1008F#6PHaha... Yeah, painfully so.\x02\x03",

            "We're pretty much always banging our\x01",
            "heads against the counter at the orbal\x01",
            "factory, lamenting our lack of sepith.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EED")

    ChrTalk(    #126
        0x107,
        (
            "#067FIt takes a lot to make good quartz,\x01",
            "yeah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3041")

    label("loc_2EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F82")

    ChrTalk(    #127
        0x104,
        (
            "#034FIndeed! It is a problem.\x02\x03",

            "The specialty quartz that I require\x01",
            "for the fullest of my abilities is\x01",
            "devilishly hard to make.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3041")

    label("loc_2F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE7")

    ChrTalk(    #128
        0x105,
        (
            "#040FYes, we do always seem to run into problems\x01",
            "making truly high-end quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3041")

    label("loc_2FE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3041")

    ChrTalk(    #129
        0x108,
        (
            "#070FHaha, yes, high-performance quartz require\x01",
            "that much more sepith.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3041")


    ChrTalk(    #130
        0xF,
        (
            "Wait, really? I hadn't realized bracers\x01",
            "were that hard up for sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xF,
        (
            "You just need sepith shards and not\x01",
            "true septium crystal cores, right?\x01",
            "Here, take some with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xF,
        "I brought a few bags home just yesterday.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x101,
        (
            "#1004F#6PWh-What?\x01",
            "You can just give us sepith?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xF,
        "Yeah, it ain't that big a deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xF,
        (
            "We can always dig up more in the mine,\x01",
            "and the big-ticket items are the true\x01",
            "crystals, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xF,
        "So which element would you like?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "500 Earth Sepith\x01",       # 0
            "500 Water Sepith\x01",       # 1
            "500 Fire Sepith\x01",        # 2
            "500 Wind Sepith\x01",        # 3
            "500 Time Sepith\x01",        # 4
            "500 Space Sepith\x01",       # 5
            "500 Mirage Sepith\x01",      # 6
        )
    )

    MenuEnd(0xD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3358")

    ChrTalk(    #137
        0xF,
        "Amber sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x0, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #138
        "#0CReceived #2C500 #56IEarth Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_3358")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E4")

    ChrTalk(    #139
        0xF,
        "Blue sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x1, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #140
        "#0CReceived #2C500 #57IWater Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_33E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346E")

    ChrTalk(    #141
        0xF,
        "Red sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x2, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #142
        "#0CReceived #2C500 #58IFire Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_346E")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352B")

    ChrTalk(    #143
        0xF,
        (
            "Of course, when you think Rolent,\x01",
            "you think green sepith, don't you?\x02",
        )
    )

    CloseMessageWindow()
    AddSepith(0x3, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #144
        "#0CReceived #2C500 #59IWind Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_352B")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B7")

    ChrTalk(    #145
        0xF,
        "Black sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x4, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #146
        "#0CReceived #2C500 #62ITime Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_35B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3643")

    ChrTalk(    #147
        0xF,
        "Gold sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x5, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #148
        "#0CReceived #2C500 #60ISpace Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36CF")

    label("loc_3643")

    Jc((scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36CF")

    ChrTalk(    #149
        0xF,
        "Silver sepith, then!\x02",
    )

    CloseMessageWindow()
    AddSepith(0x6, 0x1F4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #150
        "#0CReceived #2C500 #61IMirage Sepith#0C shards!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_36CF")


    ChrTalk(    #151
        0xF,
        (
            "Well, it may not be much, but hopefully\x01",
            "it'll help you at the factories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xF,
        (
            "Make sure to make some good quartz,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1001F#6PYou bet! Thanks a ton!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x103,
        "#021F#6PYou're really too kind, Gaton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        "Well, I'm off to the mine, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xF,
        (
            "Estelle, make sure you come back to\x01",
            "Rolent soon, all right? Everyone misses\x01",
            "you and your dad.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3831():

        label("loc_3831")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3831")

    QueueWorkItem2(0x101, 3, lambda_3831)

    def lambda_3842():

        label("loc_3842")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3842")

    QueueWorkItem2(0x103, 3, lambda_3842)

    def lambda_3853():

        label("loc_3853")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3853")

    QueueWorkItem2(0xF8, 3, lambda_3853)

    def lambda_3864():

        label("loc_3864")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3864")

    QueueWorkItem2(0xF9, 3, lambda_3864)
    OP_8E(0xF, 0xC30, 0x0, 0x7710, 0x7D0, 0x0)
    OP_8C(0xF, 270, 400)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)

    ChrTalk(    #157
        0xF,
        "#2PHey, Frissa! Anya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xF,
        "#2PI'm off to the mine again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        "#4PAaaall riiiight! Take care.\x02",
    )

    CloseMessageWindow()

    def lambda_3902():

        label("loc_3902")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_3902")

    QueueWorkItem2(0xF, 3, lambda_3902)

    ChrTalk(    #160
        0xE,
        "#2PPapaaa!\x02",
    )


    def lambda_3922():

        label("loc_3922")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_3922")

    QueueWorkItem2(0x101, 3, lambda_3922)

    def lambda_3933():

        label("loc_3933")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_3933")

    QueueWorkItem2(0x103, 3, lambda_3933)

    def lambda_3944():

        label("loc_3944")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_3944")

    QueueWorkItem2(0xF8, 3, lambda_3944)

    def lambda_3955():

        label("loc_3955")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_3955")

    QueueWorkItem2(0xF9, 3, lambda_3955)
    OP_8E(0xE, 0xFFFFEDB8, 0x0, 0x7EDF, 0x1770, 0x0)
    OP_8E(0xE, 0xFFFFFF10, 0x0, 0x74CC, 0x1770, 0x0)
    OP_8E(0xE, 0x898, 0x0, 0x7710, 0x1770, 0x0)
    OP_56(0x0)
    OP_59()
    OP_44(0xF, 0x3)

    ChrTalk(    #161
        0xE,
        "Come home soooon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xE,
        "I'll be a good girl and wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xF,
        (
            "#2PYeah, I'll be back as soon as I can,\x01",
            "Anya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xF,
        (
            "#2PYou be a good girl and help Mama\x01",
            "while I'm away, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xE,
        "Okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1016F#3P(D'awwwwwww.)\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AC0")

    ChrTalk(    #167
        0x107,
        "#560F(Heehee. I kinda envy them...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3AC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AFA")

    ChrTalk(    #168
        0x105,
        "#048F(It warms the heart, doesn't it?)\x02",
    )

    CloseMessageWindow()

    label("loc_3AFA")


    ChrTalk(    #169
        0x103,
        (
            "#021F#6P(Even Gaton isn't immune to\x01",
            "those blood sugar problems, I think.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 315, 400)

    ChrTalk(    #170
        0xF,
        "#2PI'm off, then.\x02",
    )

    CloseMessageWindow()

    def lambda_3B6D():

        label("loc_3B6D")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3B6D")

    QueueWorkItem2(0x103, 3, lambda_3B6D)

    def lambda_3B7E():

        label("loc_3B7E")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3B7E")

    QueueWorkItem2(0xF8, 3, lambda_3B7E)

    def lambda_3B8F():

        label("loc_3B8F")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3B8F")

    QueueWorkItem2(0xF9, 3, lambda_3B8F)

    def lambda_3BA0():

        label("loc_3BA0")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3BA0")

    QueueWorkItem2(0xE, 3, lambda_3BA0)

    ChrTalk(    #171
        0x103,
        "#525F#6PYes, good luck at the mine.\x02",
    )

    CloseMessageWindow()

    def lambda_3BDA():

        label("loc_3BDA")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3BDA")

    QueueWorkItem2(0x101, 3, lambda_3BDA)

    ChrTalk(    #172
        0x101,
        "#1001F#6PTake care, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xE,
        "Bye-bye!\x02",
    )

    CloseMessageWindow()
    OP_8E(0xF, 0xC30, 0x0, 0x6FB8, 0x7D0, 0x0)

    def lambda_3C2D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3C2D)
    OP_8E(0xF, 0xC30, 0x0, 0x6B6C, 0x7D0, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0xE, 0x3)
    OP_28(0x77, 0x1, 0x100)
    OP_28(0x77, 0x4, 0x10)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #174
        "Quest #2C[Mine Commission] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x9)
    OP_3F(0x235, 1)
    SetChrFlags(0xF, 0x80)
    EventEnd(0x0)
    OP_4B(0xE, 255)
    Return()

    # Function_3_21F4 end

    SaveToFile()

Try(main)
