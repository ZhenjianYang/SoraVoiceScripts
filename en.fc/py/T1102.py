from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1102   ._SN',
        MapName             = 'Bose',
        Location            = 'T1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Receptionist Ted',                     # 9
        'Lakely',                               # 10
        'Norm',                                 # 11
        'Aldan',                                # 12
        'Hardt',                                # 13
        'Berna',                                # 14
        'Airliner',                             # 15
        'Airliner Shadow',                      # 16
        'Bose - North Block',                   # 17
    )

    DeclEntryPoint(
        Unknown_00              = 46000,
        Unknown_04              = 0,
        Unknown_08              = 16500,
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT06/CH20038 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT06/CH20038P._CP',             # 05
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
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
        X                   = 27300,
        Z                   = -10000,
        Y                   = 26800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 48500,
        Z                   = 1500,
        Y                   = 36800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 47600,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 29100,
        Z                   = -3000,
        Y                   = 17200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 0,
        Y                   = 14100,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48090,
        Z                   = 3000,
        Y                   = -20910,
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
        TriggerX            = 46070,
        TriggerZ            = 0,
        TriggerY            = 18140,
        TriggerRange        = 600,
        ActorX              = 46050,
        ActorZ              = 1500,
        ActorY              = 19400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47780,
        TriggerZ            = 0,
        TriggerY            = 15880,
        TriggerRange        = 800,
        ActorX              = 47780,
        ActorZ              = 2200,
        ActorY              = 15880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34950,
        TriggerZ            = -10000,
        TriggerY            = 24520,
        TriggerRange        = 800,
        ActorX              = 34950,
        ActorZ              = -7800,
        ActorY              = 24520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = 0,
        TriggerY            = 17090,
        TriggerRange        = 800,
        ActorX              = 60000,
        ActorZ              = 1500,
        ActorY              = 17090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_368",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_5C8",          # 03, 3
        "Function_4_5CD",          # 04, 4
        "Function_5_10B4",         # 05, 5
        "Function_6_1957",         # 06, 6
        "Function_7_251D",         # 07, 7
        "Function_8_2FBF",         # 08, 8
        "Function_9_37AE",         # 09, 9
        "Function_10_3DA9",        # 0A, 10
        "Function_11_51CA",        # 0B, 11
        "Function_12_5213",        # 0C, 12
        "Function_13_526F",        # 0D, 13
        "Function_14_52E5",        # 0E, 14
        "Function_15_5364",        # 0F, 15
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2E7")
    SetChrPos(0xA, 33980, -9750, 27260, 0)
    SetChrPos(0x9, 51270, 1800, 37990, 90)
    SetChrPos(0xB, 51220, 1500, 51120, 90)
    SetChrPos(0xC, 45170, 0, 17540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E4")
    SetChrFlags(0xC, 0x80)

    label("loc_2E4")

    Jump("loc_350")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_344")
    SetChrPos(0xA, 33980, -9750, 27260, 0)
    SetChrPos(0x9, 51270, 1800, 37990, 90)
    SetChrPos(0xB, 48710, 1500, 33310, 315)
    SetChrPos(0xC, 45170, 0, 17540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xC, 0x80)

    label("loc_341")

    Jump("loc_350")

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_350")
    SetChrFlags(0xC, 0x80)

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_367")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_367")

    Return()

    # Function_0_28A end

    def Function_1_368(): pass

    label("Function_1_368")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE98A0, 0x30042)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C5")
    OP_B1("T1102_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    Jump("loc_44A")

    label("loc_3C5")

    OP_B1("T1102_2")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_6F(0xB, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402")
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    Jump("loc_413")

    label("loc_402")

    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_6F(0xC, 100)

    label("loc_413")

    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_436")
    OP_72(0x9, 0x4)
    OP_72(0xA, 0x4)
    Jump("loc_440")

    label("loc_436")

    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)

    label("loc_440")

    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)

    label("loc_44A")

    Return()

    # Function_1_368 end

    def Function_2_44B(): pass

    label("Function_2_44B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B2")

    label("loc_470")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5B2")

    label("loc_489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5B2")

    label("loc_4A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5B2")

    label("loc_4BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5B2")

    label("loc_4D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5B2")

    label("loc_4ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_506")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5B2")

    label("loc_506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5B2")

    label("loc_51F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_538")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5B2")

    label("loc_538")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_551")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5B2")

    label("loc_551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5B2")

    label("loc_56A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_583")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5B2")

    label("loc_583")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5B2")

    label("loc_59C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B2")

    label("loc_5C7")

    Return()

    # Function_2_44B end

    def Function_3_5C8(): pass

    label("Function_3_5C8")

    Call(0, 4)
    Return()

    # Function_3_5C8 end

    def Function_4_5CD(): pass

    label("Function_4_5CD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    OP_A2(0x0)

    ChrTalk(    #0
        0x8,
        (
            "That's great that the criminals\x01",
            "were caught and all, but it was\x01",
            "after the incident happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "There are several customers that\x01",
            "are now worried because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "I think it's about time we took another\x01",
            "look at the safety of our airliners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_6DE")


    ChrTalk(    #3
        0x8,
        (
            "Though the criminals were caught,\x01",
            "it happened after the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I think it's about time we took another\x01",
            "look at the safety of our airliners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_777")

    Jump("loc_10B0")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6")
    OP_A2(0x0)

    ChrTalk(    #5
        0x8,
        "The Cecilia just departed for Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Whew. Now all that's left is to\x01",
            "get the Linde up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "It appears that it was found intact,\x01",
            "but it seems like it's still under\x01",
            "the army's supervision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Flights are expected to resume once it is\x01",
            "returned to the Orbalship Corporation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_923")

    label("loc_8B6")


    ChrTalk(    #9
        0x8,
        (
            "Once the Linde is returned to the\x01",
            "Orbalship Corporation, flights are\x01",
            "expected to resume on both routes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_923")

    Jump("loc_10B0")

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D3")
    OP_A2(0x0)

    ChrTalk(    #10
        0x8,
        (
            "Only flights for the counter-clockwise\x01",
            "looping Cecilia have resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "All those passengers who are boarding,\x01",
            "please make your way to the gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC4")

    label("loc_9D3")


    ChrTalk(    #12
        0x8,
        (
            "We finally received an explanation\x01",
            "from the mayor about the missing\x01",
            "airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "She mentioned that the disappearance\x01",
            "of the Linde was due to it being\x01",
            "hijacked by some sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "I'm concerned for the safety\x01",
            "of the passengers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC4")

    Jump("loc_10B0")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE4")
    OP_A2(0x0)

    ChrTalk(    #15
        0x8,
        (
            "If flights remain canceled much longer,\x01",
            "it could affect the reputation of the\x01",
            "corporation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "There's never been an accident\x01",
            "and nothing like this has ever\x01",
            "happened before either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I certainly hope we'll be able to properly\x01",
            "explain what happened later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C91")

    label("loc_BE4")


    ChrTalk(    #18
        0x8,
        (
            "If flights remain canceled much longer,\x01",
            "it could affect the reputation of the\x01",
            "corporation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "I certainly hope we'll be able to properly\x01",
            "explain what happened later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C91")

    Jump("loc_10B0")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAA")
    OP_A2(0x0)

    ChrTalk(    #20
        0x8,
        (
            "It seems that the corporation still\x01",
            "hasn't received any word from the\x01",
            "army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "And the transportation of goods\x01",
            "related to the market has pretty\x01",
            "much become stagnant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "We're receiving all kinds of complaints\x01",
            "from everywhere now because of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5A")

    label("loc_DAA")


    ChrTalk(    #23
        0x8,
        (
            "And the transportation of goods\x01",
            "related to the market has pretty\x01",
            "much become stagnant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "We're receiving all kinds of complaints\x01",
            "from everywhere now because of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5A")

    Jump("loc_10B0")

    label("loc_E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_A2(0x0)

    ChrTalk(    #25
        0x8,
        (
            "Presently, all airliner flights\x01",
            "have been postponed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "I'm also sorry to inform you that\x01",
            "we have no idea when they will\x01",
            "resume, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_F02")


    ChrTalk(    #27
        0x8,
        (
            "Even if I tried to explain the circumstances\x01",
            "to customers, I still don't know the cause\x01",
            "of the missing airliner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "I wonder if the Royal Army is really out\x01",
            "in full force searching for the Linde.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCF")

    Jump("loc_10B0")

    label("loc_FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #29
        0x8,
        (
            "Airliner flights have been canceled,\x01",
            "and there's been no indication as to\x01",
            "when they'll resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "I feel extremely bad for all the customers\x01",
            "we have waiting here, to say nothing of\x01",
            "the other landing ports...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B0")

    TalkEnd(0x8)
    Return()

    # Function_4_5CD end

    def Function_5_10B4(): pass

    label("Function_5_10B4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AB")
    OP_A2(0x1)

    ChrTalk(    #31
        0xFE,
        (
            "After an incident like this one, it\x01",
            "makes me a lot more conscious of the\x01",
            "maintenance work I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "The Orbalship Corporation is going to have\x01",
            "to work hard to win back its customers'\x01",
            "trust now that this has happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1210")

    label("loc_11AB")


    ChrTalk(    #33
        0xFE,
        (
            "After an incident like this one, it\x01",
            "makes me a lot more conscious of the\x01",
            "maintenance work I do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1210")

    Jump("loc_1953")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_13BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1317")
    OP_A2(0x1)

    ChrTalk(    #34
        0xFE,
        (
            "It seems that even though they\x01",
            "found the Linde, it's still unable\x01",
            "to return to the skies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "But considering that the captain,\x01",
            "crew and passengers haven't been\x01",
            "found, it's no wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "The whole thing has made me feel\x01",
            "on edge...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BB")

    label("loc_1317")


    ChrTalk(    #37
        0xFE,
        (
            "It seems that the Linde is still\x01",
            "unable to return to the skies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "But considering that the captain,\x01",
            "crew and passengers haven't been\x01",
            "found, it's no wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BB")

    Jump("loc_1953")

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_1483")

    ChrTalk(    #39
        0xFE,
        (
            "Since the Royal Army's patrol ships have\x01",
            "received top priority, we're behind on\x01",
            "maintenance with the Cecilia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "This is just going to delay the departure\x01",
            "for airliner passengers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A2")
    OP_A2(0x1)

    ChrTalk(    #41
        0xFE,
        (
            "The Cecilia, which had been standing\x01",
            "by in Ruan, has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "And what's more, it appears that the\x01",
            "patrol ships from Leiston Fortress\x01",
            "have come, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I'd like to say that this is the most\x01",
            "excited I've been in a while, but \x01",
            "I'm feeling a little rusty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15A2")


    ChrTalk(    #44
        0xFE,
        (
            "The Cecilia, which had been standing\x01",
            "by in Ruan, has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "And what's more, it appears that the\x01",
            "patrol ships from Leiston Fortress\x01",
            "have come, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")

    Jump("loc_1953")

    label("loc_1645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1732")

    ChrTalk(    #46
        0xFE,
        (
            "I don't think there'd be any harm even if\x01",
            "the counter-clockwise looping Cecilia\x01",
            "were the only airliner making flights...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "But the fact that all flights have\x01",
            "been grounded means that this\x01",
            "must be a really big incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1791")

    ChrTalk(    #48
        0xFE,
        (
            "I guess we'll just have to\x01",
            "deal with it then, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Waiting like this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_190E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")
    OP_A2(0x1)

    ChrTalk(    #50
        0xFE,
        (
            "The fact that we're all on standby must\x01",
            "mean that either the company doesn't\x01",
            "fully grasp the situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Or there's already an airliner on\x01",
            "the way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I think the fact that nobody's been told\x01",
            "much means that we're all in the dark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190B")

    label("loc_189C")


    ChrTalk(    #53
        0xFE,
        (
            "And considering that there's been no\x01",
            "contact, maybe even the company\x01",
            "doesn't know what's going on either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190B")

    Jump("loc_1953")

    label("loc_190E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(    #54
        0xFE,
        "I wonder where the airliner is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "What's going on...?\x02",
    )

    CloseMessageWindow()

    label("loc_1953")

    TalkEnd(0x9)
    Return()

    # Function_5_10B4 end

    def Function_6_1957(): pass

    label("Function_6_1957")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_19C8")

    ChrTalk(    #56
        0xFE,
        (
            "International flights bound for\x01",
            "the Empire are still on hold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I hope they'll resume soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B05")
    OP_A2(0x2)

    ChrTalk(    #58
        0xFE,
        (
            "Though none have arrived just yet, this\x01",
            "is a stop for imperial merchant ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "They mainly come with goods\x01",
            "to be sold at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "And for that reason, there are two\x01",
            "runways at the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "About the only other place with\x01",
            "two runways is the Royal City in\x01",
            "Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF6")

    label("loc_1B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2E")
    OP_A2(0x3)

    ChrTalk(    #62
        0xFE,
        (
            "Having two runways alone makes this\x01",
            "landing port twice as busy as others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "But there's something about this\x01",
            "job that makes seeing an airliner\x01",
            "take off safely, extremely fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "This job can get really stressful\x01",
            "at times, but somehow I feel\x01",
            "like I'm cut out for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF6")

    label("loc_1C2E")


    ChrTalk(    #65
        0xFE,
        (
            "There's something about this job that\x01",
            "makes seeing an airliner take off\x01",
            "safely, extremely fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "This job can get really stressful\x01",
            "at times, but somehow I feel\x01",
            "like I'm cut out for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF6")

    Jump("loc_2519")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_1DDC")

    ChrTalk(    #67
        0xFE,
        (
            "The Royal Army patrol ships\x01",
            "just took off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "There was a young officer on board\x01",
            "that seemed pretty high up there\x01",
            "rank-wise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "All right, next I'll need to help\x01",
            "the boss with the maintenance of\x01",
            "the Cecilia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_1DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF0")
    OP_A2(0x2)

    ChrTalk(    #70
        0xFE,
        (
            "I'd better take care of the basic inspections\x01",
            "for the patrol ships while the boss is\x01",
            "looking over the Cecilia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "He's going to blow his top again if\x01",
            "I don't hurry and get my work done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Even if I'm busy or not, I'm\x01",
            "always getting yelled at.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F66")

    label("loc_1EF0")


    ChrTalk(    #73
        0xFE,
        (
            "I'd better take care of the basic inspections\x01",
            "for the patrol ships while the boss is\x01",
            "looking over the Cecilia...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F66")

    Jump("loc_2519")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_20A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2061")
    OP_A2(0x2)

    ChrTalk(    #74
        0xFE,
        (
            "Even though there's not really much to\x01",
            "inspect, I'm going to get yelled at if I\x01",
            "look like I have nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I've got to do something to keep\x01",
            "busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "It's really hard to look busy\x01",
            "when I've got nothing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_2061")


    ChrTalk(    #77
        0xFE,
        (
            "It's really hard to look busy\x01",
            "when I've got nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    Jump("loc_2519")

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_213D")

    ChrTalk(    #78
        0xFE,
        (
            "My boss, Lakely, appears to be\x01",
            "really irritated over something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "He's always got a stern look on his\x01",
            "face but even more so right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_247C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2418")
    OP_A2(0x2)
    ClearMapFlags(0x1)

    ChrTalk(    #80
        0xFE,
        (
            "My boss, Lakely, worked as an airship\x01",
            "mechanic even before there were such\x01",
            "things as airliners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "In other words, he's like my senior\x01",
            "in the field of maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "And for that reason alone, he's stricter\x01",
            "than anyone could imagine, and I get\x01",
            "yelled at every day...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 0)

    ChrTalk(    #83
        0x9,
        "Norm!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D8")

    def lambda_22C4():
        OP_6C(135000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C4)
    OP_69(0x9, 0x1388)
    Jump("loc_230E")

    label("loc_22D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2307")

    def lambda_22F3():
        OP_6C(225000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22F3)
    OP_69(0x9, 0x1388)
    Jump("loc_230E")

    label("loc_2307")

    OP_69(0x9, 0xBB8)

    label("loc_230E")


    ChrTalk(    #84
        0x9,
        (
            "Didn't I tell you that, 'Idle hands\x01",
            "are the devil's work?!' Now find\x01",
            "something to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "If you've got the time to talk, then\x01",
            "how about putting some of these\x01",
            "tools back where they belong?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 0)
    OP_69(0x0, 0xBB8)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #86
        0xFE,
        "Y-Yes, boss.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 0)
    SetMapFlags(0x1)
    Jump("loc_2479")

    label("loc_2418")


    ChrTalk(    #87
        0xFE,
        "I-I'm sorry to take off like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "But any more talking and his\x01",
            "head's gonna blow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2479")

    Jump("loc_2519")

    label("loc_247C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2519")

    ChrTalk(    #89
        0xFE,
        (
            "We mechanics have been standing\x01",
            "by here the whole time as per\x01",
            "the company's orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I wonder how long we'll need\x01",
            "to keep waiting like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    TalkEnd(0xA)
    Return()

    # Function_6_1957 end

    def Function_7_251D(): pass

    label("Function_7_251D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_25A7")

    ChrTalk(    #91
        0xFE,
        (
            "I have finally been able to take the\x01",
            "photo of the Linde I've been after!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Hee hee... Now, to get it developed\x01",
            "ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBB")

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B8")
    OP_A2(0x4)

    ChrTalk(    #93
        0xFE,
        (
            "Now I'm just waiting on the Linde to\x01",
            "come back...but it's taking forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Actually though, what I really want\x01",
            "is to get a shot of the Arseille,\x01",
            "which belongs to the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Rumor has it that its state-of-the-art\x01",
            "design is awesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2776")

    label("loc_26B8")


    ChrTalk(    #96
        0xFE,
        (
            "Now I'm just waiting for the Linde to\x01",
            "come back...but it's taking forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Actually though, what I really want\x01",
            "is to get a shot of the Arseille,\x01",
            "which belongs to the royal family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2776")

    Jump("loc_2FBB")

    label("loc_2779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_28B5")

    ChrTalk(    #98
        0xFE,
        (
            "Coincidentally, I got a look at one of the\x01",
            "technologically advanced patrol ships\x01",
            "the Royal Army is sporting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Not to mention, I got a really good shot\x01",
            "of it too, which was much more than\x01",
            "I would have ever expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I picked the right day to stake out\x01",
            "the landing port, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBB")

    label("loc_28B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DA")
    OP_A2(0x4)

    ChrTalk(    #101
        0xFE,
        "Th-That airship is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Isn't it one of those patrol ships\x01",
            "which belong to the Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Speaking of army patrol ships, they were\x01",
            "used in the war 10 years ago and are\x01",
            "famous for achieving great military results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Airships are just awesome, aren't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_29DA")


    ChrTalk(    #105
        0xFE,
        (
            "Speaking of army patrol ships, they were\x01",
            "used in the war 10 years ago and are\x01",
            "famous for achieving great military results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Airships are just awesome, aren't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A87")

    Jump("loc_2FBB")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEE")
    OP_A2(0x4)

    ChrTalk(    #107
        0xFE,
        (
            "At present, there are two airliners\x01",
            "which provide domestic flights\x01",
            "for passengers in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "There's the clockwise looping Linde and\x01",
            "the counter-clockwise looping Cecilia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Both were put into service in the same\x01",
            "year, but their coloring is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "And if I remember right, the engine\x01",
            "model in the Linde is older.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA4")

    label("loc_2BEE")


    ChrTalk(    #111
        0xFE,
        (
            "At present, there are two airliners\x01",
            "which provide domestic flights\x01",
            "for passengers in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "There's the clockwise looping Linde and\x01",
            "the counter-clockwise looping Cecilia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA4")

    Jump("loc_2FBB")

    label("loc_2CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8C")
    OP_A2(0x4)

    ChrTalk(    #113
        0xFE,
        (
            "We get freighters arriving from the\x01",
            "Empire about once a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "They're mainly used to carry\x01",
            "goods to Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Also, their intimidating design \x01",
            "is typical of what I'd expect\x01",
            "from the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2D8C")


    ChrTalk(    #116
        0xFE,
        (
            "I hope these military restrictions\x01",
            "will get retracted soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCD")

    Jump("loc_2FBB")

    label("loc_2DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB5")
    OP_A2(0x4)

    ChrTalk(    #117
        0xFE,
        (
            "The Bose International Landing\x01",
            "Port gets a lot of traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Which is kind of why I came here\x01",
            "expecting to get some photos\x01",
            "with this orbal camera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "But why isn't there a single ship\x01",
            "coming in?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F44")

    label("loc_2EB5")


    ChrTalk(    #120
        0xFE,
        (
            "I came here expecting to get some\x01",
            "photos of various airships with\x01",
            "this orbal camera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "But why isn't there a single ship\x01",
            "coming in?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F44")

    Jump("loc_2FBB")

    label("loc_2F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2FBB")

    ChrTalk(    #122
        0xFE,
        (
            "Hee hee. This is the perfect place\x01",
            "for taking photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Come on, come on, my fair-winged\x01",
            "airships...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBB")

    TalkEnd(0xB)
    Return()

    # Function_7_251D end

    def Function_8_2FBF(): pass

    label("Function_8_2FBF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_347B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3256")
    OP_28(0x10, 0x1, 0x2000)

    ChrTalk(    #124
        0xFE,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I don't mean to put you out like this,\x01",
            "but I canceled my escort request\x01",
            "through the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "With flights resuming, it looks like\x01",
            "I'll be able to make it to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#004FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        (
            "#013FNo problem, I'm just sorry we\x01",
            "had to bail on you like that...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #129
        0xFE,
        (
            "There's no need to apologize.\x01",
            "We all get busy at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "You guys are investigating some\x01",
            "burglaries in the south block at\x01",
            "the moment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "It seems like you bracers\x01",
            "never get a break.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #132
        0xFE,
        (
            "But anyway, good luck and bring\x01",
            "those sky bandits to justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#006FDon't you worry, we will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_33B4")

    label("loc_3256")


    ChrTalk(    #134
        0xFE,
        (
            "I don't mean to put you out like\x01",
            "this, but I canceled my escort\x01",
            "request through the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "With flights resuming, it looks like\x01",
            "I'll be able to make it to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Man, it looks like I'll finally\x01",
            "be able to get back to some of\x01",
            "my business deals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "However, since I'm this late, who\x01",
            "knows? They could all be down\x01",
            "the drain by now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B4")

    Jump("loc_3478")

    label("loc_33B7")


    ChrTalk(    #138
        0xFE,
        (
            "I've been waiting forever, but it looks\x01",
            "like I can finally head to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Unfortunately, some of my business\x01",
            "deals may be shot because of\x01",
            "being this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "Man, what to do now...?\x02",
    )

    CloseMessageWindow()

    label("loc_3478")

    Jump("loc_37AA")

    label("loc_347B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3506")

    ChrTalk(    #141
        0xFE,
        (
            "I can't believe that they won't\x01",
            "give us a reason or cause for\x01",
            "the canceled flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Don't you think that's a bit much?\x02",
    )

    CloseMessageWindow()
    Jump("loc_37AA")

    label("loc_3506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3589")

    ChrTalk(    #143
        0xFE,
        (
            "They even said they have no idea\x01",
            "when flights will resume either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I guess all I can do is sit here\x01",
            "and wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AA")

    label("loc_3589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369C")
    OP_A2(0x5)

    ChrTalk(    #145
        0xFE,
        "What is this world coming to...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I'm trying to head to Ruan, and then\x01",
            "all of a sudden I'm told that flights\x01",
            "have been canceled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Despite this being out of my control,\x01",
            "arriving late for a business deal is\x01",
            "embarrassing for a Bose merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_370E")

    label("loc_369C")


    ChrTalk(    #148
        0xFE,
        (
            "Despite this being out of my control,\x01",
            "arriving late for a business deal is\x01",
            "embarrassing for a Bose merchant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370E")

    Jump("loc_37AA")

    label("loc_3711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_37AA")

    ChrTalk(    #149
        0xFE,
        (
            "Huh? I came here thinking I could\x01",
            "catch a flight on an airliner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "But it doesn't seem like anybody's\x01",
            "getting ready for one to come in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AA")

    TalkEnd(0xC)
    Return()

    # Function_8_2FBF end

    def Function_9_37AE(): pass

    label("Function_9_37AE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D3")
    OP_A2(0x6)

    ChrTalk(    #151
        0xFE,
        (
            "Well, it looks like the sky bandits have\x01",
            "been arrested, and the missing crew and\x01",
            "passengers are back safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "And according to the receptionist,\x01",
            "flights on the Cecilia will resume\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I've been waiting to get a flight\x01",
            "for I don't know how long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_38D3")


    ChrTalk(    #154
        0xFE,
        (
            "Well, it looks like the sky bandits have\x01",
            "been arrested, and the missing crew and\x01",
            "passengers are back safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "And according to the receptionist,\x01",
            "flights on the Cecilia will resume\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399E")

    Jump("loc_3DA5")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3A5A")

    ChrTalk(    #156
        0xFE,
        (
            "I hear that the Linde is\x01",
            "still out of commission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Though it may be a big detour, I wonder\x01",
            "if taking the Cecilia to the Royal City\x01",
            "is the fastest way to get there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3B1C")

    ChrTalk(    #158
        0xFE,
        (
            "It seems like the airliner\x01",
            "landed in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "And we've got the Royal Army's\x01",
            "patrol ships here in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "I wonder if they're here to investigate\x01",
            "the string of burglaries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3BAA")

    ChrTalk(    #161
        0xFE,
        (
            "To tell you the truth, I'm getting tired\x01",
            "of waiting for flights to resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Maybe it would be best if\x01",
            "I tried again later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3C4A")

    ChrTalk(    #163
        0xFE,
        (
            "It appears that nobody here at the\x01",
            "landing port really knows what's\x01",
            "going on either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I wonder if the airliner had some\x01",
            "sort of an accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3D27")

    ChrTalk(    #165
        0xFE,
        (
            "I guess I won't be able to travel\x01",
            "by airliner for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "It's not that I'm in a hurry to\x01",
            "be anywhere, so I'm not too\x01",
            "stressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "But I'd at least like to know\x01",
            "when flights will resume...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3DA5")

    ChrTalk(    #168
        0xFE,
        (
            "I had planned to take a\x01",
            "trip to the Royal City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "But the airliner I was supposed\x01",
            "to be on hasn't showed up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA5")

    TalkEnd(0xD)
    Return()

    # Function_9_37AE end

    def Function_10_3DA9(): pass

    label("Function_10_3DA9")

    EventBegin(0x0)
    OP_6D(26480, 1500, 26090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(45000, 0)
    OP_6E(534, 0)
    SetChrPos(0x104, 49846, 1500, 40813, 0)
    SetChrPos(0x103, 48769, 1500, 40913, 0)
    SetChrPos(0x101, 49846, 1500, 43000, 180)
    SetChrPos(0x102, 48769, 1500, 43000, 180)
    SetChrPos(0x9, 51290, 1500, 48590, 90)
    OP_72(0x7, 0x4)
    OP_71(0x7, 0x2)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x2)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x1)
    OP_22(0x75, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_6D(49700, 1500, 42500, 5000)
    OP_0D()
    Fade(1000)
    OP_6B(1370, 0)
    OP_0D()

    ChrTalk(    #170
        0x103,
        (
            "#022FWell, take care. I'm going to\x01",
            "head back to Rolent now...\x02\x03",

            "#025FThat said, I'm still a little worried\x01",
            "about you two. Are you sure you\x01",
            "don't want me to come along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#506FGive it a rest, Schera.\x01",
            "We'll be fine.\x02\x03",

            "#006FThe whole reason we're going on this trip\x01",
            "is to become senior bracers. It wouldn't\x01",
            "be training anymore if you came with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#010F#3PAnd if you didn't go back, the\x01",
            "Rolent branch would have a\x01",
            "hard time managing things.\x02\x03",

            "Don't worry about us. We'll figure\x01",
            "out a way to get things done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x103,
        (
            "#025FWell, if you insist...\x02\x03",

            "#020FIt's pretty rare for someone your\x01",
            "age to be aiming for senior bracer\x01",
            "status, so don't overdo it.\x02\x03",

            "And if you run into any trouble,\x01",
            "contact the Rolent branch, you\x01",
            "got it?\x02\x03",

            "I'll come running no matter\x01",
            "where you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#008FSure...thanks, Schera.\x02\x03",

            "#506FAnd the same goes for you.\x01",
            "Don't get yourself too liquored up.\x02\x03",

            "That's the only thing I'm worried\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x103,
        (
            "#520FHa ha ha...all right, all right.\x01",
            "I'll watch the number of drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x104,
        (
            "#035FHa! Never fear, dear children.\x02\x03",

            "You can count on me to protect\x01",
            "fair Schera!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0x101,
        (
            "#509F...And why are you headed\x01",
            "to Rolent?\x02\x03",

            "Not to mention with Schera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x104,
        (
            "#030FThat's because I've tasted all\x01",
            "there is to taste of the local\x01",
            "dishes here in Bose.\x02\x03",

            "And I thought it was about time\x01",
            "I turned my attentions toward\x01",
            "another region.\x02\x03",

            "#031FAs for Rolent's cuisine, I've heard the\x01",
            "produce is just to die for, so that's\x01",
            "what I'm looking forward to next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x103,
        (
            "#025FThat's pretty much it. He says he wants me to\x01",
            "introduce him to a nice restaurant and some\x01",
            "'lovely vegetables', or some such nonsense.\x02\x03",

            "#027FSince he's so persistent, I only agreed\x01",
            "to him coming along under the condition\x01",
            "that he go drinking with me at the bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#007F...We'll never see him alive\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x102,
        (
            "#014F#3POlivier...I really hope you understand\x01",
            "what you've promised her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x104,
        (
            "#030FHa, I could die for the likes of fine women\x01",
            "and food.\x02\x03",

            "#034FPart of me longs to be by your side as you\x01",
            "continue your journey, Joshua...\x02\x03",

            "But after many agonizing hours of\x01",
            "consideration, I've decided to accompany fair\x01",
            "Scherazard instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#017F#3PI think I'll be better off with you a safe\x01",
            "distance away from me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#007FWell, have fun, but I'm warning\x01",
            "you... Don't you dare make any\x01",
            "trouble in Rolent, you hear me?\x02\x03",

            "#006FAnd here's another piece of advice:\x01",
            "When Schera's at the bar, watch out.\x01",
            "That's when the gloves come off.\x02\x03",

            "I'm seriously not joking when\x01",
            "I say you should beware.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x103,
        (
            "#022FHow dare you speak about your mentor\x01",
            "like that, Estelle! And besides,\x01",
            "Aina's coming along too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#509FYeah, and she's even worse\x01",
            "than you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x104,
        (
            "#033FThe gloves come off, huh?\x02\x03",

            "Is that...per chance...what you\x01",
            "and Estelle were talking about\x01",
            "before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x102,
        (
            "#013F#3PYes. Estelle said it best though.\x01",
            "It was nice knowing you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x104,
        "#033FYes, it was a pleasure...\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x104)

    ChrTalk(    #190
        0x104,
        "#036F#3SEh?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_4A14():
        OP_6B(1500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A14)

    def lambda_4A24():
        OP_6D(51410, 1600, 40400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A24)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #191
        (
            "\x07\x05The Rolent-bound airliner will be\x01",
            "departing shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #192
        (
            "\x07\x05All passengers, please board the\x01",
            "airship now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #193
        0x103,
        (
            "#023FWell, Olie-boy, it looks like it's\x01",
            "time for us to leave.\x02\x03",

            "#021FCome on, now. We'd better hurry\x01",
            "and get on.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xBF92, 0x5DC, 0x9D90, 0xBB8, 0x0)

    ChrTalk(    #194
        0x104,
        (
            "#036FSch-Schera, wait!\x01",
            "Can't we talk this over?\x02\x03",

            "I'd really appreciate it if I had\x01",
            "just a little more time to think\x01",
            "things through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x103,
        (
            "#021FSurely you're not getting cold\x01",
            "feet already?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #196
        0x103,
        (
            "#024F#4SIf you consider yourself a man,\x01",
            "then quit acting like a ninny!\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #197
        0x104,
        "#036FEeek!\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4CBE():

        label("loc_4CBE")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_4CBE")

    QueueWorkItem2(0x101, 2, lambda_4CBE)

    def lambda_4CCF():

        label("loc_4CCF")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_4CCF")

    QueueWorkItem2(0x102, 2, lambda_4CCF)

    def lambda_4CE0():
        OP_8E(0x101, 0xC2B6, 0x5DC, 0x9F6D, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CE0)

    def lambda_4CFB():
        OP_8E(0x102, 0xBE81, 0x5DC, 0x9FD1, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4CFB)
    OP_43(0x104, 0x1, 0x0, 0xC)
    OP_43(0x103, 0x1, 0x0, 0xB)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #198
        0x101,
        (
            "#001FSee you later, Schera!\x02\x03",

            "Give our regards to everyone\x01",
            "in Rolent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#019FHave a wonderful trip, you two!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(1000)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x104, 0x1)
    OP_A1(0xE, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0xE, 62250, -5650, 41990, 0)
    SetChrFlags(0xE, 0x4)
    OP_A1(0xF, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0xF, 62250, -5500, 41990, 0)
    SetChrFlags(0xF, 0x4)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_70(0x9, 0x64)
    OP_70(0xA, 0x64)
    OP_73(0x9)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x3C)
    OP_73(0x7)
    Fade(2000)
    OP_6D(60000, -1550, 51540, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(550, 0)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    Sleep(2000)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x7, 61)
    OP_70(0x7, 0xA0)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 161)
    OP_70(0x7, 0x104)

    def lambda_4EAF():
        OP_6D(60000, -1550, 51540, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EAF)

    def lambda_4EC7():
        OP_67(0, 11230, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EC7)

    def lambda_4EDF():
        OP_6B(2260, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4EDF)

    def lambda_4EEF():
        OP_6C(204000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EEF)

    def lambda_4EFF():
        OP_6E(801, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4EFF)
    OP_91(0xE, 0x0, 0x1F4, 0x0, 0x12C, 0x0)
    OP_91(0xE, 0x0, 0x3E8, 0x0, 0x258, 0x0)
    Sleep(2000)

    def lambda_4F3C():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F3C)
    OP_94(0x1, 0xE, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_4F61():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F61)
    OP_94(0x1, 0xE, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_4F86():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F86)
    OP_94(0x1, 0xE, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_4FAB():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FAB)
    OP_94(0x1, 0xE, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_4FD0():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FD0)
    OP_94(0x1, 0xE, 0x0, 0x708, 0x1388, 0x0)

    def lambda_4FF5():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FF5)
    OP_94(0x1, 0xE, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_501A():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_501A)
    OP_20(0xBB8)
    FadeToDark(4000, 0, -1)
    OP_94(0x1, 0xE, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_504E():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_504E)

    def lambda_5064():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5064)
    OP_0D()
    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x75, 0x14)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x75, 0xA)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x75)
    OP_23(0x77)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40042, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x12, 0x0)
    OP_A2(0x391)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5170")
    ShowSaveMenu()

    label("loc_5170")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x392)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3DA9 end

    def Function_11_51CA(): pass

    label("Function_11_51CA")

    OP_8E(0xFE, 0xC011, 0x5DC, 0x9537, 0xBB8, 0x0)
    OP_8E(0xFE, 0xE120, 0x5DC, 0x9537, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xE7C2, 0x5DC, 0x98DA, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_11_51CA end

    def Function_12_5213(): pass

    label("Function_12_5213")

    OP_8C(0xFE, 0, 0)
    OP_8F(0xFE, 0xC011, 0x5DC, 0x9537, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xE120, 0x5DC, 0x9537, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0xE5F6, 0x5DC, 0x9538, 0xBB8, 0x0)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_12_5213 end

    def Function_13_526F(): pass

    label("Function_13_526F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #200
        (
            "\x07\x05Bose Landing Port\x01",
            "⇒　Rolent City\x01",
            "⇒　Ruan City\x01",
            "⇒ Erebonian Empire\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_526F end

    def Function_14_52E5(): pass

    label("Function_14_52E5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #201
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_52E5 end

    def Function_15_5364(): pass

    label("Function_15_5364")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #202
        (
            "\x07\x05　　　     Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "      　   《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_5364 end

    SaveToFile()

Try(main)
