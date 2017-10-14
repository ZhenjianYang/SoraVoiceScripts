from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Private Antose',                       # 9
        'Private Lacos',                        # 10
        'Private Scott',                        # 11
        'Private Harold',                       # 12
        'Royal Army Soldier',                   # 13
        'Royal Army Soldier',                   # 14
        'Milch Main Road',                      # 15
        'East Bose Highway',                    # 16
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
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3300,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
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
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -1980,
        Z                   = -410,
        Y                   = -40440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 440,
        Z                   = -510,
        Y                   = 41850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 5680,
        TriggerZ            = -260,
        TriggerY            = -27360,
        TriggerRange        = 1500,
        ActorX              = 5680,
        ActorZ              = 1700,
        ActorY              = -27360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9630,
        TriggerZ            = -150,
        TriggerY            = 27430,
        TriggerRange        = 1500,
        ActorX              = -9630,
        ActorZ              = 1700,
        ActorY              = 27430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13270,
        TriggerZ            = -30,
        TriggerY            = -5630,
        TriggerRange        = 1000,
        ActorX              = -12930,
        ActorZ              = -800,
        ActorY              = -2830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21E",          # 00, 0
        "Function_1_249",          # 01, 1
        "Function_2_276",          # 02, 2
        "Function_3_3F3",          # 03, 3
        "Function_4_54D",          # 04, 4
        "Function_5_B67",          # 05, 5
        "Function_6_F60",          # 06, 6
        "Function_7_14BC",         # 07, 7
        "Function_8_1836",         # 08, 8
        "Function_9_18FF",         # 09, 9
        "Function_10_1994",        # 0A, 10
        "Function_11_1B4D",        # 0B, 11
        "Function_12_1BBF",        # 0C, 12
    )


    def Function_0_21E(): pass

    label("Function_0_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_228")
    Jump("loc_248")

    label("loc_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_248")

    Return()

    # Function_0_21E end

    def Function_1_249(): pass

    label("Function_1_249")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFE0FE8, 0x230005)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275")
    OP_6F(0x1, 420)
    OP_6F(0x2, 420)

    label("loc_275")

    Return()

    # Function_1_249 end

    def Function_2_276(): pass

    label("Function_2_276")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DD")

    label("loc_29B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DD")

    label("loc_2B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DD")

    label("loc_2CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DD")

    label("loc_2E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DD")

    label("loc_2FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DD")

    label("loc_318")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DD")

    label("loc_331")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DD")

    label("loc_34A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DD")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DD")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DD")

    label("loc_395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DD")

    label("loc_3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DD")

    label("loc_3C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DD")

    label("loc_3F2")

    Return()

    # Function_2_276 end

    def Function_3_3F3(): pass

    label("Function_3_3F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54C")
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x438A, 0xFFFFFFC4, 0xFFFF9E94, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFABBE, 0xFFFFFF88, 0xFFFF9C14, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFAB46, 0xFFFFFEFC, 0xFFFF8DC8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFA, 0xFFFFFEF2, 0xFFFF9034, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1054, 0xFFFFFF10, 0xFFFF89B8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C10, 0xFFFFFE2A, 0xFFFF8A08, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C1A, 0x50, 0xFFFFD79C, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4236, 0xA, 0xFFFFD6E8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4218, 0x78, 0xFFFFE1BA, 0x9C4, 0x0)
    Jump("Function_3_3F3")

    label("loc_54C")

    Return()

    # Function_3_3F3 end

    def Function_4_54D(): pass

    label("Function_4_54D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_6C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_643")

    ChrTalk(    #0
        0xFE,
        "Mr. Ashton just came by on his rounds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Even now, he's steady as a rock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I guess the real cream of the military\x01",
            "are different in this kind of situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "He's the man I admire most after\x01",
            "General Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6C6")

    label("loc_643")


    ChrTalk(    #4
        0xFE,
        "Even now, Mr. Ashton's steady as a rock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I guess the real cream of the military\x01",
            "are different in this kind of situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6")

    Jump("loc_B63")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_83D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(    #6
        0xFE,
        (
            "Man, guarding an open gate's a real\x01",
            "nail biter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Not being able to use my orbal gun\x01",
            "makes this a pretty scary assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If those crimson soldiers were to attack\x01",
            "now, we'd be in some serious trouble...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_83A")

    label("loc_7B7")


    ChrTalk(    #9
        0xFE,
        (
            "Man, guarding an open gate's a real\x01",
            "nail biter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Not being able to use my orbal gun\x01",
            "makes this a pretty scary assignment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83A")

    Jump("loc_B63")

    label("loc_83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8DF")

    ChrTalk(    #11
        0xFE,
        (
            "I'm sure the general must be very relieved\x01",
            "to have this dragon case over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The market's reopened, too, so I hope\x01",
            "peaceful days come back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B63")

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_952")

    ChrTalk(    #13
        0xFE,
        "The dragon capture plan's hit a snag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It's frustrating, but there's not much\x01",
            "we can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F5")

    label("loc_952")


    ChrTalk(    #15
        0xFE,
        "The dragon capture plan's hit a snag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It's frustrating, but there's not much\x01",
            "we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "This time, we've just got to leave it to\x01",
            "the air forces.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9F5")

    Jump("loc_B63")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A82")

    ChrTalk(    #18
        0xFE,
        (
            "Mr. Ashton on the east side is an\x01",
            "incredible person!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "His orders during the patrol of Rolent\x01",
            "were just perfect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B63")

    label("loc_A82")


    ChrTalk(    #20
        0xFE,
        (
            "Mr. Ashton on the east side is an\x01",
            "incredible person!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "His orders during the patrol of Rolent\x01",
            "were just perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He's the kind of guy I want to be like.\x01",
            "Whatever happens, he remains calm\x01",
            "and composed as ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B63")

    TalkEnd(0x8)
    Return()

    # Function_4_54D end

    def Function_5_B67(): pass

    label("Function_5_B67")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_BFF")

    ChrTalk(    #23
        0xFE,
        (
            "The commander's a man of experience,\x01",
            "having lived through the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I guess that's why he can always remain\x01",
            "so calm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CB1")

    ChrTalk(    #25
        0xFE,
        (
            "For all the airships out of service, there\x01",
            "sure aren't many travelers on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Guess not many people want to risk\x01",
            "wandering around in an emergency\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(    #27
        0xFE,
        (
            "The dragon mess has finally been\x01",
            "put behind us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I wonder if the air force managed to\x01",
            "get their side of things done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #29
        0xFE,
        "*shiver* *shiver*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I-I hope the dragon doesn't come here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFA")

    label("loc_D8F")


    ChrTalk(    #31
        0xFE,
        (
            "Do y-you think the dragon breathes fire\x01",
            "from its mouth...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "I-I hope it doesn't come this way.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DFA")

    Jump("loc_F5C")

    label("loc_DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E8C")

    ChrTalk(    #33
        0xFE,
        (
            "We were busy managing the gate during\x01",
            "those foggy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I hope I never see anything like that\x01",
            "crazy fog ever again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_E8C")


    ChrTalk(    #35
        0xFE,
        (
            "That fog a while back got us real busy\x01",
            "with managing the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "But I bet that bracer on that escort\x01",
            "mission had it even harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Must've been tough to keep track of\x01",
            "your charges in that fog.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F5C")

    TalkEnd(0x9)
    Return()

    # Function_5_B67 end

    def Function_6_F60(): pass

    label("Function_6_F60")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1003")

    ChrTalk(    #38
        0xFE,
        (
            "All the airships in the air during that\x01",
            "phenomenon were forced to make\x01",
            "emergency landings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "*shiver* I'm sure glad I wasn't on\x01",
            "an airship...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B8")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")

    ChrTalk(    #40
        0xFE,
        (
            "Thanks to some weird gizmo we got,\x01",
            "we managed to get communications\x01",
            "back online.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Hearing reports come in from other\x01",
            "regions is just depressing, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Ugh... Between that and the whole fog\x01",
            "thing, things have just been gettin' worse\x01",
            "and worse.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1193")

    label("loc_111D")


    ChrTalk(    #43
        0xFE,
        (
            "Hearing reports come in from other\x01",
            "regions is just depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "What the heck's going on in this country...?\x02",
    )

    CloseMessageWindow()

    label("loc_1193")

    Jump("loc_14B8")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1317")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1251")

    ChrTalk(    #45
        0xFE,
        (
            "This place is pretty peaceful.\x01",
            "Just being here mellows you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "The mission in Rolent was worth\x01",
            "doing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "I feel like I'm better suited to this place.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1314")

    label("loc_1251")


    ChrTalk(    #48
        0xFE,
        (
            "With the Rolent patrols done, I'm back\x01",
            "to my normal duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "It was pretty nerve-racking over\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "By comparison, it's nice and peaceful\x01",
            "here. Just being here mellows a guy out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1314")

    Jump("loc_14B8")

    label("loc_1317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_14B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1396")

    ChrTalk(    #51
        0xFE,
        (
            "The sky bandits are powerless at\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "When the leaders were captured,\x01",
            "the members all split.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B8")

    label("loc_1396")


    ChrTalk(    #53
        0xFE,
        (
            "So some of the sky bandits appeared\x01",
            "in Bose, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Rumor has it there was a pretty skilled\x01",
            "guy with 'em, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Eh, probably no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "The sky bandits are powerless at\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "When the leaders were captured,\x01",
            "the members all split. So I was told,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14B8")

    TalkEnd(0xA)
    Return()

    # Function_6_F60 end

    def Function_7_14BC(): pass

    label("Function_7_14BC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_15B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154B")

    ChrTalk(    #58
        0xFE,
        (
            "All the stuff that runs on orbal energy's\x01",
            "dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Thanks to that, not even freight vehicles\x01",
            "are passing today.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_15B1")

    label("loc_154B")


    ChrTalk(    #60
        0xFE,
        (
            "All the stuff that runs on orbal energy's\x01",
            "dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "A-And the guns we use are all orbal, too...\x02",
    )

    CloseMessageWindow()

    label("loc_15B1")

    Jump("loc_1832")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161A")

    ChrTalk(    #62
        0xFE,
        "You're the bracers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Okay, you can pass. All part of our orders.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1656")

    label("loc_161A")


    ChrTalk(    #64
        0xFE,
        "Bracers are free to pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "All part of our orders.\x02",
    )

    CloseMessageWindow()

    label("loc_1656")

    Jump("loc_1832")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(    #66
        0xFE,
        (
            "The patrol of Rolent was one heart-racing\x01",
            "moment after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I'm really glad we made it back in one\x01",
            "piece.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_16E2")


    ChrTalk(    #68
        0xFE,
        (
            "The patrol of Rolent was one heart-racing\x01",
            "moment after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Our range of sight was awful. I could barely\x01",
            "see my own feet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I'm really glad we made it back in one\x01",
            "piece.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17A0")

    Jump("loc_1832")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1832")

    ChrTalk(    #71
        0xFE,
        (
            "One way or another, we're back on high\x01",
            "alert here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Not that it changes things for me.\x01",
            "I'll be doing the same stuff as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1832")

    TalkEnd(0xB)
    Return()

    # Function_7_14BC end

    def Function_8_1836(): pass

    label("Function_8_1836")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_18FB")

    ChrTalk(    #73
        0xFE,
        (
            "We're a supplementary force for\x01",
            "Ashton's group from Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "We'll be keeping this gate secure for\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "It's just a temporary assignment,\x01",
            "but it's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FB")

    TalkEnd(0xC)
    Return()

    # Function_8_1836 end

    def Function_9_18FF(): pass

    label("Function_9_18FF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_1990")

    ChrTalk(    #76
        0xFE,
        (
            "A number of our supplementary\x01",
            "forces went to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Man, if I had a choice, I'd rather take\x01",
            "the Rolent patrol than be here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1990")

    TalkEnd(0xD)
    Return()

    # Function_9_18FF end

    def Function_10_1994(): pass

    label("Function_10_1994")

    EventBegin(0x1)

    ChrTalk(    #78
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_19C0():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19C0)

    def lambda_19D0():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_19D0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #79
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3D")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x2, 0xFFFFCC2A, 0xFFFFFFE2, 0xFFFFEA02, 0x168, 0xFFFFCD7E, 0xFFFFFCE0, 0xFFFFF4F2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_1B37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2E")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x4)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05Recorded Verte Bridge fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1B2E")

    Jump("loc_1B37")

    label("loc_1B31")

    OP_28(0x73, 0x1, 0x400)

    label("loc_1B37")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_1B4C")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4C")
    EventEnd(0x1)

    label("loc_1B4C")

    Return()

    # Function_10_1994 end

    def Function_11_1B4D(): pass

    label("Function_11_1B4D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #81
        (
            "\x07\x05East: City of Rolent - 172 selge\x01",
            "West: City of Bose - 420 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1B4D end

    def Function_12_1BBF(): pass

    label("Function_12_1BBF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #82
        (
            "\x07\x05West: City of Bose - 420 selge\x01",
            "East: City of Rolent - 172 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1BBF end

    SaveToFile()

Try(main)
