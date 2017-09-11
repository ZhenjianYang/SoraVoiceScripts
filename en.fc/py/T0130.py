from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0130   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0130   ._SN',
            'ED6_DT01/T0130_1 ._SN',
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
        'Father Divine',                        # 9
        'Sister May',                           # 10
        'Seagaro',                              # 11
        'Edel',                                 # 12
        'Mylene',                               # 13
        'Aryll',                                # 14
        'Aryll',                                # 15
        'Girl in Uniform',                      # 16
        'Paddington',                           # 17
        'Radford',                              # 18
        'Mayor Klaus',                          # 19
        'Lita',                                 # 20
    )

    DeclEntryPoint(
        Unknown_00              = 59000,
        Unknown_04              = 0,
        Unknown_08              = 40000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 3,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 59000,
        Unknown_04              = 0,
        Unknown_08              = 40000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01043 ._CH',             # 02
        'ED6_DT07/CH01213 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01700 ._CH',             # 05
        'ED6_DT07/CH01700 ._CH',             # 06
        'ED6_DT07/CH02330 ._CH',             # 07
        'ED6_DT07/CH01250 ._CH',             # 08
        'ED6_DT07/CH01003 ._CH',             # 09
        'ED6_DT07/CH02350 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
        'ED6_DT07/CH00014 ._CH',             # 0C
        'ED6_DT07/CH00015 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01043P._CP',             # 02
        'ED6_DT07/CH01213P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01700P._CP',             # 05
        'ED6_DT07/CH01700P._CP',             # 06
        'ED6_DT07/CH02330P._CP',             # 07
        'ED6_DT07/CH01250P._CP',             # 08
        'ED6_DT07/CH01003P._CP',             # 09
        'ED6_DT07/CH02350P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
        'ED6_DT07/CH00014P._CP',             # 0C
        'ED6_DT07/CH00015P._CP',             # 0D
    )

    DeclNpc(
        X                   = 58800,
        Z                   = 1000,
        Y                   = 52200,
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
        X                   = -16832,
        Z                   = 0,
        Y                   = 42888,
        Direction           = 270,
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
        X                   = 56090,
        Z                   = 100,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55330,
        Z                   = 100,
        Y                   = 45940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 58997,
        Z                   = 1000,
        Y                   = 50050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58960,
        Z                   = 1000,
        Y                   = 49950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 59170,
        Z                   = 1000,
        Y                   = 50210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 61810,
        Z                   = 0,
        Y                   = 45970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 58997,
        Z                   = 1000,
        Y                   = 50050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 59070,
        Z                   = 1000,
        Y                   = 50010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_480",          # 01, 1
        "Function_2_4CA",          # 02, 2
        "Function_3_4E0",          # 03, 3
        "Function_4_4E5",          # 04, 4
        "Function_5_1AF1",         # 05, 5
        "Function_6_2327",         # 06, 6
        "Function_7_2493",         # 07, 7
        "Function_8_25F0",         # 08, 8
        "Function_9_2711",         # 09, 9
        "Function_10_2754",        # 0A, 10
        "Function_11_2846",        # 0B, 11
        "Function_12_2A16",        # 0C, 12
        "Function_13_2BC8",        # 0D, 13
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_316")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_424")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_32A")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_424")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_36B")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_368")
    OP_8C(0x8, 270, 0)

    label("loc_368")

    Jump("loc_424")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3AC")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A9")
    OP_8C(0x8, 270, 0)

    label("loc_3A9")

    Jump("loc_424")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3D2")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_3CF")

    Jump("loc_424")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3F5")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_424")

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_413")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    Jump("loc_424")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_424")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    OP_28(0x9, 0x1, 0x10)
    Event(1, 6)

    label("loc_44A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    OP_28(0x9, 0x1, 0x20)
    OP_28(0x9, 0x1, 0x40)
    Event(1, 7)

    label("loc_47F")

    Return()

    # Function_0_302 end

    def Function_1_480(): pass

    label("Function_1_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_498")
    OP_B1("t0130_y")
    Jump("loc_4A1")

    label("loc_498")

    OP_B1("t0130_n")

    label("loc_4A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    OP_1B(0x1, 0x1, 0x9)

    label("loc_4C9")

    Return()

    # Function_1_480 end

    def Function_2_4CA(): pass

    label("Function_2_4CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4CA")

    label("loc_4DF")

    Return()

    # Function_2_4CA end

    def Function_3_4E0(): pass

    label("Function_3_4E0")

    Call(0, 4)
    Return()

    # Function_3_4E0 end

    def Function_4_4E5(): pass

    label("Function_4_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_69C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50F")
    Call(1, 1)
    Jump("loc_699")

    label("loc_50F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_683")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5A4")

    ChrTalk(    #0
        0x8,
        (
            "You have done me a great service\x01",
            "in gathering these medicinal\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Make sure you take care in\x01",
            "your travels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D")

    label("loc_5A4")


    ChrTalk(    #2
        0x8,
        (
            "Please make sure this letter\x01",
            "is delivered to the right hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "The chapel is on the east side\x01",
            "of Bose City, so it should be\x01",
            "fairly easy to locate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I pray that the Goddess will guide\x01",
            "you on your journey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D")

    TalkEnd(0x8)
    Jump("loc_699")

    label("loc_683")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_695")
    Call(1, 2)
    Jump("loc_699")

    label("loc_695")

    Call(1, 0)

    label("loc_699")

    Jump("loc_1AF0")

    label("loc_69C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    TalkBegin(0x8)

    ChrTalk(    #5
        0x8,
        (
            "Mm? Is there something I can\x01",
            "help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Something which appeared to\x01",
            "be an animal ran that way.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1AF0")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    Call(1, 4)
    Jump("loc_86F")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7DD")
    TalkBegin(0x8)

    ChrTalk(    #7
        0x8,
        (
            "Thank you for all your hard\x01",
            "work, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "I pray that the Goddess will\x01",
            "always be with you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_86F")

    label("loc_7DD")

    TalkBegin(0x8)

    ChrTalk(    #9
        0x8,
        (
            "Well there, it appears to me that\x01",
            "your faces seem a bit older and\x01",
            "wiser.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "I am glad to see that you have\x01",
            "matured in body and mind.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_86F")

    Jump("loc_1AF0")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_962")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Call(1, 4)
    Jump("loc_95F")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_91D")
    TalkBegin(0x8)

    ChrTalk(    #11
        0x8,
        (
            "Thank you for all your hard\x01",
            "work, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I pray that the Goddess will\x01",
            "always be with you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_95F")

    label("loc_91D")

    TalkBegin(0x8)

    ChrTalk(    #13
        0x8,
        (
            "It appears that the mayor was\x01",
            "pleased about something.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_95F")

    Jump("loc_1AF0")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_CA3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    Call(1, 4)
    Jump("loc_CA0")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A0D")
    TalkBegin(0x8)

    ChrTalk(    #14
        0x8,
        (
            "Thank you for all your hard\x01",
            "work, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I pray that the Goddess will\x01",
            "always be with you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_CA0")

    label("loc_A0D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE0")
    OP_A2(0x0)

    ChrTalk(    #16
        0x8,
        (
            "I have watched over Rolent for\x01",
            "almost 30 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I stood with the citizens in bewilderment\x01",
            "as we saw our once fair city reduced to\x01",
            "rubble 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "However, when I gaze out on the\x01",
            "rebuilt city, I am awed at the\x01",
            "strength that people possess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Frailty, strength... These two\x01",
            "contrasting things are inseparable\x01",
            "in our paradoxical existences...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "However, for myself, these features\x01",
            "are what make us, as humans, most\x01",
            "beloved.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_C9D")

    label("loc_BE0")


    ChrTalk(    #21
        0x8,
        (
            "Frailty and strength, these two\x01",
            "contrasting things are inseparable\x01",
            "in our paradoxical existences...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "However, for myself, these features\x01",
            "are what make us, as humans, most\x01",
            "beloved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9D")

    TalkEnd(0x8)

    label("loc_CA0")

    Jump("loc_1AF0")

    label("loc_CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCD")
    Call(1, 4)
    Jump("loc_109F")

    label("loc_CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D4E")
    TalkBegin(0x8)

    ChrTalk(    #23
        0x8,
        (
            "Thank you for all your hard\x01",
            "work, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I pray that the Goddess will\x01",
            "always be with you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_109F")

    label("loc_D4E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD6")
    OP_A2(0x2B5)

    ChrTalk(    #25
        0x8,
        (
            "The greater the light, the darker\x01",
            "the shadow becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "When one's soul is touched by a blinding\x01",
            "light, it becomes conscious of the darkness\x01",
            "within, and embraces a contrite spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "Especially, those who are tormented\x01",
            "by the sins of their past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "However, through this ordeal, one can\x01",
            "understand the pain and suffering of others\x01",
            "and reach a greater plane of insight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "What is important for the individual is\x01",
            "preparing for the future and deciding\x01",
            "what one wants to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#007FArgh...just listening to him\x01",
            "makes my brain hurt...\x02\x03",

            "Father Divine's sermons are always\x01",
            "difficult for me to understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109C")

    label("loc_FD6")


    ChrTalk(    #32
        0x8,
        (
            "When one's soul is touched by a blinding\x01",
            "light, it becomes conscious of the darkness\x01",
            "within, and embraces a contrite spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "Especially, those who are tormented\x01",
            "by the sins of their past.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109C")

    TalkEnd(0x8)

    label("loc_109F")

    Jump("loc_1AF0")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1388")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EC")
    OP_A2(0x2B4)

    ChrTalk(    #34
        0x8,
        (
            "Estelle and Joshua. I heard that\x01",
            "you both joined the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "I am sure that aside from your\x01",
            "aspirations and expectations that\x01",
            "there is some tension and anxiety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "Hmm...I sense that Estelle has\x01",
            "a different kind of anxiety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#004FHuh...?\x02\x03",

            "#501FI-I think you must be mistaken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "The absence of a parent would\x01",
            "cause anyone to feel uncertain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "However, we as humans have\x01",
            "the strength to overcome such\x01",
            "adversity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "Think of these trials as a gift from\x01",
            "the Goddess and work hard to\x01",
            "overcome them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#000FI'll try...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1385")

    label("loc_12EC")


    ChrTalk(    #43
        0x8,
        (
            "We as humans have the strength\x01",
            "to overcome such adversity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Think of these trials as a gift from\x01",
            "the Goddess and work hard to\x01",
            "overcome them.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1385")

    Jump("loc_1AF0")

    label("loc_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1537")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C6")
    OP_A2(0x2B3)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #45
        0x8,
        "Oh my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "You appear to be troubled by\x01",
            "something, Estelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#501FHuh? R-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "We as humans grow through these\x01",
            "afflictions. These are a trial\x01",
            "given to us by the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "Aidios, who art on high, please\x01",
            "guide this beleaguered youth.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1534")

    label("loc_14C6")


    ChrTalk(    #50
        0x8,
        (
            "No matter which path you decide\x01",
            "to travel, never forget that each day\x01",
            "is a blessing from the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1534")

    Jump("loc_1AF0")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_17CE")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1710")
    OP_A2(0x2B2)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #51
        0x8,
        (
            "Estelle, you seem to be rather\x01",
            "cheerful today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "Did something wonderful happen\x01",
            "in your life?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        "#001FHeeheehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#018FYes, I guess you could say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "Joyous occasions are\x01",
            "indeed a wonderful thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "But, it is at times when things go\x01",
            "well that we should gird up our loins\x01",
            "for the trials that lie ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Oh, Goddess Aidios of the firmament,\x01",
            "please guide these unseasoned youths.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_17CB")

    label("loc_1710")


    ChrTalk(    #58
        0x8,
        (
            "It is at times when things go well\x01",
            "that we should gird up our loins\x01",
            "for the trials that lie ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "Oh, Goddess Aidios of the firmament,\x01",
            "please guide these unseasoned youths.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_17CB")

    Jump("loc_1AF0")

    label("loc_17CE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A70")
    OP_A2(0x2B1)

    ChrTalk(    #60
        0x8,
        (
            "It has been a while since I saw\x01",
            "the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I'm impressed to see you visiting\x01",
            "the chapel so early in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#000FGood morning, Father Divine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "You were habitually late and played\x01",
            "hooky more than a few times during\x01",
            "your Sunday School days, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "So have you changed your attitude\x01",
            "on life since you graduated?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        "#008FAh ha ha...a bit I guess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "It looks like there is a little time\x01",
            "before morning mass begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "So how about I give you both\x01",
            "a special sermon...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#004FUh...\x02\x03",

            "#506FN-No thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#018F(Why am I getting thrown\x01",
            "into the mix here...?)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1AF0")

    label("loc_1A70")


    ChrTalk(    #71
        0x8,
        (
            "It looks like there is a little time\x01",
            "before morning mass begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "So how about I give you both\x01",
            "a special sermon...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1AF0")

    Return()

    # Function_4_4E5 end

    def Function_5_1AF1(): pass

    label("Function_5_1AF1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA9")
    OP_A2(0x2)

    ChrTalk(    #73
        0xFE,
        (
            "I taught the children about the\x01",
            "Bracer Guild in our last lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Luke was especially attentive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I guess for young boys, bracers\x01",
            "are like heroes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDF")

    label("loc_1BA9")


    ChrTalk(    #76
        0xFE,
        (
            "I guess for young boys, bracers\x01",
            "are like heroes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDF")

    Jump("loc_2323")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(    #77
        0xFE,
        (
            "I could have sworn something\x01",
            "just went up those stairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I wonder if it was just my\x01",
            "imagination...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CF5")

    ChrTalk(    #79
        0xFE,
        (
            "Recently, some of the children\x01",
            "have come to see me on non-\x01",
            "Sunday School days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I'm glad I became a sister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1DB6")

    ChrTalk(    #81
        0xFE,
        (
            "The Sunday School lesson\x01",
            "went better than expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "This is thanks to the advice\x01",
            "of Father Divine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "However, I just don't know what to\x01",
            "do about Luke's naughty behavior.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_1DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E31")

    ChrTalk(    #84
        0xFE,
        (
            "I will be teaching Sunday School\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I hope the children will listen\x01",
            "to what I have to say...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2068")
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2020")
    OP_A2(0x2)

    ChrTalk(    #86
        0xFE,
        "A-Aren't you Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I've heard many things about\x01",
            "you from Father Divine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#004FL-Like what kinds of things...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Heehee...\x01",
            "Oh, just stories about when you\x01",
            "were in Sunday School and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#010FIt seems you were an expert at sleeping\x01",
            "in class, being late, skipping school,\x01",
            "and generally just causing trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "But, despite all these things, it looks\x01",
            "like Father Divine was quite fond of\x01",
            "you as a student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#008FY-You really think so...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2065")

    label("loc_2020")


    ChrTalk(    #93
        0xFE,
        (
            "It looks like Father Divine was\x01",
            "quite fond of you as a student.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2065")

    Jump("loc_2323")

    label("loc_2068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(    #94
        0x9,
        "Oh, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "I give thanks for the peace and\x01",
            "tranquility thou hast bestowed\x01",
            "upon us this day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_22CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221B")
    OP_A2(0x2)

    ChrTalk(    #96
        0x9,
        (
            "I'm a newly assigned sister\x01",
            "to this chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "I was recently transferred from\x01",
            "the Royal City to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "This place is surrounded by greenery,\x01",
            "and everyone in town is so kind.\x01",
            "I think I'm going to enjoy it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "Father Divine is a bit strict, but he\x01",
            "is someone I can respect a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CA")

    label("loc_221B")


    ChrTalk(    #100
        0x9,
        (
            "I was recently transferred from\x01",
            "the Royal City to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "This place is surrounded by greenery,\x01",
            "and everyone in town is so kind.\x01",
            "I think I'm going to enjoy it here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CA")

    Jump("loc_2323")

    label("loc_22CD")


    ChrTalk(    #102
        0x9,
        "It's almost time for mass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "Mylene is already here,\x01",
            "so I'd best hurry along!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2323")

    TalkEnd(0x9)
    Return()

    # Function_5_1AF1 end

    def Function_6_2327(): pass

    label("Function_6_2327")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BF")
    OP_A2(0x3)

    ChrTalk(    #104
        0xA,
        (
            "We're on a pilgrimage to see\x01",
            "chapels from each region of\x01",
            "this beautiful kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        "The airliner just arrived in Rolent.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2446")

    label("loc_23BF")


    ChrTalk(    #106
        0xA,
        (
            "Thanks to these airliners, traveling\x01",
            "has never been so easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "I'm just glad I've been able to get\x01",
            "away from work for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2446")

    Jump("loc_248F")

    label("loc_2449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2471")

    ChrTalk(    #108
        0xA,
        "本当はまだ配置なしです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_248F")

    label("loc_2471")


    ChrTalk(    #109
        0xA,
        "本当はまだ配置なしです。\x02",
    )

    CloseMessageWindow()

    label("loc_248F")

    TalkEnd(0xA)
    Return()

    # Function_6_2327 end

    def Function_7_2493(): pass

    label("Function_7_2493")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_25A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2552")
    OP_A2(0x4)

    ChrTalk(    #110
        0xB,
        (
            "Yes, yes, yes!\x01",
            "I came along with my husband fully\x01",
            "intending to shop till I drop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "The air in Rolent is so fresh, and the\x01",
            "city itself is peaceful and calming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A3")

    label("loc_2552")


    ChrTalk(    #112
        0xB,
        (
            "The air in Rolent is so fresh, and the\x01",
            "city itself is peaceful and calming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A3")

    Jump("loc_25EC")

    label("loc_25A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_25CE")

    ChrTalk(    #113
        0xB,
        "本当はまだ配置なしです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25EC")

    label("loc_25CE")


    ChrTalk(    #114
        0xB,
        "本当はまだ配置なしです。\x02",
    )

    CloseMessageWindow()

    label("loc_25EC")

    TalkEnd(0xB)
    Return()

    # Function_7_2493 end

    def Function_8_25F0(): pass

    label("Function_8_25F0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C0")
    OP_A2(0x5)

    ChrTalk(    #115
        0x101,
        "#000FGood morning, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "My, my, if it isn't Estelle and\x01",
            "Joshua. Good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "Where are you off to this morning?\x01",
            "It must be tough waking up so early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_26C0")


    ChrTalk(    #119
        0xC,
        (
            "Where are you off to this morning?\x01",
            "It must be tough waking up so early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270D")

    TalkEnd(0xC)
    Return()

    # Function_8_25F0 end

    def Function_9_2711(): pass

    label("Function_9_2711")

    TalkBegin(0xF)

    ChrTalk(    #120
        0xF,
        (
            "I see...\x02\x03",

            "I completely agree with your\x01",
            "inspired words.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_9_2711 end

    def Function_10_2754(): pass

    label("Function_10_2754")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CC")
    OP_A2(0x7)

    ChrTalk(    #121
        0xFE,
        (
            "Another day has passed.\x01",
            "There is nothing better than peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "War should never happen again...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2842")

    label("loc_27CC")


    ChrTalk(    #123
        0xFE,
        "War should never happen again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Just thinking about what happened\x01",
            "10 years ago makes my old bones\x01",
            "tremble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2842")

    TalkEnd(0x10)
    Return()

    # Function_10_2754 end

    def Function_11_2846(): pass

    label("Function_11_2846")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C7")

    ChrTalk(    #125
        0xFE,
        "What's with all this talking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "This place is supposed to be\x01",
            "a house of prayer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A12")

    label("loc_28C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2989")
    OP_A2(0x8)

    ChrTalk(    #127
        0xFE,
        (
            "The other day, I snuck out to see my\x01",
            "son-in-law working in the woods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "He appeared to be working hard\x01",
            "in his own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Yet, somehow he seemed to\x01",
            "be lacking something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A12")

    label("loc_2989")


    ChrTalk(    #130
        0xFE,
        (
            "There's just something missing from my son-\x01",
            "in-law's work... It's hard to put my finger\x01",
            "on it, but I just can't approve of him yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A12")

    TalkEnd(0x11)
    Return()

    # Function_11_2846 end

    def Function_12_2A16(): pass

    label("Function_12_2A16")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ACC")

    ChrTalk(    #131
        0xFE,
        (
            "#600FOh, Estelle and Joshua. You did\x01",
            "me a great service in recovering\x01",
            "that septium.\x02\x03",

            "That said, why do you appear\x01",
            "to be in such a rush?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC4")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B77")
    OP_A2(0x9)

    ChrTalk(    #132
        0xFE,
        (
            "#601FOh, Estelle and Joshua. You did\x01",
            "me a great service in recovering\x01",
            "that septium.\x02\x03",

            "I came here today because I had an\x01",
            "appointment with Father Divine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC4")

    label("loc_2B77")


    ChrTalk(    #133
        0xFE,
        (
            "#601FI came here today because I had an\x01",
            "appointment with Father Divine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC4")

    TalkEnd(0x12)
    Return()

    # Function_12_2A16 end

    def Function_13_2BC8(): pass

    label("Function_13_2BC8")

    TalkBegin(0x13)

    ChrTalk(    #134
        0xFE,
        (
            "Please bless the mayor and his\x01",
            "wife so that they may live in\x01",
            "good health...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_13_2BC8 end

    SaveToFile()

Try(main)
