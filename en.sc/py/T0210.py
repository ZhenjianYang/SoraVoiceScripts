from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0210   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0210.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0210   ._SN',
            'ED6_DT21/T0210_1 ._SN',
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
        'Mylene',                               # 9
        'Lita',                                 # 10
        'Mayor Klaus',                          # 11
        'Mayor Klaus',                          # 12
        'Paddington',                           # 13
        '紅茶',                                 # 14
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


    AddCharChip(
        'ED6_DT07/CH01180 ._CH',             # 00
        'ED6_DT26/CH20330 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02350 ._CH',             # 03
        'ED6_DT07/CH01250 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH02353 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01180P._CP',             # 00
        'ED6_DT26/CH20330P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02350P._CP',             # 03
        'ED6_DT07/CH01250P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH02353P._CP',             # 06
    )

    DeclNpc(
        X                   = 5860,
        Z                   = 0,
        Y                   = 64489,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = -1800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 6080,
        Z                   = 0,
        Y                   = -4640,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 5350,
        Z                   = 200,
        Y                   = -6560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3860,
        Z                   = 0,
        Y                   = -5520,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 200400,
        Z                   = 500,
        Y                   = 49090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_354",          # 02, 2
        "Function_3_4D1",          # 03, 3
        "Function_4_E26",          # 04, 4
        "Function_5_1922",         # 05, 5
        "Function_6_3561",         # 06, 6
        "Function_7_4496",         # 07, 7
        "Function_8_4618",         # 08, 8
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1D2")
    SetChrPos(0x9, 7070, 0, 64599, 0)
    SetChrPos(0x8, 202000, 0, 1390, 82)

    label("loc_1D2")

    Jump("loc_2FD")

    label("loc_1D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1F0")
    SetChrPos(0x9, 6700, 0, 62710, 270)
    Jump("loc_2FD")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_239")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 25)
    Jump("loc_2FD")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_278")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    Jump("loc_2FD")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrPos(0x8, 200400, 0, 48360, 90)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    OP_4A(0x9, 255)
    SetChrFlags(0xA, 0x80)
    Jump("loc_2FD")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0")
    SetChrFlags(0x8, 0x10)

    label("loc_2D0")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, 6700, 0, 62710, 270)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2FD")

    label("loc_2F3")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_30B")
    OP_A3(0x10F0)
    Event(0, 8)

    label("loc_30B")

    Return()

    # Function_0_1A2 end

    def Function_1_30C(): pass

    label("Function_1_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_353")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_327")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_6F(0x5, 10)
    Jump("loc_353")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_353")
    Jump("loc_353")

    label("loc_353")

    Return()

    # Function_1_30C end

    def Function_2_354(): pass

    label("Function_2_354")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4BB")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4BB")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4BB")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4BB")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4BB")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4BB")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4BB")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4BB")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4BB")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4BB")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4BB")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4BB")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4BB")

    label("loc_4A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4BB")

    label("loc_4D0")

    Return()

    # Function_2_354 end

    def Function_3_4D1(): pass

    label("Function_3_4D1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D1")

    ChrTalk(    #0
        0xFE,
        (
            "The stove isn't working, so cooking is even\x01",
            "more of a chore than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "The real problem is trying to decide\x01",
            "what to even try and make with what we\x01",
            "can still use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "*sigh* I really need to ask the mistress\x01",
            "for help...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_67F")

    label("loc_5D1")


    ChrTalk(    #3
        0xFE,
        (
            "The stove isn't working, so cooking is even\x01",
            "more of a chore than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "The real problem is trying to decide\x01",
            "what to even try and make with what we\x01",
            "can still use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67F")

    Jump("loc_E22")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C7")

    ChrTalk(    #5
        0xFE,
        "Ah, Estelle, Scherazard!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D5")

    label("loc_6C7")


    ChrTalk(    #6
        0xFE,
        "Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_6D5")


    ChrTalk(    #7
        0xFE,
        (
            "Umm, thank you for everything during the\x01",
            "fog trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Don't worry about me. I'm back on my\x01",
            "feet and everything! See?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7CF")

    label("loc_75A")


    ChrTalk(    #9
        0xFE,
        (
            "Thank you for everything during the\x01",
            "fog trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Don't worry about me. I'm back on my\x01",
            "feet and everything!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF")

    Jump("loc_E22")

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_A1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8AF")

    ChrTalk(    #11
        0xFE,
        (
            "When I was asleep, I had this very long,\x01",
            "elaborate dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You see, the mistress makes a tea\x01",
            "with the most delicious scent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "A single sniff of it is enough to send me\x01",
            "back to my childhood...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1A")

    label("loc_8AF")


    ChrTalk(    #14
        0xFE,
        (
            "When I was asleep, I had this very long,\x01",
            "elaborate dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "It was a dream of when Mayor Klaus and\x01",
            "the mistress first took me in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "The mistress makes a tea with the most\x01",
            "delicious scent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I've loved that tea ever since I came to\x01",
            "live here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "And the tea in the dream...\x01",
            "The scent was so clear. I still can't\x01",
            "really believe it was a dream.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A1A")

    Jump("loc_E22")

    label("loc_A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(    #19
        0xFE,
        (
            "Carry the tea, clear it up,\x01",
            "and then right back to cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Oh! And can't forget to smile at the guests...\x01",
            "Haha! ☆\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_A3(0x1)
    Jump("loc_C7C")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BA4")

    ChrTalk(    #21
        0xFE,
        "The mistress' tea really is amazing, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "A sip of the mistress' tea will warm you\x01",
            "right up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Hmm, it seems like there's some kind of\x01",
            "secret to that tea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Ohh, but, right, I need to hurry up\x01",
            "and serve it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C7C")

    label("loc_BA4")


    ChrTalk(    #25
        0xFE,
        (
            "*sigh* So, so busy.\x01",
            "There are so many guests today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I need to serve tea, but the cleaning needs\x01",
            "to get done, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Clean, carry the tea, clear that,\x01",
            "clean again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Round and around it goes...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C7C")

    Jump("loc_E22")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D05")

    ChrTalk(    #29
        0xFE,
        (
            "Mayor Klaus and his wife are currently\x01",
            "in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I believe they're touring the capital\x01",
            "before returning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E22")

    label("loc_D05")


    ChrTalk(    #31
        0xFE,
        "Oh! Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Yes, Estelle, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "So you've returned to Rolent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Sadly, I'm afraid Mayor Klaus is in Grancel\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "The mistress is also in Grancel,\x01",
            "at least for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Mmm... The mistress wanted to see you\x01",
            "very badly, too, Estelle. It's a shame.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E22")

    TalkEnd(0x9)
    Return()

    # Function_3_4D1 end

    def Function_4_E26(): pass

    label("Function_4_E26")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB6")
    Jump("loc_EF8")

    label("loc_EB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF8")

    label("loc_ED2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF8")

    label("loc_EEE")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF8")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_END)), "loc_1066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(    #37
        0xB,
        (
            "#602FHaving the passenger airliners grounded\x01",
            "entirely already makes this an\x01",
            "emergency.\x02\x03",

            "It seems my decision to delay my trip\x01",
            "to Grancel was wise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_FC7")


    ChrTalk(    #38
        0xB,
        (
            "#602FHaving the passenger airliners grounded\x01",
            "entirely already makes this an\x01",
            "emergency.\x02\x03",

            "I'm sorry, but I hope we can count on\x01",
            "your aid for the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1063")

    Jump("loc_1919")

    label("loc_1066")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #39
        0xB,
        "#601FAhh, Estelle, Scherazard, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1006FHey, Mayor Klaus!\x01",
            "Sorry we've been kinda missing for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(    #41
        0xB,
        (
            "#603FAnd...Princess Klaudia.\x01",
            "I am glad to see you in good health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#048FThank you, Mayor Klaus.\x01",
            "You as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        "#021FIt's good to see you well, Mayor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_11A4")


    ChrTalk(    #44
        0x103,
        "#021FIt's good to see you well, Mayor.\x02",
    )

    CloseMessageWindow()

    label("loc_11D0")


    ChrTalk(    #45
        0xB,
        (
            "#601FHaha! Well, seeing both of you does me well,\x01",
            "if nothing else. You are both a source of\x01",
            "pride for Rolent.\x02\x03",

            "#600FSo what brings you home?\x02\x03",

            "Work as always, I suspect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1015FWell...sorta.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05Estelle explained how her group was stopped in\x01",
            "Rolent by the fog while in transit to Bose.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #48
        0xB,
        (
            "#602FAhh, I see. You're victims of this\x01",
            "cursed fog as well, hmm?\x02\x03",

            "It seems I was right to delay my trip\x01",
            "to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1015FHuh? What were you going to do there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#023FWait, the capital...\x02\x03",

            "Were you invited to the non-aggression\x01",
            "pact signing, Mayor?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #51
        0x101,
        (
            "#1004FWhoa!\x02\x03",

            "The signing ceremony? Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        (
            "#603FMmm... yes, I was.\x02\x03",

            "All of the leaders of the provinces were\x01",
            "invited to attend.\x02\x03",

            "But the state of the regions we govern\x01",
            "must come first. I can hardly leave Rolent\x01",
            "when this is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007FNo kidding...\x02\x03",

            "Guess it's not all roses and sunshine for\x01",
            "you, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#602FRegardless, I intend to make sure nothing\x01",
            "befalls Rolent during this.\x02\x03",

            "If any trouble should arise, I will\x01",
            "doubtless need the guild's help to deal\x01",
            "with it.\x02\x03",

            "I hope you'll be willing to help, friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1006FOf course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D4")

    ChrTalk(    #56
        0x106,
        (
            "#050FYeah, don't worry, we'll be there.\x02\x03",

            "Sorta feels like fate that we're here,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_16D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1756")

    ChrTalk(    #57
        0x108,
        (
            "#070FWe will be glad to be of aid, sir.\x02\x03",

            "One cannot help but feel the hand of She\x01",
            "Above in guiding us here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_1756")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F5")

    ChrTalk(    #58
        0x104,
        (
            "#030FHeh, leave it to us, my good man.\x02\x03",

            "One cannot help but feel the gentle hand\x01",
            "of Aidios on our shoulders, that we\x01",
            "should be here now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_17F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1870")

    ChrTalk(    #59
        0x105,
        (
            "#040FWe will do everything we can,\x01",
            "Mayor Klaus.\x02\x03",

            "It almost feels like fate that we're here\x01",
            "now, really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1870")


    ChrTalk(    #60
        0xB,
        "#603FYou have my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#020FIf anything comes up, just contact the\x01",
            "guildhouse.\x02\x03",

            "Aina will know where to find us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#600FIf the time comes, I shall.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1881)
    OP_A2(0x2)

    label("loc_1919")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_E26 end

    def Function_5_1922(): pass

    label("Function_5_1922")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BF")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #63
        0xA,
        (
            "#601FAhh, Estelle, welcome.\x01",
            "I see Joshua rejoined you at last.\x02\x03",

            "We still owe you much for your help\x01",
            "with the fog crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1008FIt's okay, Mayor Klaus.\x01",
            "We didn't really do much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1044FFog crisis...?\x02\x03",

            "#1043FSo the society hit here, too, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#602FWhat's going on now makes that look\x01",
            "like a spot of bad weather, though.\x02\x03",

            "Is...this phenomenon really affecting the\x01",
            "entire kingdom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1026FYeah...everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1035FEvery single orbment in Liberl's borders\x01",
            "is currently non-functional, essentially\x01",
            "without exception.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C60")

    ChrTalk(    #69
        0x103,
        (
            "#522FAnd thanks to that, all forms of transport\x01",
            "are non-functional, most forms of\x01",
            "heating, or cooking...\x02\x03",

            "If this continues much longer, daily\x01",
            "life as we've known it will be nearly\x01",
            "impossible for many people.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_1DE2")

    label("loc_1C60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D10")

    ChrTalk(    #70
        0x106,
        (
            "#050FAnd now transportation ain't workin',\x01",
            "stoves ain't workin', lamps, guns...\x02\x03",

            "This keeps up, people are really gonna\x01",
            "start feelin' the squeeze.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_1DE2")

    label("loc_1D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE2")

    ChrTalk(    #71
        0x108,
        (
            "#072FAnd because of it, transportation is\x01",
            "paralyzed, as are many kinds of modern\x01",
            "convenience...\x02\x03",

            "Should power not return soon, many\x01",
            "people may struggle to go about their\x01",
            "lives at all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)

    label("loc_1DE2")


    ChrTalk(    #72
        0xA,
        (
            "#603FI see... It's as dire as I feared.\x02\x03",

            "We need to think of some kind of response,\x01",
            "and urgently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015FI dunno, Rolent doesn't seem as bad as\x01",
            "some other places we've seen.\x02\x03",

            "Sorta seems like everyone's just going\x01",
            "about things they always have...\x01",
            "except for Mr. Melders, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1040FThat's a good point.\x02\x03",

            "It certainly isn't like Bose or some of\x01",
            "the other large cities.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #75
        0xA,
        (
            "#600FI suppose it's because Rolent does\x01",
            "not rely on orbments as heavily.\x02\x03",

            "As far as orbments go for civic functions,\x01",
            "they're really just used in the clock tower\x01",
            "and the airships at our landing port.\x02\x03",

            "#601FIt likely helps that the people of\x01",
            "Rolent have always been fairly...\x01",
            "'laid-back.'\x02\x03",

            "I think our people will take to even this\x01",
            "crisis with some measure of calmness.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2111")

    ChrTalk(    #76
        0x103,
        "#021FWouldn't surprise me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2168")

    label("loc_2111")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2141")

    ChrTalk(    #77
        0x106,
        "#051FHeh. I can see that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2168")

    label("loc_2141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2168")

    ChrTalk(    #78
        0x108,
        "#070FHeh! Possibly.\x02",
    )

    CloseMessageWindow()

    label("loc_2168")


    ChrTalk(    #79
        0x101,
        (
            "#1007FYeeeah... The joys of living in the 'boonies,'\x01",
            "as Kevin put it once, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #80
        0xA,
        (
            "#600FOne way or another, however...\x01",
            "we must be ready to help one another\x01",
            "in these troubled times.\x02\x03",

            "For my part, I am currently taking stock of\x01",
            "what aid we can offer the other provinces,\x01",
            "and making plans accordingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1040FIt'll be appreciated, I'm sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006FIf you need the guild's help, just contact us!\x01",
            "You'll find the guild's phone is a liiittle\x01",
            "bit more functional than others right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#600FI'll keep that mind.\x02\x03",

            "Well, then, everyone.\x01",
            "Good luck to you. To us all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20A8)
    Jump("loc_2C97")

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_297B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2690")

    ChrTalk(    #84
        0xA,
        (
            "#600FAh, by the way, Estelle.\x02\x03",

            "I heard you resolved the crisis\x01",
            "at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1000FWord of that's already getting around,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#1040FIt was close, but we did manage to rescue\x01",
            "the miners.\x02\x03",

            "Really did feel like victory by the skin\x01",
            "of our teeth, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "#600FThat entire incident is just one more\x01",
            "side-effect of this massive orbal crisis.\x02\x03",

            "If that happened here, I shudder to\x01",
            "think what else may be happening to our\x01",
            "neighbors.\x02\x03",

            "Be careful, friends.\x01",
            "I fear the danger has only just begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1000FWe'll be okay!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2619")

    ChrTalk(    #89
        0x103,
        "#020FWe'll be careful, Mayor Klaus.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2687")

    label("loc_2619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264B")

    ChrTalk(    #90
        0x106,
        "#050FYeah, we'll watch out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2687")

    label("loc_264B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2687")

    ChrTalk(    #91
        0x108,
        "#070FWe shall remain alert, Mayor Klaus.\x02",
    )

    CloseMessageWindow()

    label("loc_2687")

    OP_A3(0x3)
    OP_A2(0x2)
    Jump("loc_2978")

    label("loc_2690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2881")

    ChrTalk(    #92
        0xA,
        (
            "#600FI heard you resolved the crisis at the\x01",
            "Malga Mine.\x02\x03",

            "That entire incident is just one more\x01",
            "side-effect of this massive orbal crisis.\x02\x03",

            "If that happened here, I shudder to\x01",
            "think what else may be happening to our\x01",
            "neighbors.\x02\x03",

            "Be careful, friends.\x01",
            "I fear the danger has only just begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1000FYou bet'cha!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280D")

    ChrTalk(    #94
        0x103,
        "#020FWe'll be careful, Mayor Klaus.\x02",
    )

    CloseMessageWindow()
    Jump("loc_287B")

    label("loc_280D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_283F")

    ChrTalk(    #95
        0x106,
        "#050FYeah, we'll watch out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_287B")

    label("loc_283F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287B")

    ChrTalk(    #96
        0x108,
        "#070FWe shall remain alert, Mayor Klaus.\x02",
    )

    CloseMessageWindow()

    label("loc_287B")

    OP_A2(0x2)
    Jump("loc_2978")

    label("loc_2881")


    ChrTalk(    #97
        0xA,
        (
            "#600FWhat happened to the Malga Mine is just\x01",
            "another side-effect of this greatest of\x01",
            "crises.\x02\x03",

            "If that happened here, I shudder to\x01",
            "think what else may be happening to our\x01",
            "neighbors.\x02\x03",

            "Be careful, friends.\x01",
            "I fear the danger has only just begun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2978")

    Jump("loc_2C97")

    label("loc_297B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(    #98
        0xA,
        (
            "#600FRolent is less reliant on orbments than\x01",
            "other cities, and its people have always\x01",
            "been more...'laid-back.'\x02\x03",

            "Perhaps that is why we are not suffering\x01",
            "the panic other cities face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C97")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD0")

    ChrTalk(    #99
        0xA,
        (
            "#603FWith powered shipping shut down, securing\x01",
            "all the necessities of life may be a problem.\x02\x03",

            "In truth, Rolent is better off in that\x01",
            "regard. So much of the city outskirts is\x01",
            "given over to agriculture...\x02\x03",

            "#602FThat's not nearly as true of cities\x01",
            "like Bose or Zeiss, though...\x01",
            "and certainly not Grancel.\x02\x03",

            "I will examine the situation and see if\x01",
            "we can get them some support somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2C97")

    label("loc_2BD0")


    ChrTalk(    #100
        0xA,
        (
            "#602FWith powered shipping shut down, securing\x01",
            "all the necessities of life may be a problem.\x02\x03",

            "But other provinces will be even worse off.\x01",
            "I will continue to see what I can do for\x01",
            "our neighbors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C97")

    Jump("loc_355D")

    label("loc_2C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_31CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 3)), scpexpr(EXPR_END)), "loc_2D45")

    ChrTalk(    #101
        0xA,
        (
            "#600FIt seems you're ready to depart for\x01",
            "another province, but please, be careful.\x02\x03",

            "Your enemy--OUR enemy--is more twisted\x01",
            "than I could've imagined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C8")

    label("loc_2D45")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #102
        0xA,
        (
            "#600FAh, Estelle, everyone!\x02\x03",

            "I have heard all the details of what\x01",
            "happened from Aina.\x02\x03",

            "A great deal of it still seems to be under\x01",
            "investigation, so I doubt I was told\x01",
            "everything, but...\x02\x03",

            "#603FWho could've even imagined.\x01",
            "A fog that bends dreams...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1007FTrust me, we're in the middle of it all\x01",
            "and we don't know much more.\x02\x03",

            "Anyway, right now we're just chasing\x01",
            "snakes from region to region.\x02\x03",

            "#1006FHopefully we can catch one sooner or\x01",
            "later and get some real answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "#602FYes, good. For my part, I did plan on\x01",
            "keeping the full truth of this incident\x01",
            "from the citizenry, as well.\x02\x03",

            "Everyone is still recovering from the\x01",
            "trauma of seeing loved ones comatose...\x01",
            "I do not wish to scare them further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x103,
        (
            "#020FIt's probably for the best, for now.\x02\x03",

            "Saying the wrong thing right now could\x01",
            "just lead to chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#600FAnd I imagine you are off to new horizons.\x01",
            "I can only ask you all to be careful.\x02\x03",

            "Your enemy--OUR enemy--is more twisted\x01",
            "than I could've imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1002FDon't worry, we're used to the twisting\x01",
            "by now.\x02\x03",

            "#1000FAnyway, take care, Mayor Klaus!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "#601FAnd you, Estelle.\x01",
            "Come back safe to us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A63)

    label("loc_31C8")

    Jump("loc_355D")

    label("loc_31CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_33B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_328E")

    ChrTalk(    #109
        0xA,
        (
            "#600FGood work evacuating all the citizens to\x01",
            "within the city walls.\x02\x03",

            "I'm sure the families of the miners must\x01",
            "be relieved.\x02\x03",

            "I hope we can continue to rely on your\x01",
            "support.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AE")

    label("loc_328E")


    ChrTalk(    #110
        0xA,
        (
            "#600FAshton has his men working like the\x01",
            "clock tower. It's impressive to watch.\x02\x03",

            "By the by, good work evacuating all the\x01",
            "citizens from outlying areas to within\x01",
            "the city walls.\x02\x03",

            "I'm sure the families of the miners must\x01",
            "be relieved.\x02\x03",

            "I hope we can continue to rely on your\x01",
            "support.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_33AE")

    Jump("loc_355D")

    label("loc_33B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_355D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3450")

    ChrTalk(    #111
        0xA,
        (
            "#600FAshton just came by to report to\x01",
            "me as part of his assignment.\x02\x03",

            "It's heartening to have a Rolent man\x01",
            "taking command of our defense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_355D")

    label("loc_3450")


    ChrTalk(    #112
        0xA,
        (
            "#600FAshton just came by to report to\x01",
            "me as part of his assignment.\x02\x03",

            "It's heartening to have a Rolent man\x01",
            "taking command of our defense.\x02\x03",

            "Not just because he has a sense for the\x01",
            "land, but he also knows the citizenry.\x02\x03",

            "I imagine that was Cassius' entire\x01",
            "intent.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_355D")

    TalkEnd(0xA)
    Return()

    # Function_5_1922 end

    def Function_6_3561(): pass

    label("Function_6_3561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3579")
    SetChrFlags(0xFE, 0x10)

    label("loc_3579")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_36E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3654")

    ChrTalk(    #113
        0xFE,
        "Estelle, Joshua, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I heard from my husband.\x01",
            "Something happened at the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I'm glad you were all there,\x01",
            "in any event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Please, continue to help my husband,\x01",
            "and our city.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_36DE")

    label("loc_3654")


    ChrTalk(    #117
        0xFE,
        (
            "What happened at the mine is a result\x01",
            "of these wider orbal problems, too,\x01",
            "I heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "We just can't seem to catch a break,\x01",
            "can we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DE")

    Jump("loc_4492")

    label("loc_36E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_399C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3902")

    ChrTalk(    #119
        0x101,
        "#1001FHi, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#1040FHello.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #121
        0xFE,
        (
            "Oh, hello, Joshua!\x01",
            "With Estelle again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Goodness, how long has it been since\x01",
            "both of you were in our house together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#1040FSince...the robbery, I guess.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(600)

    ChrTalk(    #124
        0x101,
        (
            "#1004FHas it really been that long?\x02\x03",

            "#1016FMan, that feels like years ago!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #125
        0xFE,
        "It shows how much you've grown.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I'm sure work is keeping you busy,\x01",
            "but since you've come all the way back\x01",
            "home together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Do try to find some time to relax and\x01",
            "enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3999")

    label("loc_3902")


    ChrTalk(    #128
        0xFE,
        (
            "And just when I thought the fog had\x01",
            "cleared, our orbments stop working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Sometimes it just feels like our poor\x01",
            "kingdom is cursed, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3999")

    Jump("loc_4492")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 4)), scpexpr(EXPR_END)), "loc_3B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A4B")

    ChrTalk(    #130
        0xFE,
        (
            "I've eaten it before, but I have no\x01",
            "idea how to make it, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "You should ask one of our older\x01",
            "residents who knows more about cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B07")

    label("loc_3A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A76")
    Call(1, 0)
    Jump("loc_3B07")

    label("loc_3A76")


    ChrTalk(    #132
        0xFE,
        (
            "When you find some free time,\x01",
            "come back to Rolent again, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I'll have the best tea and snacks\x01",
            "you've ever had waiting for you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B07")

    Jump("loc_3D08")

    label("loc_3B0A")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #134
        0xFE,
        "Oh, everyone, well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I heard from my husband. You solved the\x01",
            "problem with the comas and the fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Our Lita is up and about,\x01",
            "safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "And it's all thanks to you, Estelle.\x01",
            "Thank you, from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1017FAhaha... Awww, it's nothin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#020FCasual heroism's just part of the\x01",
            "job as a bracer, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #140
        0xFE,
        (
            "When you find some free time,\x01",
            "come back to Rolent again, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I'll have the best tea and snacks\x01",
            "you've ever had waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A64)

    label("loc_3D08")

    Jump("loc_4492")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3D6F")

    ChrTalk(    #142
        0xFE,
        (
            "Lita!\x01",
            "I've made your favorite chamomile tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "Doesn't it smell wonderful?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E6D")

    label("loc_3D6F")


    ChrTalk(    #144
        0xFE,
        (
            "I thought she might wake up if I brought\x01",
            "something to catch her attention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "So I made Lita's favorite chamomile tea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Even though I knew, deep down, it probably\x01",
            "wouldn't have any effect...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "I can't stand just doing nothing for her.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3E6D")

    Jump("loc_4492")

    label("loc_3E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_3FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3EF3")

    ChrTalk(    #148
        0xFE,
        (
            "I heard Ashton's son isn't waking up,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "And yet to be on deployment...\x01",
            "It must be so hard on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3EF3")


    ChrTalk(    #150
        0xFE,
        (
            "Ashton came by a bit ago to meet with\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Apparently his son Luke isn't waking\x01",
            "up either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Such a young child in danger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "It must be terribly hard on Ashton.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3FB0")

    Jump("loc_4492")

    label("loc_3FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_414F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_404F")

    ChrTalk(    #154
        0xFE,
        (
            "I thought, maybe when the morning came...\x01",
            "but reality isn't so kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Good luck with your investigation.\x01",
            "It's my only hope now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_414C")

    label("loc_404F")


    ChrTalk(    #156
        0xFE,
        (
            "Lita's always been so energetic,\x01",
            "so I thought when the morning came...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "...It was a faint hope.\x01",
            "Reality is not so kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "I will keep watching over Lita, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Everyone, good luck with your investigation.\x01",
            "You are my only hope now...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_414C")

    Jump("loc_4492")

    label("loc_414F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4203")

    ChrTalk(    #160
        0xFE,
        (
            "I'm sure the fog outside is terrible,\x01",
            "so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "We've never experienced weather like\x01",
            "this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Why does my heart tremble with\x01",
            "unease so...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4492")

    label("loc_4203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 1)), scpexpr(EXPR_END)), "loc_42C7")

    ChrTalk(    #163
        0xFE,
        (
            "We've never experienced weather like\x01",
            "this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'm sure the citizens are anxious.\x01",
            "We've been having guests all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I hope it's just a passing whim of\x01",
            "nature, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4492")

    label("loc_42C7")


    ChrTalk(    #166
        0x101,
        "#1000FHi, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x103,
        "#020FHello, ma'am! It's been a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #168
        0xFE,
        "Why, Estelle, Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "It certainly has!\x01",
            "Are you working right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1006FYeah, we're gonna patrol the highways\x01",
            "a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "I see... Do be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "You've seen what's happened to the town.\x01",
            "The fog outside is terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "We've never experienced weather like this\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Why does my heart tremble with\x01",
            "unease so...?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x18A1)
    OP_A2(0x4)

    label("loc_4492")

    TalkEnd(0x8)
    Return()

    # Function_6_3561 end

    def Function_7_4496(): pass

    label("Function_7_4496")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_454C")

    ChrTalk(    #175
        0xFE,
        (
            "I came by to talk to the mayor about parts\x01",
            "for the clock tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Well, we're done for now, so I was just on\x01",
            "my way out. Go on, have a word with\x01",
            "the man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4614")

    label("loc_454C")


    ChrTalk(    #177
        0xFE,
        (
            "The fog today reminded me that a few\x01",
            "parts of the clock tower are gettin' a bit\x01",
            "rusty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "So I decided to come talk to the mayor\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "Heh-heh! No point in waiting, as they say!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4614")

    TalkEnd(0xC)
    Return()

    # Function_7_4496 end

    def Function_8_4618(): pass

    label("Function_8_4618")

    EventBegin(0x0)
    SetMapFlags(0x2000000)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x9, 255)
    OP_6F(0x5, 10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, 200280, 0, 48270, 60)
    ClearChrFlags(0x8, 0x80)
    OP_6D(199670, 0, 45910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_46D8():
        OP_6D(201780, 0, 48770, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_46D8)
    FadeToBright(1000, 0)
    Sleep(3000)
    SetChrSubChip(0x9, 1)
    Sleep(300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_8_4618 end

    SaveToFile()

Try(main)
