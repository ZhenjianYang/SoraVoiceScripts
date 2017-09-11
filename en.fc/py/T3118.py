from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3118   ._SN',
            'ED6_DT01/T3118_1 ._SN',
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
        'Dr. Miriam',                           # 9
        'Agate',                                # 10
        'Rudi',                                 # 11
        'Antoine',                              # 12
        'Tita',                                 # 13
        'Factory Chief Murdock',                # 14
        'Book',                                 # 15
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH01500 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH02620 ._CH',             # 05
        'ED6_DT06/CH20061 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH01500P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH02620P._CP',             # 05
        'ED6_DT06/CH20061P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x196,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9560,
        Z                   = 800,
        Y                   = -1360,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769479,
        ChipIndex           = 0x7,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -9560,
        TriggerZ            = 0,
        TriggerY            = -1360,
        TriggerRange        = 800,
        ActorX              = -9560,
        ActorZ              = 800,
        ActorY              = -1360,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_471",          # 01, 1
        "Function_2_564",          # 02, 2
        "Function_3_57A",          # 03, 3
        "Function_4_5C8",          # 04, 4
        "Function_5_641",          # 05, 5
        "Function_6_681",          # 06, 6
        "Function_7_9B2",          # 07, 7
        "Function_8_32D5",         # 08, 8
        "Function_9_3326",         # 09, 9
        "Function_10_3BFB",        # 0A, 10
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1FC")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_20A")
    OP_A3(0x3FB)
    Event(1, 4)

    label("loc_20A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_216"),
        (SWITCH_DEFAULT, "loc_22E"),
    )


    label("loc_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_22B")

    Jump("loc_22E")

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_26E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2BA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3440, 0, -6430, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    Jump("loc_455")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_326")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -4680, 0, 6630, 90)
    Jump("loc_455")

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_330")
    Jump("loc_455")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3AC")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35F")
    SetChrPos(0x8, -5680, 0, 6400, 337)
    Jump("loc_393")

    label("loc_35F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_382")
    SetChrPos(0x8, -1160, 0, 6790, 110)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_393")

    label("loc_382")

    SetChrPos(0x8, -1160, 0, 6790, 110)

    label("loc_393")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3E2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_418")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_438")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_455")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)

    label("loc_455")

    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470")
    ClearChrFlags(0xE, 0x80)

    label("loc_470")

    Return()

    # Function_0_1EE end

    def Function_1_471(): pass

    label("Function_1_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_489")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B6")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B6")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE")
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_543")
    SetChrFlags(0xB, 0x80)

    label("loc_543")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_563")
    OP_65(0x0, 0x1)

    label("loc_563")

    Return()

    # Function_1_471 end

    def Function_2_564(): pass

    label("Function_2_564")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_579")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_564")

    label("loc_579")

    Return()

    # Function_2_564 end

    def Function_3_57A(): pass

    label("Function_3_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x1000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A4")

    label("loc_58C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58C")

    label("loc_5A1")

    Jump("loc_5C7")

    label("loc_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C7")
    OP_8D(0xFE, -5120, 8029, -7290, 5400, 1000)
    Jump("loc_5A4")

    label("loc_5C7")

    Return()

    # Function_3_57A end

    def Function_4_5C8(): pass

    label("Function_4_5C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_609")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x38A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F0")
    Call(1, 3)
    Jump("loc_606")

    label("loc_5F0")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #0
        0xFE,
        "Nyayayaa～.\x02",
    )

    CloseMessageWindow()

    label("loc_606")

    Jump("loc_63D")

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_624")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #1
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_63D")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_63D")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #2
        0xFE,
        "Nya-go.\x02",
    )

    CloseMessageWindow()

    label("loc_63D")

    TalkEnd(0xFE)
    Return()

    # Function_4_5C8 end

    def Function_5_641(): pass

    label("Function_5_641")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_65C")

    ChrTalk(    #3
        0x9,
        "#053F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_67D")

    label("loc_65C")


    ChrTalk(    #4
        0x9,
        "#551F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x107,
        "#063FAgate...\x02",
    )

    CloseMessageWindow()

    label("loc_67D")

    TalkEnd(0xFE)
    Return()

    # Function_5_641 end

    def Function_6_681(): pass

    label("Function_6_681")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_9AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6E9")

    ChrTalk(    #6
        0xFE,
        (
            "#060FI'm going to stay here and\x01",
            "watch Agate for a while.\x02\x03",

            "Be careful, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 4)), scpexpr(EXPR_END)), "loc_78B")
    OP_A2(0x2)

    ChrTalk(    #7
        0xFE,
        (
            "#060FYou too, Joshua.\x02\x03",

            "I think Agate's going to be\x01",
            "all right now.\x02\x03",

            "#066FBut still...I think I'll stay\x01",
            "here and watch him.\x02\x03",

            "Be careful, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_78B")

    OP_A2(0x2)
    OP_A2(0x58C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899")

    ChrTalk(    #8
        0xFE,
        "#560FEstelle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#000FHow's Agate doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "#060FHe's asleep.\x01",
            "I think he'll be all right.\x02\x03",

            "How are you guys doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#000FWe're investigating.\x02\x03",

            "Just leave it to us while you\x01",
            "keep an eye on Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "#060FOkay.\x02\x03",

            "Be careful, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_899")


    ChrTalk(    #13
        0xFE,
        "#560FJoshua...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#010FHow is Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "#060FHe's asleep.\x01",
            "I think he'll be all right.\x02\x03",

            "How are you guys doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#010FWe're doing everything we\x01",
            "can to find a good lead.\x02\x03",

            "Don't worry about us, though.\x01",
            "Just keep an eye on Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "#060FOkay.\x02\x03",

            "Be careful, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE")

    TalkEnd(0xFE)
    Return()

    # Function_6_681 end

    def Function_7_9B2(): pass

    label("Function_7_9B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A36")

    ChrTalk(    #18
        0xFE,
        (
            "Surely the army won't let things\x01",
            "stand as they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "We should expect some kind\x01",
            "of retaliatory strike.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFD")

    label("loc_A36")

    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        "Hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I heard about the rescue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "At least you were able to recover\x01",
            "the professor safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Other than that, we can only wait\x01",
            "and hope they stay one step ahead\x01",
            "of the army.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFD")

    Jump("loc_32D1")

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #24
        0xFE,
        "Please be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "And don't overdo things this\x01",
            "time, Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2D")

    label("loc_B58")

    OP_A2(0x58B)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #26
        0xFE,
        "Where is Agate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I told him...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#051FHey, I'm right here, Doc.\x02\x03",

            "I just wanted to get out and\x01",
            "stretch my legs a little.\x02\x03",

            "#053F...And work out. A little.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #29
        0x101,
        (
            "#509FStretch your legs...work out...?\x02\x03",

            "Insane, Agate. You're insane!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I give up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Well, you bracers are supposed\x01",
            "to know your own limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Do what you like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Just...be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x106,
        (
            "#051FI'll do what I can to stay out\x01",
            "of your clinic, Doc. \x02\x03",

            "Thanks for everything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2D")

    Jump("loc_32D1")

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DBC")

    ChrTalk(    #35
        0xFE,
        (
            "He hasn't woken up yet, but it\x01",
            "appears Agate is stable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Tita hasn't left his side. She's\x01",
            "been a tremendous help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA6")

    label("loc_DBC")

    OP_A2(0x0)

    ChrTalk(    #37
        0xFE,
        (
            "Thank you for yesterday. With\x01",
            "your help you've saved him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "He hasn't woken up, but he's\x01",
            "definitely past the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "He's no longer unconscious,\x01",
            "just in a deep sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "It won't be long before he\x01",
            "wakes up, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA6")

    Jump("loc_32D1")

    label("loc_EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(    #41
        0xFE,
        (
            "The Septian Church has been\x01",
            "a repository of traditional\x01",
            "medicine for almost 1000 years. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Father Vixen should know\x01",
            "something about this strange\x01",
            "poison we're dealing with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "There might be some value\x01",
            "in going to the church and\x01",
            "discussing the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D1")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1045")

    ChrTalk(    #44
        0xFE,
        (
            "I'm sorry, but I've already\x01",
            "withdrawn the cigarette\x01",
            "investigation contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Perhaps you can help us\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_1045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133D")
    OP_28(0x2C, 0x1, 0x4000)
    OP_A2(0x4)

    ChrTalk(    #46
        0xFE,
        (
            "As far as I know there aren't\x01",
            "any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "It was quite a harrowing experience,\x01",
            "but at least it seems that no one\x01",
            "was harmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Yes, speaking of that, there\x01",
            "is the matter of that request\x01",
            "regarding the missing cigarettes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I'm sorry, but I've decided to\x01",
            "cancel my investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#004FR-Really...? Why?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #51
        0xFE,
        "You've taken too much time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Without the proof, we can't arrest\x01",
            "or even accuse anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "So I've decided to close\x01",
            "the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#013FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#007FI'm sorry. It's my fault.\x02\x03",

            "I shouldn't have dragged my feet\x01",
            "on the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#010FIf there is anything else we can\x01",
            "help you with, please don't\x01",
            "hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #57
        0xFE,
        (
            "Thank you.\x01",
            "I'll keep you in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13D1")

    ChrTalk(    #58
        0xFE,
        (
            "As far as I know, there aren't\x01",
            "any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It was quite a harrowing experience,\x01",
            "but at least it seems that no one\x01",
            "was harmed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_13D1")

    OP_A2(0x0)

    ChrTalk(    #60
        0xFE,
        "Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "As far as I know, there aren't\x01",
            "any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "It was quite a harrowing experience,\x01",
            "but at least it seems that no one\x01",
            "was harmed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158D")

    ChrTalk(    #63
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #64
        0xFE,
        "Tita, are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "Do you feel ill?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        (
            "#064FNo...\x02\x03",

            "#060FNo, I'm okay.\x02\x03",

            "Just a little light-headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Don't overtax yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I imagine you're exhausted.\x01",
            "Go and get some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        "#060FYes, ma'am.\x02",
    )

    CloseMessageWindow()

    label("loc_158D")

    Jump("loc_32D1")

    label("loc_1590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_195D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1636")

    ChrTalk(    #70
        0xFE,
        (
            "Thank you everyone. I really\x01",
            "appreciate your help in\x01",
            "resolving this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If I need your help in the future,\x01",
            "I'll contact you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D3")

    label("loc_1636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16E9")

    ChrTalk(    #72
        0xFE,
        (
            "I was studying methods of\x01",
            "reducing stress using lab\x01",
            "animals as test subjects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I was conducting very serious\x01",
            "research, despite any appearances\x01",
            "to the contrary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D3")

    label("loc_16E9")

    OP_A2(0x0)

    ChrTalk(    #74
        0xFE,
        (
            "Iddin dat wight, Antoine?\x01",
            "You help'd find da bad guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "What a good widdle kitty you are!\x01",
            "Yes, you are!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(    #76
        0xFE,
        "...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #77
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Ahem...yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "How can I help you?\x02",
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_195A")

    label("loc_17D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_18FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186A")

    ChrTalk(    #81
        0xFE,
        "Oh, good! Antoine's with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I believe he can provide us with\x01",
            "some crucial information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Very well, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_186A")


    ChrTalk(    #84
        0xFE,
        (
            "If you bring Antoine with you,\x01",
            "he should be able to provide\x01",
            "an important hint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "The General Goods store sells\x01",
            "the Fresh Milk he prefers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FC")

    Jump("loc_195A")

    label("loc_18FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1910")
    Call(1, 2)
    Jump("loc_195A")

    label("loc_1910")


    ChrTalk(    #86
        0xFE,
        "Hmm... That's strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "I could have sworn I left them here...\x02",
    )

    CloseMessageWindow()

    label("loc_195A")

    Jump("loc_32D1")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_279A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    ChrTalk(    #88
        0xFE,
        "Did you forget something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I think your only option right\x01",
            "now is to go to Operations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A4D")

    label("loc_19D5")


    ChrTalk(    #90
        0xFE,
        "Oh yes, I forgot to mention...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "If you ever find yourself lost,\x01",
            "go to the Information Desk\x01",
            "on the first floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4D")

    Jump("loc_2797")

    label("loc_1A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABD")

    ChrTalk(    #92
        0xFE,
        (
            "Have you already completed\x01",
            "your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Operations is on the fifth floor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B10")

    label("loc_1ABD")


    ChrTalk(    #94
        0xFE,
        (
            "If you ever find yourself lost go\x01",
            "to the Information Desk on the\x01",
            "first floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B10")

    Jump("loc_2797")

    label("loc_1B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D6")
    OP_A2(0x0)
    OP_A2(0x58A)
    OP_A2(0x58A)
    OP_A2(0x0)

    ChrTalk(    #95
        0xFE,
        (
            "It would seem yesterday was\x01",
            "quite stressful for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Things here were mostly like usual,\x01",
            "but everyone else was rushing about\x01",
            "until all hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "When I came in this morning\x01",
            "I found Antoine asleep on the\x01",
            "bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Poor little dear was exhausted...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #99
        0x101,
        "#505FAntoine?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #100
        0xFE,
        "Why, that's the cat's name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Antoine has been living in the\x01",
            "central factory for quite some\x01",
            "time now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CED")

    def lambda_1CE5():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1CE5)

    label("loc_1CED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D07")

    def lambda_1CFF():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1CFF)

    label("loc_1D07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D21")

    def lambda_1D19():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1D19)

    label("loc_1D21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D3B")

    def lambda_1D33():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1D33)

    label("loc_1D3B")

    TurnDirection(0x0, 0xB, 400)
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(    #102
        0xFE,
        (
            "He doesn't have an owner and\x01",
            "tends to be cared for by anyone\x01",
            "who feels the urge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#000FSo he's kind of like everybody's cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "I suppose you could say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Though I'm sure Antoine has little\x01",
            "desire to be formally owned by\x01",
            "any one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Do be friendly to him if you\x01",
            "see him around the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#001FOf course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EB6")

    def lambda_1EAE():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1EAE)

    label("loc_1EB6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ED0")

    def lambda_1EC8():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1EC8)

    label("loc_1ED0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EEA")

    def lambda_1EE2():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1EE2)

    label("loc_1EEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F04")

    def lambda_1EFC():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1EFC)

    label("loc_1F04")

    TurnDirection(0x0, 0x8, 400)

    ChrTalk(    #108
        0xFE,
        (
            "Now that I've introduced you to\x01",
            "Antoine, I believe it's time for me\x01",
            "to return to work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2215")
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #109
        0xFE,
        (
            "Didn't you have something you\x01",
            "needed to do yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#505FWe were on our way to\x01",
            "Operations, yes.\x02\x03",

            "There's something we need\x01",
            "to check out up there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #111
        0xFE,
        "Operations?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I hope it's all right to go up\x01",
            "there... They've been in the\x01",
            "middle of recalibrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#014FIs there some kind of problem?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #114
        0xFE,
        (
            "No. Operations is just a lot of\x01",
            "delicate machinery that needs\x01",
            "a lot of attention. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Go and see for yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#501FAre you sure it's all right?\x01",
            "It doesn't sound all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#010FWe have to go anyway, so\x01",
            "worrying will do little good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#000FYeah, true enough.\x02\x03",

            "See you, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#010FThank you for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Good bye.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22D3")

    label("loc_2215")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #121
        0xFE,
        (
            "Didn't you have something you\x01",
            "needed to do yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#505FYes, we've got to get that gasoline\x01",
            "and the Combustion Engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#010FThank you for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Good bye.\x02",
    )

    CloseMessageWindow()

    label("loc_22D3")

    Jump("loc_2797")

    label("loc_22D6")

    OP_A2(0x0)
    OP_A2(0x58A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A6")

    ChrTalk(    #125
        0xFE,
        "Well, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Did you meet with Professor Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#000FYes we did. We're helping him\x01",
            "out right now, as a matter of fact.\x02\x03",

            "We need to go check something\x01",
            "out up in Operations.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #128
        0xFE,
        "Operations?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I hope it's all right to go up\x01",
            "there... They've been in the\x01",
            "middle of recalibrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#010FIs there some kind of problem?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #131
        0xFE,
        (
            "No. Operations is just a lot of\x01",
            "delicate machinery that needs\x01",
            "a lot of attention. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "Go and see for yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#000FAre you sure it's all right?\x01",
            "It doesn't sound all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        (
            "#010FWe have to go anyway, so\x01",
            "worrying will do little good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#000FYeah, true enough.\x02\x03",

            "See you, Doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#010FThank you for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Goodbye.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2797")

    label("loc_25A6")


    ChrTalk(    #138
        0xFE,
        "Well, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Did you meet with Professor Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#000FYes we did. We're helping him\x01",
            "out right now, as a matter of fact.\x02\x03",

            "We've got to go get something\x01",
            "for him right now, actually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #141
        0xFE,
        (
            "I see. Well, the central factory\x01",
            "is a big place. See that you\x01",
            "don't get lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "If you ever find yourself lost,\x01",
            "go to the Information Desk\x01",
            "on the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        "#010FThank you, we will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "Well, I need to start work myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#010FPlease excuse us, then.\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2797")

    Jump("loc_32D1")

    label("loc_279A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_282D")

    ChrTalk(    #146
        0xFE,
        (
            "Professor Russell should be\x01",
            "in his workshop down on the\x01",
            "third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "He's usually hard at work by\x01",
            "this hour of the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0B")

    label("loc_282D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_END)), "loc_2899")

    ChrTalk(    #148
        0xFE,
        (
            "Did you already go to Professor\x01",
            "Russell's workshop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "His workshop is on the third floor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F0B")

    label("loc_2899")

    OP_A2(0x0)
    OP_A2(0x589)

    ChrTalk(    #150
        0xFE,
        "Good morning to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "It would seem yesterday was\x01",
            "quite stressful for everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #152
        0x107,
        (
            "#065FDoctor...?\x02\x03",

            "Was everything here all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #153
        0xFE,
        (
            "The clinic isn't quite tied into\x01",
            "the rest of the factory, so\x01",
            "things were mostly quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Everyone else was running about\x01",
            "until all hours, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "When I came in this morning,\x01",
            "I found Antoine asleep on the\x01",
            "bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "Poor little dear was exhausted...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #157
        0x101,
        "#505FAntoine?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #158
        0x107,
        (
            "#560FThat's what we call the cat.\x02\x03",

            "He's been living here at the\x01",
            "factory for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AFB")

    def lambda_2AF3():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2AF3)

    label("loc_2AFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B15")

    def lambda_2B0D():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2B0D)

    label("loc_2B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B2F")

    def lambda_2B27():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2B27)

    label("loc_2B2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B49")

    def lambda_2B41():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2B41)

    label("loc_2B49")

    TurnDirection(0x0, 0xB, 400)
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(    #159
        0xFE,
        (
            "He doesn't have an owner and \x01",
            "tends to be cared for by anyone\x01",
            "who feels the urge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#000FSo he's kind of like everybody's cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x107,
        "#061FYes, something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Though I'm sure Antoine has little\x01",
            "desire to be formally owned by\x01",
            "any one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Do be friendly to him if you\x01",
            "see him around the factory.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #164
        0x101,
        "#001FOf course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CCD")

    def lambda_2CC5():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2CC5)

    label("loc_2CCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CE7")

    def lambda_2CDF():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2CDF)

    label("loc_2CE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D01")

    def lambda_2CF9():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2CF9)

    label("loc_2D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D1B")

    def lambda_2D13():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2D13)

    label("loc_2D1B")

    TurnDirection(0x0, 0x8, 400)

    ChrTalk(    #165
        0xFE,
        (
            "Now that I've introduced you to\x01",
            "Antoine, I believe it's time for me\x01",
            "to return to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #166
        0xFE,
        (
            "Weren't you in the middle of\x01",
            "something yourself, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x107,
        (
            "#060FYes, ma'am.\x02\x03",

            "I was on my way to talk to\x01",
            "my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Professor Russell should be\x01",
            "in his workshop down on the\x01",
            "third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "He came in especially early\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        "#010FThe third floor workshop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#501FGot it. Let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x107,
        (
            "#560FYes, we probably should.\x02\x03",

            "Good bye, Dr. Miriam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "Good bye.\x02",
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x40)

    label("loc_2F0B")

    Jump("loc_32D1")

    label("loc_2F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_322E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 0)), scpexpr(EXPR_END)), "loc_2FC7")

    ChrTalk(    #174
        0xFE,
        (
            "Tita has definitely picked up\x01",
            "her reasonable nature from\x01",
            "her grandfather...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "But I hope she doesn't also pick\x01",
            "up his tendency to forget his\x01",
            "regular check-ups.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_322B")

    label("loc_2FC7")

    OP_A2(0x588)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #176
        0xFE,
        "Why, hello, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "How is your grandfather?\x01",
            "Is he doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x107,
        (
            "#560FYes, ma'am. He's still as\x01",
            "healthy as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "But the strange work schedule\x01",
            "he keeps is sure to catch up\x01",
            "with him eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "Please tell him not to miss\x01",
            "his next check-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x107,
        "#061FYes, ma'am, I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Tita, you've definitely picked up\x01",
            "your reasonable nature from\x01",
            "your grandfather...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "...but he's always coming up with\x01",
            "the most outlandish excuses to\x01",
            "miss his check-ups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "It's rather like dealing with a\x01",
            "small child...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x107,
        (
            "#067FHa ha...um...\x01",
            "Sounds like Grandpa, all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322B")

    Jump("loc_32D1")

    label("loc_322E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_32D1")

    ChrTalk(    #187
        0xFE,
        "Is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "This is the factory clinic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "We're equipped for dealing with\x01",
            "conventional illness too, so don't\x01",
            "hesitate to come in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D1")

    TalkEnd(0xFE)
    Return()

    # Function_7_9B2 end

    def Function_8_32D5(): pass

    label("Function_8_32D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_3322")

    ChrTalk(    #190
        0xFE,
        "*cough* *hack*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "My lungs still aren't feeling\x01",
            "better yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3322")

    TalkEnd(0xFE)
    Return()

    # Function_8_32D5 end

    def Function_9_3326(): pass

    label("Function_9_3326")

    EventBegin(0x0)
    OP_6D(-3770, 0, 7220, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x8, -1330, 0, -4950, 180)
    SetChrPos(0x107, -2140, 0, -4950, 180)
    SetChrPos(0x101, -3440, 0, -6060, 90)
    SetChrPos(0x102, 840, 0, 1080, 270)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_6D(-1680, 0, -3300, 4000)

    ChrTalk(    #192
        0x8,
        (
            "#5PFirst things first: We have\x01",
            "to perform first aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#5PIt looks to be some unique\x01",
            "form of neurotoxin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "#5PMy usual array of antidotes won't \x01",
            "work on something like this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #195
        0x107,
        (
            "#063F#3PU-Umm... What's going to\x01",
            "happen to him...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x8,
        (
            "#5PWell, he's a fighter, so I think\x01",
            "he'll manage to hold out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#5PBut in all likelihood, the\x01",
            "longer he stays in this coma,\x01",
            "the greater the risk of death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x107,
        "#069F#3P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#003F#1PN-No...\x02",
    )

    CloseMessageWindow()
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_8E(0x102, 0xFFFFFBBE, 0x0, 0x3A2, 0xBB8, 0x0)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_8E(0x102, 0xFFFFF1DC, 0x0, 0xFFFFFE84, 0xBB8, 0x0)

    def lambda_35F7():
        OP_8E(0xFE, 0xFFFFF1DC, 0x0, 0xFFFFEE08, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35F7)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    def lambda_3635():

        label("loc_3635")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3635")

    QueueWorkItem2(0x101, 1, lambda_3635)

    ChrTalk(    #200
        0x101,
        "#002F#2PJoshua...\x02",
    )

    CloseMessageWindow()

    def lambda_365D():

        label("loc_365D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_365D")

    QueueWorkItem2(0x107, 1, lambda_365D)

    def lambda_366E():

        label("loc_366E")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_366E")

    QueueWorkItem2(0x8, 1, lambda_366E)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #201
        0x102,
        (
            "#010F#1PSorry I took so long. I had\x01",
            "to report in to Kilika.\x02\x03",

            "She passed the info on to the\x01",
            "military, so if anything comes\x01",
            "up, we should find out soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#007F#2POkay... Thank you.\x02\x03",

            "#004FHey, where'd Zin go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        (
            "#010F#1PApparently, he and Kilika\x01",
            "know each other.\x02\x03",

            "They had a lot to discuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#000F#2PI see... Well, they are\x01",
            "both Easterners.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #205
        0x102,
        (
            "#012F#1PSo...\x01",
            "How's he doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#003F#2PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x107,
        "#063F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        "#012F#1PNot so well, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "#4PUnfortunately, I'm not so well-versed\x01",
            "in poisons that I can counteract the\x01",
            "effects without knowing the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#4PBut Father Vixen might\x01",
            "be able to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x107,
        "#064F#5PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#505F#5PFather Vixen?\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0xFF)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #213
        0x107,
        (
            "#560F#5PUm...\x01",
            "He's a priest in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3967():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3967)

    def lambda_3975():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3975)
    Sleep(400)

    ChrTalk(    #214
        0x8,
        (
            "#2PHe's built up a substantial knowledge\x01",
            "of medicine by tapping the Septian\x01",
            "Church's millennium-old archives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        (
            "#2PHe's particularly learned\x01",
            "in pharmacology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "#2PHe may be able to devise some\x01",
            "form of remedy to counteract\x01",
            "the poison's effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#501F#5PAhh, I get it. The priest in\x01",
            "Rolent is also really good with\x01",
            "this stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x102,
        (
            "#010F#1PIt's certainly worth asking about.\x02\x03",

            "It's late...but let's see if\x01",
            "going to the church will net\x01",
            "us anything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #219
        0x107,
        "#062F#2PO-Okay...!\x02",
    )

    CloseMessageWindow()
    OP_28(0x42, 0x4, 0x2)
    OP_28(0x42, 0x4, 0x4)
    OP_28(0x42, 0x1, 0x1)
    OP_28(0x42, 0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0xFF)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, -4490, 0, -1400, 0)
    SetChrPos(0x102, -4490, 0, -1400, 0)
    SetChrPos(0x107, -4490, 0, -1400, 0)
    OP_6D(-4490, 0, -1400, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x800)
    EventEnd(0x0)
    Return()

    # Function_9_3326 end

    def Function_10_3BFB(): pass

    label("Function_10_3BFB")

    EventBegin(0x0)
    ClearMapFlags(0x10000000)
    OP_6D(-2250, 0, -130, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    SetChrPos(0x8, -3660, 0, -5180, 135)
    SetChrPos(0x101, -1990, 0, 1000, 225)
    SetChrPos(0x102, -1280, 0, 1910, 225)
    SetChrPos(0x108, -940, 0, 820, 225)
    SetChrPos(0x107, -1410, 0, 160, 225)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #220
        0x101,
        "#006FWe're back, Doctor!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)

    def lambda_3CE4():
        OP_6D(-2250, 0, 1000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CE4)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0xFFFFFB78, 0xFA0, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #221
        0x8,
        "#6PHow'd it go?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x107,
        "#061FThe priest gave us the medicine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "#6PReally?! I knew he wouldn't\x01",
            "let us down!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFF45C, 0x0, 0xFFFFFDF8, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #224
        "\x07\x00Handed over \x07\x02Arve Sovereign Serum\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x366, 1)
    OP_8F(0x101, 0xFFFFF678, 0x0, 0x10E, 0xBB8, 0x0)

    ChrTalk(    #225
        0x8,
        (
            "#6PI see... This will stimulate\x01",
            "his natural immune response.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        "#6PIt's worth a shot...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x8, -1330, 0, -4950, 180)
    SetChrPos(0x107, -2140, 0, -4950, 180)
    SetChrPos(0x101, -3440, 0, -6060, 90)
    SetChrPos(0x102, -3430, 0, -6960, 90)
    SetChrPos(0x108, -3630, 0, -5030, 135)
    OP_6D(-1680, 0, -3300, 0)
    Sleep(1500)

    ChrTalk(    #227
        0x8,
        "#5PNow to get him to drink it...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #228
        "\x07\x05Dr. Miriam used an oral syringe to administer the medicine to Agate.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #229
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#002F#1P*gulp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x107,
        "#063F#5PAidios, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        "#053F#2P...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #233
        0x9,
        "#053F#2P...Mmmngh...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x14, 0x0, 0x190, 0xFA0)

    ChrTalk(    #234
        0x9,
        "#056F#2PRrrr...rrrrrhhh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 5)
    OP_9E(0x9, 0x1E, 0x0, 0x1F4, 0xFA0)

    ChrTalk(    #235
        0x9,
        "#059F#2PGaaaaaggghh...AAAAAHHHH!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x107,
        "#069F#5PEep...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#002F#1PWhoa! Why's he screaming\x01",
            "like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#010F#1PIt's okay... I think he's\x01",
            "going to be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#004F#1PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x108,
        (
            "#070F#1PThe medicine is beginning\x01",
            "to take effect.\x02\x03",

            "It hurts, and it's rough on his\x01",
            "system, but he'll recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x8,
        "#5PHa ha... Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        (
            "#5PThis should take him out of\x01",
            "any immediate danger from the\x01",
            "neurotoxin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        "#501F#1PO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x107,
        "#063F#5PB-But...he's in so much pain...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x8,
        (
            "#5PYes, and he will be for the\x01",
            "better part of a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        (
            "#5PBut he'll be all right. He's\x01",
            "going to pull through and make\x01",
            "a full recovery.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #247
        "\x07\x05And so, Agate's life was saved.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #248
        "\x07\x05Late into the night, Estelle and the others slept in shifts to watch over him.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    OP_20(0x3E8)
    OP_21()
    OP_77(0x70, 0x91, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x107, -1160, 0, 6540, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_6D(-1160, 0, 6540, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    OP_1D(0x53)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #249
        0x107,
        (
            "#064FHmmm... That's strange...\x02\x03",

            "Now where's that spare towel...\x01",
            "Ah-HA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x9,
        "#1P*pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        "#1P...Urrraaaahh...\x02",
    )

    CloseMessageWindow()
    OP_4A(0x107, 255)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #252
        0x107,
        "#062F!!!\x02",
    )

    CloseMessageWindow()

    def lambda_448D():
        OP_6D(-1300, 0, -4950, 4500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_448D)
    OP_8E(0x107, 0xFFFFEACA, 0x0, 0x1446, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFF114, 0x0, 0xFFFFED90, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFFAEC, 0x0, 0xFFFFECAA, 0x1388, 0x0)
    OP_8C(0x107, 180, 400)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #253
        0x107,
        (
            "#065F#6PA-Agate...\x02\x03",

            "He's sweating like crazy...\x01",
            "I need to dry him...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #254
        0x9,
        "#553F#4P...Nnnh...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #255
        0x107,
        (
            "#560F#6PA-Agate!\x01",
            "Are you awake...?\x02\x03",

            "I'll bring you some water...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x1, 0x3, 0x320)
    Sleep(500)

    ChrTalk(    #256
        0x9,
        "#553F#4PM-Mischa...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x107,
        "#064F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x9,
        (
            "#554F#4PTh-Thank the Goddess...\x01",
            "There...you are...\x02\x03",

            "I'm...right here...\x01",
            "Don't be...scared...\x02\x03",

            "...Just... Just...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x5, 0x2BC)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #259
        0x9,
        "#053F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x107,
        "#065F#6PA-Agate?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #261
        (
            "\x07\x05Tita put a hand to Agate's forehead, confirming his fever. She wiped his\x01",
            "brow and laid a cool towel upon him.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #262
        (
            "\x07\x05Gradually the pain left his face, and his breathing grew less ragged. Soon,\x01",
            "all was quiet and calm, and he drifted off into a peaceful slumber.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #263
        0x107,
        (
            "#561F#6PWhew...\x01",
            "Thank goodness...\x02\x03",

            "#066F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #264
        0x107,
        (
            "#063F#6PBut...\x02\x03",

            "...Who's Mischa?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0xD, 0x0, 0x64)
    SetMapFlags(0x100000)
    Sleep(3000)
    OP_A2(0x558)
    OP_28(0x42, 0x1, 0x200)
    ClearMapFlags(0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3BFB end

    SaveToFile()

Try(main)
