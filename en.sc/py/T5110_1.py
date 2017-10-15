from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5110_1 ._SN',
        MapName             = 'Other',
        Location            = 'T5110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60025",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T5110   ._SN',
            'ED6_DT21/T5110_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_38D",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_CEC",          # 05, 5
        "Function_6_11B6",         # 06, 6
        "Function_7_182E",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_26F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_143")
    Jump("loc_185")

    label("loc_143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15F")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_15F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_17B")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222")
    OP_A2(0x0)

    ChrTalk(    #0
        0x9,
        (
            "#843FYou're here, Estelle. Good.\x02\x03",

            "#840FWell, let's begin, then.\x01",
            "Please take the seat across\x01",
            "from me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264")

    label("loc_222")


    ChrTalk(    #1
        0x9,
        (
            "#840FLet's begin, then.\x01",
            "Please take the seat across\x01",
            "from me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_38C")

    label("loc_26F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    OP_A2(0x0)

    ChrTalk(    #2
        0x9,
        (
            "#840FEstelle, hello.\x02\x03",

            "Get your equipment ready\x01",
            "and head to the first floor.\x02\x03",

            "We'll begin today's training\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389")

    label("loc_2F5")


    ChrTalk(    #3
        0x9,
        (
            "#840FFirst, return to your room\x01",
            "and prepare your equipment.\x02\x03",

            "We'll begin today's training\x01",
            "soon, and I don't recommend\x01",
            "going out there unarmed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389")

    TalkEnd(0x9)

    label("loc_38C")

    Return()

    # Function_2_AC end

    def Function_3_38D(): pass

    label("Function_3_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_4C3")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_424")
    Jump("loc_466")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_440")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_466")

    label("loc_440")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45C")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_466")

    label("loc_45C")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_466")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #4
        0x8,
        (
            "#810FEstelle, your seat's next\x01",
            "to mine.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_628")

    label("loc_4C3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 7)), scpexpr(EXPR_END)), "loc_563")

    ChrTalk(    #5
        0x8,
        (
            "#810FLet's get ready quick and\x01",
            "meet on the first floor.\x02\x03",

            "Kurt's preeetty strict about\x01",
            "being on time, so he'll get\x01",
            "super ticked if we're late!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_625")

    label("loc_563")

    OP_A2(0x1037)

    ChrTalk(    #6
        0x8,
        "#814FEstelle! Already done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000FNah, I was just about to\x01",
            "head to my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#810FAh, okay.\x01",
            "You better get ready fast,\x01",
            "then.\x02\x03",

            "See you in a bit, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1006FYeah, later!\x02",
    )

    CloseMessageWindow()

    label("loc_625")

    TalkEnd(0x8)

    label("loc_628")

    Return()

    # Function_3_38D end

    def Function_4_629(): pass

    label("Function_4_629")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_69B")

    ChrTalk(    #10
        0xA,
        (
            "First go hear what Kurt\x01",
            "has to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "I think he has something\x01",
            "he wants to give you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79A")

    ChrTalk(    #12
        0xA,
        "Estelle! Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "You and Anelace were\x01",
            "really going at it. I could hear\x01",
            "you from in here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "My workshop's still not\x01",
            "open, but I'll be ready before\x01",
            "you have to head out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "We can do orbment tuning\x01",
            "or whatever you need then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_79A")


    ChrTalk(    #16
        0xA,
        (
            "I'm still in the middle of getting\x01",
            "everything ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "I'll be open before you need\x01",
            "to head out, Estelle, don't worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819")

    OP_A2(0x1007)
    TalkEnd(0xA)
    Return()

    label("loc_823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_837")
    Call(1, 7)
    TalkEnd(0xA)
    Return()

    label("loc_837")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Upgrade/Exchange\x01",      # 1
            "Shop\x01",                  # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B1")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_8A6")
    OP_A9(0xFA)
    Jump("loc_8A8")

    label("loc_8A6")

    OP_A9(0xFD)

    label("loc_8A8")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_8B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_8CB")
    OP_A9(0xFB)
    Jump("loc_8CD")

    label("loc_8CB")

    OP_A9(0xFE)

    label("loc_8CD")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_8D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E7")
    TalkEnd(0xA)
    Return()

    label("loc_8E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_94B")

    ChrTalk(    #18
        0xA,
        "How's training going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "If there's any equipment\x01",
            "you need, you can order\x01",
            "it here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_94B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x6E)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C2")

    ChrTalk(    #20
        0xA,
        (
            "Very good. Looks like you\x01",
            "can use restorative arts now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "Okay!\x01",
            "You two take care out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_9C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x258, 0x0)"), scpexpr(EXPR_END)), "loc_B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A65")

    ChrTalk(    #22
        0xA,
        (
            "If you set that 'HP 1' quartz,\x01",
            "you'll be able to use restorative\x01",
            "arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "If you can use those, you'll be\x01",
            "ready for your practice today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5E")

    label("loc_A65")


    ChrTalk(    #24
        0xA,
        (
            "Ah, looks like you made\x01",
            "the designated quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "If you set that into your orbment,\x01",
            "you'll be able to use restorative\x01",
            "arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "Do that and you'll be ready\x01",
            "to train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "All right, Kurt is waiting\x01",
            "outside, so go on and set\x01",
            "that quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B5E")

    Jump("loc_CE8")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_BFC")

    ChrTalk(    #28
        0xA,
        "Not sure what to make?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        "All right, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        "Just make an 'HP 1' quartz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "If you set one of those,\x01",
            "you can use restorative arts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_BFC")


    ChrTalk(    #32
        0xA,
        (
            "The art in question is\x01",
            "called 'Tear.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "If you check the Orbal Arts section\x01",
            "of your notebook, it will tell you the\x01",
            "elemental level you need for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "When you want to make quartz, select\x01",
            "'Quartz' under 'Upgrade/Exchange.'\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_CE8")

    TalkEnd(0xA)
    Return()

    # Function_4_629 end

    def Function_5_CEC(): pass

    label("Function_5_CEC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E38")
    OP_A2(0x1035)

    ChrTalk(    #35
        0xB,
        "Oh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        "Weeell? Satisfied?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1008FYup! I'm stuffed!\x02\x03",

            "It was so good I, uh, couldn't\x01",
            "help but eat a little too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "Well, that's good. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "Today will be a big lesson that\x01",
            "will wrap up your training here,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "Put your best foot forward,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1006FI will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA4")

    label("loc_E38")


    ChrTalk(    #42
        0xB,
        "I'm rooting for you, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "I'll have something delicious\x01",
            "waiting for you when you get\x01",
            "back! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA4")

    TalkEnd(0xB)
    Return()

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(    #44
        0xB,
        "Come on, now, take a seat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "Kurt and Anelace have been\x01",
            "waiting for a while now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2F")
    Call(1, 6)
    TalkEnd(0xB)
    Return()

    label("loc_F2F")

    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_F4C")
    OP_A9(0xFC)
    Jump("loc_F4E")

    label("loc_F4C")

    OP_A9(0xFF)

    label("loc_F4E")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_F57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F68")
    TalkEnd(0xB)
    Return()

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_1091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101E")
    OP_A2(0x2)

    ChrTalk(    #46
        0xB,
        "Good work, you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "If there's anything you need,\x01",
            "make sure you come right\x01",
            "back to the lodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "Robert and I will be on standby\x01",
            "here, just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_101E")


    ChrTalk(    #49
        0xB,
        (
            "If there's anything you need,\x01",
            "make sure you come right\x01",
            "back to the lodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "Good luck with your lesson!\x02",
    )

    CloseMessageWindow()

    label("loc_108E")

    Jump("loc_11B2")

    label("loc_1091")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_114F")

    ChrTalk(    #51
        0xB,
        (
            "If it gets dangerous, make\x01",
            "sure you have a meal and\x01",
            "rest a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        (
            "I know you're big, tough bracers\x01",
            "and it's good to push yourselves,\x01",
            "but overdoing it's no good either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B2")

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(    #53
        0xB,
        "Come now, Kurt is waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "Don't you want to get an\x01",
            "explanation of the lesson?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B2")

    label("loc_11B2")

    TalkEnd(0xB)
    Return()

    # Function_5_CEC end

    def Function_6_11B6(): pass

    label("Function_6_11B6")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 22220, 0, 12120, 90)
    SetChrPos(0x10A, 21720, 0, 12890, 90)
    OP_8C(0xB, 270, 0)
    OP_6D(23050, 0, 12920, 0)
    OP_0D()

    ChrTalk(    #55
        0xB,
        (
            "So Kurt's going to be working you\x01",
            "to the bone again, is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "Here, then, let me show you how\x01",
            "to prepare some nice, clean water\x01",
            "for yourselves out in the field.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #57
        "\x07\x00Received #525i.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x20D, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1E)"), scpexpr(EXPR_END)), "loc_12EE")
    Jump("loc_131F")

    label("loc_12EE")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #58
        "\x06Learned [#2CNature's Bounty#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_131F")

    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #59
        0xB,
        "Oh, don't forget the ingredients, dears.\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x06Received #2Cassortment of ingredients#0C.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_3E(0x396, 10)
    OP_3E(0x399, 10)
    OP_3E(0x39B, 10)
    OP_3E(0x394, 10)
    OP_3E(0x393, 10)
    OP_3E(0x390, 10)
    OP_3E(0x3A8, 2)

    ChrTalk(    #61
        0x10A,
        (
            "#0814FSo, like, we can just throw this stuff\x01",
            "in a pot to cook up a meal, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "Well, yes, what you have will cover\x01",
            "most basic cooking, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "You can only get some ingredients\x01",
            "by defeating monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "Gathering all the ingredients for those is\x01",
            "a bit dangerous, needless to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1016FYeah, tell me about it.\x01",
            "There're some weird recipes\x01",
            "out there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        (
            "#0817FMan. Kind of takes 'those who don't work,\x01",
            "don't eat' to a whole new level, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "Your Bracer Notebook will have\x01",
            "a more detailed explanation of cooking.\x01",
            "Make sure to look it over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        "Well, good luck with your training!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1006FThanks, Phyllis!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10A,
        (
            "#1310FWe'll try not to burn anything\x01",
            "down when we cook stuff!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #71
        (
            "\x07\x05You can learn new recipes by eating meals at bars, or by eating\x01",
            "'To-Go' food items you purchase or find.\x02\x03",

            "Once you learn a recipe, you can make the food item any time so\x01",
            "long as you have the ingredients by opening your Recipe Book.\x02\x03",

            "To open your Recipe Book, select the 'Items' tab from the Camp\x01",
            "Menu, and then select the 'Recipe Book' under the 'Book' category.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0xC5, 0x1, 0x4)
    FadeToBright(300, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_11B6 end

    def Function_7_182E(): pass

    label("Function_7_182E")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 24620, 0, 4960, 90)
    SetChrPos(0x10A, 24060, 0, 5730, 90)
    OP_8C(0xA, 270, 0)
    OP_6D(24720, 0, 5730, 0)
    OP_0D()

    ChrTalk(    #72
        0xA,
        (
            "Ah, looks like you two picked up\x01",
            "the new model combat orbments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "Did you already go over the list\x01",
            "of new quartz in your notebooks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "The fundamentals aren't much different,\x01",
            "but some things have had their attributes\x01",
            "adjusted in the switch, so give it a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "Now, before we get started,\x01",
            "how about a quick overview?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "If you need a refresher on\x01",
            "anything about how your\x01",
            "orbments work, ask away!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_1A0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2541")
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x18\x07\x05What would you like to ask about?\x02",
    )

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        155,
        0,
        (
            "Orbments\x01",             # 0
            "Orbal Arts\x01",           # 1
            "Quartz\x01",               # 2
            "Sepith\x01",               # 3
            "Upgrading Slots\x01",      # 4
            "Cancel\x01",               # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AE5"),
        (1, "loc_1D40"),
        (2, "loc_1F9E"),
        (3, "loc_21C7"),
        (4, "loc_2351"),
        (5, "loc_252C"),
        (SWITCH_DEFAULT, "loc_253C"),
    )


    label("loc_1AE5")


    ChrTalk(    #78
        0xA,
        (
            "Orbments are energy control devices that manifest\x01",
            "a variety of effects via crystalline circuits\x01",
            "made of septium, commonly called 'quartz.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "When most bracers think of an 'orbment,' they\x01",
            "think of combat orbments that improve your\x01",
            "physical abilities and let you use 'Orbal Arts.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "Combat orbments are specially tuned to each\x01",
            "individual user, so no two will be exactly alike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        (
            "This mostly boils down to elemental\x01",
            "limitations on certain slots, and the\x01",
            "arrangement of the orbment's 'lines.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "Taking a person's strengths into account is\x01",
            "crucial in preparing a strong orbment for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_1D40")


    ChrTalk(    #83
        0xA,
        (
            "Orbal Arts are a kind of...'magic,' I guess\x01",
            "you'd say, that can be activated through\x01",
            "a combat orbment's power system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "'Orbal Arts' is a bit of a mouthful, so\x01",
            "most people refer to 'em just as 'arts.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "To use arts--or get any use out of\x01",
            "your orbment at all!--you first need to\x01",
            "synthesize quartz at a factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "Setting quartz circuits in your orbment\x01",
            "will allow you to utilize arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "The arts you can use, therefore, depend\x01",
            "on the quartz you set in your orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "For example, you want to fling around\x01",
            "water arts? Use water-element quartz\x01",
            "to focus your orbment in that direction!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_1F9E")


    ChrTalk(    #89
        0xA,
        (
            "Quartz themselves are circuits made\x01",
            "from sepith fragments which are\x01",
            "synthesized and engraved accordingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "They have a hell of a lot of effects when\x01",
            "put into an orbment. They can make you\x01",
            "stronger, faster, all kinds of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "Quartz are basically useless without an\x01",
            "orbment's drive mechanism, and that's not\x01",
            "the only limitation they've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "You see, some slots only allow certain kinds\x01",
            "of quartz to be set in them, limited by element.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "Particularly potent quartz will also only\x01",
            "function if placed into upgraded orbment slots.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_21C7")


    ChrTalk(    #94
        0xA,
        (
            "Sepith are small fragments of septium,\x01",
            "commonly held by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "There are seven different 'colors' or\x01",
            "elements of sepith: #56IEarth, #57IWater, #58IFire,\x01",
            "#59IWind, #62ITime, #60ISpace, and #61IMirage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "Just about any store will take sepith\x01",
            "off your hands for some money, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "You can also take them to a factory to\x01",
            "have them made into quartz or orbment\x01",
            "slot upgrades!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_2351")


    ChrTalk(    #98
        0xA,
        (
            "Oh, right. One of the new tricks with\x01",
            "the new model combat orbment is\x01",
            "slot upgrading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "A lot of the higher-end quartz for\x01",
            "these new things are stupidly potent,\x01",
            "but...there's a catch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "That kind of circuitry is going to require\x01",
            "adjustments and upgrades to your slots\x01",
            "before you can use it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "Good news is, the upgrades will also\x01",
            "increase the maximum 'EP' charge your\x01",
            "orbment can hold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "You'll need sepith to do it,\x01",
            "but it's worth it, trust me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_252C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_253C")

    label("loc_253C")

    OP_56(0x0)
    Jump("loc_1A0D")

    label("loc_2541")


    ChrTalk(    #103
        0xA,
        (
            "Okay, you've listened to me ramble\x01",
            "on long enough. Let's make some\x01",
            "quartz and get you over to Kurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "You want my advice? You should\x01",
            "make sure you can use some healing\x01",
            "arts, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "Do you know what kind of quartz\x01",
            "are required for healing arts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "Your Bracer Notebook will have a full\x01",
            "list of arts and their requirements.\x01",
            "Make sure to check it.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC5, 0x1, 0x8)
    OP_28(0xC5, 0x1, 0x10)
    OP_28(0xC5, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_7_182E end

    SaveToFile()

Try(main)
