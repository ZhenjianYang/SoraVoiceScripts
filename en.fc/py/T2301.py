from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2301   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2301   ._SN',
            'ED6_DT01/T2300_1 ._SN',
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
        'Girl in Uniform',                      # 9
        'Sieg',                                 # 10
        'Boy Wearing Cap',                      # 11
        'Clem',                                 # 12
        'Sadie',                                # 13
        'Mary',                                 # 14
        'Amelia',                               # 15
        'Camera',                               # 16
        'Orvid',                                # 17
        'Lucia',                                # 18
        'Daniel',                               # 19
        'Polly',                                # 20
        'Manoria Byroad',                       # 21
        'Gull Seaside Way',                     # 22
    )

    DeclEntryPoint(
        Unknown_00              = 9000,
        Unknown_04              = 6000,
        Unknown_08              = -3000,
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH02630 ._CH',             # 04
        'ED6_DT07/CH01050 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01070 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH00004 ._CH',             # 0A
        'ED6_DT07/CH00044 ._CH',             # 0B
        'ED6_DT07/CH00003 ._CH',             # 0C
        'ED6_DT07/CH00013 ._CH',             # 0D
        'ED6_DT07/CH00005 ._CH',             # 0E
        'ED6_DT06/CH20051 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT06/CH20085 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH02630P._CP',             # 04
        'ED6_DT07/CH01050P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01070P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH00004P._CP',             # 0A
        'ED6_DT07/CH00044P._CP',             # 0B
        'ED6_DT07/CH00003P._CP',             # 0C
        'ED6_DT07/CH00013P._CP',             # 0D
        'ED6_DT07/CH00005P._CP',             # 0E
        'ED6_DT06/CH20051P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT06/CH20085P._CP',             # 11
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
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
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 46980,
        Z                   = 0,
        Y                   = 22480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 37310,
        Z                   = 1700,
        Y                   = -33090,
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
        X                   = -4100,
        Z                   = 8000,
        Y                   = 45100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
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
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 4000,
        Y                   = 29000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
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
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
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


    DeclEvent(
        X                   = 16870,
        Y                   = 7000,
        Z                   = -7690,
        Range               = -9400,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFF998,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 8200,
        Y                   = 4000,
        Z                   = 9300,
        Range               = 1460,
        Unknown_10          = 0x178E,
        Unknown_14          = 0x198C,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 65500,
        Y                   = -1000,
        Z                   = 23100,
        Range               = 68250,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x4736,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -760,
        Y                   = 5000,
        Z                   = 59750,
        Range               = -5380,
        Unknown_10          = 0x2670,
        Unknown_14          = 0xF4D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )


    ScpFunction(
        "Function_0_3DA",          # 00, 0
        "Function_1_572",          # 01, 1
        "Function_2_58A",          # 02, 2
        "Function_3_5A0",          # 03, 3
        "Function_4_5C4",          # 04, 4
        "Function_5_61C",          # 05, 5
        "Function_6_CD0",          # 06, 6
        "Function_7_D25",          # 07, 7
        "Function_8_D77",          # 08, 8
        "Function_9_DE8",          # 09, 9
        "Function_10_E63",         # 0A, 10
        "Function_11_12A8",        # 0B, 11
        "Function_12_20C3",        # 0C, 12
        "Function_13_20D3",        # 0D, 13
        "Function_14_301F",        # 0E, 14
        "Function_15_3AED",        # 0F, 15
        "Function_16_3AF8",        # 10, 16
        "Function_17_46ED",        # 11, 17
        "Function_18_4FCD",        # 12, 18
        "Function_19_54EE",        # 13, 19
        "Function_20_550A",        # 14, 20
        "Function_21_58DE",        # 15, 21
        "Function_22_58FA",        # 16, 22
        "Function_23_58FE",        # 17, 23
        "Function_24_5902",        # 18, 24
    )


    def Function_0_3DA(): pass

    label("Function_0_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3E4")
    Jump("loc_4AF")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_3F8")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_4AF")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_476")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2050, 3970, 31120, 0)
    OP_43(0xB, 0x0, 0x0, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5690, 4160, 30210, 0)
    OP_43(0xD, 0x0, 0x0, 0x3)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -3290, 3990, 27420, 0)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -5420, 4000, 27290, 0)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4AF")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_480")
    Jump("loc_4AF")

    label("loc_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_48A")
    Jump("loc_4AF")

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_4AF")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_49E")
    Jump("loc_4AF")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_4A8")
    Jump("loc_4AF")

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4AF")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ClearChrFlags(0xE, 0x80)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4E5")
    OP_A3(0x3FA)
    Event(0, 16)

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_501")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 17)

    label("loc_501")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_511"),
        (105, "loc_54D"),
        (SWITCH_DEFAULT, "loc_560"),
    )


    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    OP_A2(0x409)
    Event(0, 10)
    Jump("loc_54A")

    label("loc_523")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x36)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54A")
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x1, 0x8)
    RemoveParty(0x36, 0xFF)
    Event(1, 1)

    label("loc_54A")

    Jump("loc_560")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55D")
    Event(0, 11)

    label("loc_55D")

    Jump("loc_560")

    label("loc_560")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_3DA end

    def Function_1_572(): pass

    label("Function_1_572")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x3004B)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_572 end

    def Function_2_58A(): pass

    label("Function_2_58A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_58A")

    label("loc_59F")

    Return()

    # Function_2_58A end

    def Function_3_5A0(): pass

    label("Function_3_5A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C3")
    OP_8D(0xFE, -6100, 32000, 300, 25200, 3000)
    Jump("Function_3_5A0")

    label("loc_5C3")

    Return()

    # Function_3_5A0 end

    def Function_4_5C4(): pass

    label("Function_4_5C4")

    TalkBegin(0xC)

    ChrTalk(    #0
        0xC,
        (
            "Once the store is cleaned up,\x01",
            "I was thinking of going to\x01",
            "check on the kids.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_4_5C4 end

    def Function_5_61C(): pass

    label("Function_5_61C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_6DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_692")
    OP_A2(0x1)

    ChrTalk(    #1
        0xFE,
        "Who were those nasty old men?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Were they teasing Polly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "You gotta make 'em pay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D8")

    label("loc_692")


    ChrTalk(    #4
        0xFE,
        (
            "You just can't let people who\x01",
            "pick on everyone get away\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8")

    Jump("loc_CCC")

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74C")
    OP_A2(0x1)

    ChrTalk(    #5
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came home crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "How come? Was someone mean\x01",
            "to them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_771")

    label("loc_74C")


    ChrTalk(    #7
        0xFE,
        "Who was being mean to everyone?\x02",
    )

    CloseMessageWindow()

    label("loc_771")

    Jump("loc_CCC")

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_80D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF")
    OP_A2(0x1)

    ChrTalk(    #8
        0xFE,
        (
            "Me and Polly play together\x01",
            "every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I'm sure glad I have lots of friends.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_7DF")


    ChrTalk(    #10
        0xFE,
        "I'm sure glad I have lots of friends.\x02",
    )

    CloseMessageWindow()

    label("loc_80A")

    Jump("loc_CCC")

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_8CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A")
    OP_A2(0x1)

    ChrTalk(    #11
        0xFE,
        "Clem ran outside in a big hurry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Did he do something bad again\x01",
            "and make the matron all mad?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC")

    label("loc_88A")


    ChrTalk(    #13
        0xFE,
        (
            "Did Clem do something bad again\x01",
            "and make the matron all mad?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CC")

    Jump("loc_CCC")

    label("loc_8CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_9E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_963")
    OP_A2(0x1)

    ChrTalk(    #14
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "They were all upset about\x01",
            "something, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DD")

    label("loc_963")


    ChrTalk(    #17
        0xFE,
        (
            "Everyone from the orphanage\x01",
            "came over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "They were all upset about\x01",
            "something, though...\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DD")

    Jump("loc_CCC")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A93")
    OP_A2(0x1)

    ChrTalk(    #19
        0xFE,
        (
            "*sigh* I wanna go play at\x01",
            "the orphanage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "It must be nice, being like brothers\x01",
            "and sisters with all those kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I wanna be their friend, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_A93")


    ChrTalk(    #22
        0xFE,
        (
            "I wanna be friends with the\x01",
            "orphans, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jump("loc_CCC")

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_B50")

    ChrTalk(    #23
        0xFE,
        (
            "The kids at the orphanage come\x01",
            "to Manoria and play sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I've seen 'em a few times.\x01",
            "The matron seems really nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB5")
    OP_A2(0x1)

    ChrTalk(    #25
        0xFE,
        "A boy in a cap? You mean him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Umm, I saw him over by the\x01",
            "flower shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_BB5")


    ChrTalk(    #27
        0xFE,
        (
            "If you're lookin' for a little boy,\x01",
            "I think I saw him over by the\x01",
            "flower shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C09")

    Jump("loc_CCC")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85")
    OP_A2(0x1)

    ChrTalk(    #28
        0xFE,
        "Are you guys customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I live over at the inn!\x01",
            "You oughtta stop in,\x01",
            "if you have time. ★\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_C85")


    ChrTalk(    #30
        0xFE,
        (
            "I live over at the inn!\x01",
            "You oughtta stop in,\x01",
            "if you have time. ★\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCC")

    TalkEnd(0x11)
    Return()

    # Function_5_61C end

    def Function_6_CD0(): pass

    label("Function_6_CD0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(    #31
        0xFE,
        (
            "#770FOh, hey!\x02\x03",

            "Everyone's been doing\x01",
            "pretty good.\x02\x03",

            "You can relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D21")

    TalkEnd(0xB)
    Return()

    # Function_6_CD0 end

    def Function_7_D25(): pass

    label("Function_7_D25")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_D73")

    ChrTalk(    #32
        0xFE,
        "Thanks for helping Clem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "He can be a real pain sometimes.\x02",
    )

    CloseMessageWindow()

    label("loc_D73")

    TalkEnd(0xD)
    Return()

    # Function_7_D25 end

    def Function_8_D77(): pass

    label("Function_8_D77")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_DB7")

    ChrTalk(    #34
        0xFE,
        (
            "I wonder what's gonna go with\x01",
            "dinner tonight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE4")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_DE4")

    ChrTalk(    #35
        0xFE,
        "What's Clem all worked up about?\x02",
    )

    CloseMessageWindow()

    label("loc_DE4")

    TalkEnd(0x12)
    Return()

    # Function_8_D77 end

    def Function_9_DE8(): pass

    label("Function_9_DE8")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E13")

    ChrTalk(    #36
        0xFE,
        "I'm playin' wif evvyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5F")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_E5F")

    ChrTalk(    #37
        0xFE,
        (
            "Clem looked all upset when we had\x01",
            "puddin'. Was his puddin' bad?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5F")

    TalkEnd(0x13)
    Return()

    # Function_9_DE8 end

    def Function_10_E63(): pass

    label("Function_10_E63")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, -2020, 8000, 57380, 180)
    SetChrPos(0x102, -3170, 8039, 57530, 180)
    OP_6D(-2500, 6000, -3290, 0)
    OP_6C(310000, 0)
    OP_6B(5900, 0)

    def lambda_EB5():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB5)
    Sleep(2000)

    def lambda_ECA():
        OP_6D(-2100, 7980, 57740, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECA)
    OP_6B(3000, 8000)

    ChrTalk(    #38
        0x101,
        (
            "#501F#2P*sigh*...\x01",
            "Civilization at last.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        (
            "#000F#2PAnd with all these pretty white\x01",
            "flowers blooming everywhere,\x01",
            "too...\x02\x03",

            "What did you say this place\x01",
            "was called?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#010FManoria. It's a little seaside\x01",
            "village with an inn.\x02\x03",

            "And the white flowers are a\x01",
            "type of hibiscus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#000F#2PThey're so pretty...\x02\x03",

            "The ocean and the flowers together...\x01",
            "It smells great around here!\x02\x03",

            "#001FHmm... It also makes me kind of\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#019FHa ha ha. Only you could work\x01",
            "up an appetite from smelling\x01",
            "flowers.\x02\x03",

            "#011FJust make sure you eat the\x01",
            "food and not the flowers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #43
        0x101,
        (
            "#006F#2PHey, I'm a growing girl.\x02\x03",

            "It's almost noon, anyway, so\x01",
            "what would you say to lunch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#014FFine by me... But do we have\x01",
            "any provisions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#004F#2PUmm...\x02\x03",

            "#000FWhy don't we get something local?\x01",
            "It's such a nice, quiet little town...\x02\x03",

            "I mean, we just got to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#010FThat's true. Okay, let's go check\x01",
            "out the inn and tavern.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_10_E63 end

    def Function_11_12A8(): pass

    label("Function_11_12A8")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(27790, 0, 18450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 35500, -80, 17000, 270)
    SetChrPos(0x101, 27300, 480, 20630, 0)
    SetChrPos(0x102, 27300, 480, 21630, 180)
    FadeToBright(1000, 0)
    OP_8E(0x8, 0x6B44, 0x3C, 0x41BE, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #47
        0x8,
        (
            "#042FI've already checked here...\x02\x03",

            "#042FHe's not in the general store,\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13AE():
        OP_6D(27520, 60, 16390, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13AE)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    Sleep(200)
    OP_8C(0x8, 270, 400)
    Sleep(200)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #48
        0x8,
        "#043FDamn... Where could he be?\x02",
    )

    CloseMessageWindow()
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_8F(0x101, 0x6A90, 0x1F4, 0x4B8C, 0xBB8, 0x0)

    ChrTalk(    #49
        0x101,
        "#001FGet a move on, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#012FWhoa, Estelle. Watch where\x01",
            "you're going, or...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_148E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_148E)

    def lambda_149C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_149C)

    def lambda_14AA():
        OP_8F(0xFE, 0x6AF4, 0x3C, 0x431C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14AA)
    WaitChrThread(0x101, 0x1)
    OP_22(0x12, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_14D4():
        OP_96(0xFE, 0x6A68, 0x14, 0x4574, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D4)

    def lambda_14F2():
        OP_96(0xFE, 0x6B30, 0x46, 0x3D0E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14F2)
    OP_43(0x101, 0x2, 0x0, 0xC)

    ChrTalk(    #51 op#A op#5
        0x8,
        "#044F#4P#12AOof...\x05\x02",
    )


    ChrTalk(    #52 op#A op#5
        0x101,
        "#004F#1P#12AAck...\x05\x02",
    )

    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x102, 0x4)

    def lambda_1551():
        OP_8E(0xFE, 0x6C52, 0x1F4, 0x4B50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1551)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        "#007FOwwww...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(400)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0x101, 0x4)
    OP_92(0x101, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #54
        0x101,
        (
            "#004FI-I'm sorry! Are you okay?!\x02\x03",

            "I wasn't paying attention to where\x01",
            "I was going, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "#040FNo, no... It's all right.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(400)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #56
        0x8,
        (
            "#045FPardon me. I confess, my attention\x01",
            "was elsewhere, as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#501FOh, okay.\x02\x03",

            "#001FSo I guess we're even.\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_8E(0x102, 0x6E78, 0xFFFFFFD8, 0x425E, 0x7D0, 0x0)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #58
        0x102,
        (
            "#017FI swear, Estelle.\x01",
            "What are you doing?\x02\x03",

            "#014F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#040F???\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #60
        0x101,
        "#000FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#013FN-Nothing...\x02",
    )

    CloseMessageWindow()
    OP_92(0x102, 0x8, 0x4B0, 0x3E8, 0x0)

    def lambda_1799():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1799)
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(    #62
        0x102,
        (
            "#010FI'm sorry if she disturbed you.\x02\x03",

            "You're not hurt, I hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#045FNo, I'm fine.\x02\x03",

            "I was looking for someone, and\x01",
            "I wasn't watching where I was\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#501FOh, who are you looking for?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #65
        0x8,
        (
            "#040FA little boy, about ten years old,\x01",
            "wearing a cap.\x02\x03",

            "I don't suppose you've seen him,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#000FA boy in a cap...\x02\x03",

            "#000FYou see anyone like that,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#010FNot that I can recall, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#043FI see...\x01",
            "Where could he be?\x02\x03",

            "#045FIf you'll excuse me. Sorry to have\x01",
            "caused you any trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_19C1():

        label("loc_19C1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_19C1")

    QueueWorkItem2(0x101, 1, lambda_19C1)

    def lambda_19D2():

        label("loc_19D2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_19D2")

    QueueWorkItem2(0x102, 1, lambda_19D2)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_1A07():
        OP_8E(0xFE, 0xA0BE, 0xFFFFFFEC, 0x48E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A07)
    OP_6D(30950, -30, 16970, 2000)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_63(0x101)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_6D(28490, 40, 16850, 1000)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #69
        0x101,
        (
            "#002FJoshua?\x02\x03",

            "#002FHello... Calling Joshua, come in,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #70
        0x102,
        "#014F#2POh, uhh... What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#007FGee, I wonder.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #72
        0x101,
        (
            "#004FOh, I get it...\x02\x03",

            "#001FI see what's going on. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#018F#2PWhat half-baked idea are you\x01",
            "cooking up THIS time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#006FNow, now. No need to be shy\x01",
            "about it.\x02\x03",

            "I see the way she's set your\x01",
            "heart aflutter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#017F#2PAb-so-lute-ly NOT.\x02\x03",

            "I just think I've met her before,\x01",
            "a long time ago.\x02\x03",

            "#010F#2PI was just surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#004FHmmmmm... 'Met her before,'\x01",
            "you say.\x02\x03",

            "#502FAs pick-up lines go, I give it\x01",
            "thirty points.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #77
        0x102,
        (
            "#015F#2PMoving on...\x01",
            "Don't you recognize her uniform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#004FNow that you mention it...\x02\x03",

            "Isn't that the same outfit that\x01",
            "Josette used as a disguise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#010F#2PYep. The Jenis Royal Academy\x01",
            "uniform.\x02\x03",

            "Since we're in Ruan, it's not all\x01",
            "that surprising to see someone\x01",
            "wearing one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#501FAhh... So that's the real thing,\x01",
            "then?\x02\x03",

            "#001FShe seemed polite and smart...\x01",
            "and refined.\x02\x03",

            "Totally different from that scruffy,\x01",
            "crude pretender, in other words!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#015F#2PWhat are you talking about?\x02\x03",

            "Josette had you completely\x01",
            "fooled from the get-go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#009F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#019F#2POh, that's right. You teased me\x01",
            "about it THEN, too.\x02\x03",

            "Well, if you get taken for a\x01",
            "fool again, don't expect me\x01",
            "to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#003FGrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#019F#2PInstead of picking on me, why not\x01",
            "work on becoming a better judge\x01",
            "of character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#007FAll right, all right!\x02\x03",

            "Fine, I won't pick on you\x01",
            "anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#010F#2PGood.\x02\x03",

            "Now, why don't we go have lunch\x01",
            "up on the viewing platform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#007FFine...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x40A)
    EventEnd(0x0)
    Return()

    # Function_11_12A8 end

    def Function_12_20C3(): pass

    label("Function_12_20C3")

    Sleep(200)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x8, 11)
    Return()

    # Function_12_20C3 end

    def Function_13_20D3(): pass

    label("Function_13_20D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_301E")
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #89
        0x101,
        "#004FWow, check out this view!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#010FYep, you can practically see\x01",
            "the entire ocean from here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2186():
        OP_6D(2428, 6000, -13190, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2186)

    def lambda_219E():
        OP_6B(8450, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219E)

    def lambda_21AE():
        OP_6C(60000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21AE)

    def lambda_21BE():
        OP_67(0, 5095, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21BE)
    StopSound(0x9470, 0x3D090, 0x1B58)
    Sleep(7000)

    ChrTalk(    #91
        0x101,
        (
            "#501FGetting to eat at a nice place like\x01",
            "this really makes it feel like\x01",
            "you're living it up, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        (
            "#010FIt sure does.\x02\x03",

            "So, shall we have ourselves\x01",
            "a little picnic, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#501FSure!\x02\x03",

            "#001FI'm starving!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(5420, 6000, -13860, 0)
    OP_6B(2800, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    StopSound(0x9470, 0x14C08, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x102, 13)
    SetChrPos(0x101, 5200, 6200, -13860, 180)
    SetChrPos(0x102, 6100, 6200, -13860, 180)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 2)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #94
        0x101,
        (
            "#501F#3PGet a load of this smoked\x01",
            "ham sandwich!\x02\x03",

            "Mmmm, it smells so good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#010FI'm looking forward to eating my\x01",
            "seafood paella, personally.\x02\x03",

            "I love the smell of saffron.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#001F#3PWell, let's dig in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#015FYes, let's.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(300)

    ChrTalk(    #98
        0x101,
        (
            "#501F#3PTime for that first bite...\x02\x03",

            "#502F*chompmunchchew*...*gulp*\x02\x03",

            "#004FWow, it's as good as it smells!\x01",
            "The lettuce is super-fresh and\x01",
            "crunchy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#010FThe paella's really good, too.\x01",
            "Just the right amount of saffron.\x02\x03",

            "My compliments to the chef.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #100
        0x101,
        (
            "#501F#3PHey, can I have a bite?\x02\x03",

            "I've never tried paella before.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(300)

    ChrTalk(    #101
        0x102,
        "#010FAll right... How about we share?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#000F#3PHmm...but my hands are full.\x02\x03",

            "I know! You can feed me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        "#014FFeed...you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#001F#3PYep! Aaaahhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        "#018FThis is...a little embarrassing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#006F#3POh, it's fine. It's not like\x01",
            "anyone's watching.\x02\x03",

            "Unless you can let loose, you'll\x01",
            "never enjoy yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#017FIt's not being seen that makes it\x01",
            "embarrassing...\x02\x03",

            "I don't have much of a choice\x01",
            "here, do I?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #108
        "\x07\x05Joshua fed Estelle a bite of the paella.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #109
        0x101,
        (
            "#502F#3P*munchchew*...*gulp*\x02\x03",

            "#501FMmmm, delicious. That's some\x01",
            "pretty fantastic seafood.\x02\x03",

            "I don't know what that sweet-\x01",
            "peppery smell is, but it really\x01",
            "adds something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#010FYeah, it's pretty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#009F#3POh. I'm being selfish, aren't I?\x02\x03",

            "#001FOkay, give this a try!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #112
        (
            "\x07\x05Estelle pushed her sandwich into Joshua's mouth...perhaps a little too\x01",
            "enthusiastically.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #113
        0x102,
        (
            "#014FMmrrph...\x02\x03",

            "#015F*chewchewchew*...*gulp*\x02\x03",

            "#018F...That's pretty tasty, but you\x01",
            "really didn't have to do that,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#502F#3PHeh heh heh... I know.♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(5600, 6150, -15410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x101, 5150, 6150, -14900, 180)
    SetChrPos(0x102, 6010, 6000, -14900, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #115
        0x101,
        "#001FAhhh, that hit the spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#010FThe herbal tea we got with our meals\x01",
            "was pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#501FYeah, it was nice and warming\x01",
            "without sitting all heavy.\x02\x03",

            "#007FThe breeze is so nice...\x01",
            "makes me kind of sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        (
            "#010FThey say you shouldn't sleep right\x01",
            "after eating...\x02\x03",

            "...but maybe a little post-meal\x01",
            "nap isn't so bad, in moderation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#501FYeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #120
        0x101,
        "#004F...Huh?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    StopSound(0x9470, 0x20F58, 0x0)
    OP_6C(0, 0)

    def lambda_2C40():

        label("loc_2C40")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2C40")

    QueueWorkItem2(0x102, 1, lambda_2C40)

    def lambda_2C51():

        label("loc_2C51")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2C51")

    QueueWorkItem2(0x101, 1, lambda_2C51)

    def lambda_2C62():

        label("loc_2C62")

        OP_69(0x9, 0x0)
        OP_48()
        Jump("loc_2C62")

    QueueWorkItem2(0x9, 3, lambda_2C62)

    def lambda_2C73():

        label("loc_2C73")

        OP_69(0x9, 0x0)
        OP_48()
        Jump("loc_2C73")

    QueueWorkItem2(0x9, 1, lambda_2C73)

    def lambda_2C84():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2C84)

    def lambda_2C94():
        OP_6C(300000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C94)
    SetChrPos(0x9, -15000, 15680, -15710, 0)
    ClearChrFlags(0x9, 0x80)
    OP_8E(0x9, 0x4D58, 0x2CEC, 0xFFFFCFEA, 0x32C8, 0x0)
    OP_8E(0x9, 0x9B14, 0x2CEC, 0xFFFFFF92, 0x32C8, 0x0)
    OP_8E(0x9, 0xD804, 0x396C, 0x17CA, 0x32C8, 0x0)
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, 9310, 6140, -12420, 90)
    SetChrPos(0x102, 8940, 6140, -13650, 90)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(8900, 6000, -13650, 0)
    OP_6B(3000, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    StopSound(0x9470, 0x14C08, 0x0)
    OP_0D()

    ChrTalk(    #121
        0x101,
        (
            "#004FHey, did you see that bird? It\x01",
            "looked like a seagull, except\x01",
            "it was huge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        (
            "#010F#4PYeah. The wings were a different\x01",
            "shape and the beak was sharp.\x02\x03",

            "Maybe it was a falcon or an eagle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#000FA white falcon...? Didn't know\x01",
            "they made 'em in that color!\x02\x03",

            "#001FHmm... I wonder if it's a sign of\x01",
            "good fortune in our future.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #124
        0x102,
        (
            "#019F#4PHa ha. That would be nice.\x02\x03",

            "#010FHey... I thought you were sleepy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #125
        0x101,
        (
            "#008FOh...\x02\x03",

            "Not anymore, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#010F#4PMaybe we should get going, then?\x02\x03",

            "I'd like to check in with the Ruanian\x01",
            "guild branch, and get all our paperwork\x01",
            "squared away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#000FOh, right...\x02\x03",

            "Okay. I hate to leave, but I guess\x01",
            "we have to.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_A2(0x40B)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)

    label("loc_301E")

    Return()

    # Function_13_20D3 end

    def Function_14_301F(): pass

    label("Function_14_301F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AEC")
    OP_A2(0x40C)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(4130, 3990, 10660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 4590, 5970, 3440, 0)
    SetChrPos(0x102, 5510, 5980, 2610, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 180, 4050, 18030, 152)
    FadeToBright(500, 0)

    def lambda_30C4():

        label("loc_30C4")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_30C4")

    QueueWorkItem2(0x101, 3, lambda_30C4)

    def lambda_30D5():
        OP_8E(0xFE, 0x10CC, 0xF82, 0x2C9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30D5)
    Sleep(500)

    def lambda_30F5():
        OP_8E(0xFE, 0x1464, 0xFAA, 0x25D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30F5)
    Sleep(1200)

    def lambda_3115():
        OP_8E(0xFE, 0x10A4, 0xF8C, 0x2ECC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3115)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_22(0x12, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xA, 0x4)
    TurnDirection(0xA, 0x101, 0)

    def lambda_3150():
        OP_96(0xFE, 0x1126, 0xF8C, 0x28B4, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3150)

    def lambda_316E():
        OP_96(0xFE, 0x1108, 0xF78, 0x335E, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_316E)
    OP_43(0x101, 0x2, 0x0, 0xF)

    ChrTalk(    #128 op#A op#5
        0xA,
        "#774F#4P#12AWhoa!\x05\x02",
    )


    ChrTalk(    #129 op#A op#5
        0x101,
        "#004F#1P#12AOw...\x05\x02",
    )

    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #130
        0x101,
        (
            "#007FToday...must be my day for just\x01",
            "randomly running into people...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xA, 0x4)
    OP_8E(0xA, 0x114E, 0xF96, 0x2D3C, 0xBB8, 0x0)

    ChrTalk(    #131
        0xA,
        (
            "#771FSorry 'bout that. I'm just\x01",
            "looking for somebody.\x02\x03",

            "#770FSay, you're not from around\x01",
            "here, are you?\x02",
        )
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #132
        0x101,
        (
            "#000FNope. We're from out of town.\x02\x03",

            "#004FHey, aren't you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        "#772F...Wh-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#501FWe ran into a girl who said she\x01",
            "was looking for a boy who was\x01",
            "wearing a cap...\x02\x03",

            "You know anything about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xA,
        (
            "#770FOh! I'm looking for her, actually.\x02\x03",

            "Where'd you see her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#000FOver by the tavern...\x02\x03",

            "It was a while ago, though, so\x01",
            "I'm not sure where she went.\x02\x03",

            "Would you like us to help\x01",
            "you search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "#774FN-No, that's okay. I'm pretty\x01",
            "sure I can find her.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(    #138
        0xA,
        "#771FOkay, bye!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    def lambda_34D6():

        label("loc_34D6")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_34D6")

    QueueWorkItem2(0x102, 3, lambda_34D6)

    def lambda_34E7():
        OP_6D(7160, 4030, 12560, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_34E7)
    OP_8E(0xA, 0x41C8, 0x6B8, 0x3958, 0x1770, 0x0)
    SetChrFlags(0xA, 0x80)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #139
        0x101,
        (
            "#501FThat kid seems pretty energetic.\x02\x03",

            "He reminds me a little of Luke,\x01",
            "back in Rolent.\x02\x03",

            "I wonder what the kids are up\x01",
            "to now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_35B7():
        OP_6D(4380, 4019, 9800, 1200)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_35B7)
    OP_44(0x101, 0x3)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #140
        0x101,
        "#004F#2PWhat's wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102)
    OP_44(0x102, 0x3)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #141
        0x102,
        (
            "#014F#1PIt...might just be my imagination, but...\x02\x03",

            "...have you lost anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#004F#2PLost...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        (
            "#012F#1PAnything you're wearing.\x02\x03",

            "Like a money pouch or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#004F#2PWhy are you asking all of a\x01",
            "sudden?\x02\x03",

            "#006FLet's see...\x01",
            "Pouch...check.\x02\x03",

            "Hairbands...check.\x02\x03",

            "#501FBracer emblem...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #145
        0x102,
        "#015F#1PI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#004F#2PWhat the...?! Where is it?!\x02\x03",

            "Did I drop it on the mountain\x01",
            "pass or something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#012F#1PCalm down.\x02\x03",

            "I remember that you had it\x01",
            "when we were eating lunch.\x02\x03",

            "If you lost it, it has to be\x01",
            "somewhere around here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    Sleep(200)
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(400)

    ChrTalk(    #148
        0x101,
        "#002F#2PB-But...where around here?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #149
        0x101,
        "#004F#2POh, no way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#010F#1PYeah, I'm thinking the same thing.\x01",
            "It was probably that kid.\x02\x03",

            "I'll bet it happened when he\x01",
            "'accidentally' ran into you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        (
            "#005F#2P...WHAT?!\x02\x03",

            "Why would he want my\x01",
            "bracer emblem?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x102,
        (
            "#015F#1PWhat reason does a kid have\x01",
            "for wanting anything?\x02\x03",

            "He probably just took it because\x01",
            "he could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#009F#2PGrrrr... Oh, he is in SO much\x01",
            "trouble!\x02\x03",

            "#005FOnce I get my hands on him, he's\x01",
            "gonna get the spanking of his life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        (
            "#010F#1PNow, calm down...\x02\x03",

            "For now, let's focus on figuring\x01",
            "out where he is.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_3AEC")

    Return()

    # Function_14_301F end

    def Function_15_3AED(): pass

    label("Function_15_3AED")

    Sleep(200)
    SetChrChipByIndex(0x101, 14)
    Return()

    # Function_15_3AED end

    def Function_16_3AF8(): pass

    label("Function_16_3AF8")

    EventBegin(0x0)
    OP_6D(26870, 100, 17110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xD, 39130, -90, 16600, 270)
    SetChrPos(0x101, 26280, 40, 17460, 180)
    SetChrPos(0x102, 26250, 70, 16210, 0)
    SetChrPos(0x136, 27640, 40, 17110, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #155
        0x101,
        (
            "#002FThis sure has turned into a\x01",
            "royal mess.\x02\x03",

            "Where should we start the search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#012F#4PHmm...\x02\x03",

            "Maybe we should go to the guild\x01",
            "and report back to Jean.\x02\x03",

            "We can figure out a plan of\x01",
            "attack then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#006FSounds good to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x136,
        "#049F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #159
        0x101,
        (
            "#004FSomething wrong? You look like\x01",
            "something's bugging you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x136,
        (
            "#045FOh, I'm sorry...\x02\x03",

            "My mind is just all over the\x01",
            "place right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#003FI know how you feel...\x02\x03",

            "#501FBy the way, Joseph was Matron\x01",
            "Theresa's husband, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x136,
        (
            "#048FYes.\x02\x03",

            "He died several years ago...\x02\x03",

            "But he meant a great deal to\x01",
            "me, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#000FI see...\x02\x03",

            "#004FWait, does that mean...you're\x01",
            "from the orphanage, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x136,
        (
            "#045FNo, nothing like that...\x02\x03",

            "He just did a huge favor for me\x01",
            "a long time ago.\x02\x03",

            "We grew close again when I came\x01",
            "to Ruan to attend the academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#501FOh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#010FSo in other words, every time\x01",
            "you came by to play you ended\x01",
            "up helping out, like part of the family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x136,
        (
            "#048FYes...\x02\x03",

            "#047F...\x02\x03",

            "#049FHe was like a father to me...but the shock\x01",
            "I experienced was nothing compared to that\x01",
            "of the matron and the other children.\x02\x03",

            "But we managed somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xD,
        "#3PMiss Kloe!\x02",
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_4A(0xD, 255)
    ClearChrFlags(0xD, 0x80)

    def lambda_402E():
        OP_6D(28370, 100, 17960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_402E)

    def lambda_4046():

        label("loc_4046")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4046")

    QueueWorkItem2(0x136, 1, lambda_4046)

    def lambda_4057():

        label("loc_4057")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4057")

    QueueWorkItem2(0x101, 1, lambda_4057)

    def lambda_4068():

        label("loc_4068")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_4068")

    QueueWorkItem2(0x102, 1, lambda_4068)
    OP_62(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xD, 0x7198, 0xFFFFFF88, 0x4380, 0x1388, 0x0)

    ChrTalk(    #169
        0x136,
        (
            "#044FMary! What's gotten you into\x01",
            "such a hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xD,
        "Listen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xD,
        "Clem's gone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x136,
        "#043FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#004FY-You don't mean he's left\x01",
            "Manoria...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        (
            "#012FCan you give us some more\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xD,
        "Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xD,
        (
            "After that old man showed up,\x01",
            "Clem went upstairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xD,
        (
            "In a coupla minutes, he came back\x01",
            "down all red in the face saying,\x01",
            "'They're not gettin' away with this!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xD,
        "Then he just ran off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#002FI wonder who he meant...?\x02\x03",

            "You don't suppose it's...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[The orphanage's arsonist]\x01",           # 0
            "[Mayor Dalmore and his steward]\x01",      # 1
            "[The gang at the warehouse]\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4317"),
        (1, "loc_438D"),
        (2, "loc_4407"),
        (SWITCH_DEFAULT, "loc_4466"),
    )


    label("loc_4317")


    ChrTalk(    #180
        0x102,
        (
            "#012FI'll bet you're right...\x02\x03",

            "Everything points at the Ravens.\x02\x03",

            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4466")

    label("loc_438D")


    ChrTalk(    #181
        0x102,
        (
            "#017FWhy would you say that?\x02\x03",

            "#012FEverything points at the Ravens.\x02\x03",

            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4466")

    label("loc_4407")


    ChrTalk(    #182
        0x102,
        (
            "#013FYes... I believe it was the Ravens.\x02\x03",

            "He probably overheard what\x01",
            "the steward said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4466")

    label("loc_4466")


    ChrTalk(    #183
        0x101,
        (
            "#004FOh, no!\x02\x03",

            "I hope he's not planning to go\x01",
            "and find them himself...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x136, 0xFF)
    OP_8C(0x136, 270, 400)

    ChrTalk(    #184
        0x136,
        (
            "#043F#2PIt... It can't be...\x02\x03",

            "#042FI can't allow this! I have to find\x01",
            "him at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#012FWe'll come with you.\x02\x03",

            "If we hurry, we might be able\x01",
            "to catch him before he gets to\x01",
            "Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xD,
        "Miss Kloe...\x02",
    )

    CloseMessageWindow()

    def lambda_458F():

        label("loc_458F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_458F")

    QueueWorkItem2(0x136, 1, lambda_458F)
    Sleep(400)

    ChrTalk(    #187
        0x136,
        (
            "#042FDon't you worry.\x01",
            "I'll bring him back safely.\x02\x03",

            "You just look after the other\x01",
            "children, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xD,
        "Okay... Good luck!\x02",
    )

    CloseMessageWindow()

    def lambda_4628():
        OP_6D(26760, 100, 17100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4628)
    OP_8E(0xD, 0x6B62, 0x1F4, 0x4AA6, 0xBB8, 0x0)
    OP_8C(0xD, 0, 400)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    SetChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x6CFC, 0x1F4, 0x52D0, 0xBB8, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    TurnDirection(0x102, 0x136, 400)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #189
        0x101,
        "#002FLet's head back to Ruan!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 270, 400)

    ChrTalk(    #190
        0x136,
        "#042FAll right...!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_3AF8 end

    def Function_17_46ED(): pass

    label("Function_17_46ED")

    EventBegin(0x0)
    OP_6D(27410, 20, 17820, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x106, 16)
    SetChrPos(0x106, 27180, 500, 20940, 0)
    SetChrPos(0x101, 27180, 500, 20940, 0)
    SetChrPos(0x102, 27180, 500, 20940, 0)
    SetChrPos(0x105, 27180, 500, 20940, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x4, 0x1E)
    OP_73(0x4)

    def lambda_476C():
        OP_8E(0xFE, 0x6BF8, 0x0, 0x41A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_476C)
    Sleep(500)

    def lambda_478C():
        OP_8E(0xFE, 0x6914, 0x0, 0x44B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_478C)
    Sleep(500)

    def lambda_47AC():
        OP_8E(0xFE, 0x7058, 0x0, 0x4434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47AC)
    Sleep(500)

    def lambda_47CC():
        OP_8E(0xFE, 0x6CF2, 0x0, 0x470E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_47CC)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #191
        0x101,
        "#580FWow, how'd it get to be so late?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)

    ChrTalk(    #192
        0x106,
        (
            "#552FBah... This is no good.\x02\x03",

            "How are we supposed to search\x01",
            "in the dark?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 16500, 6000, 10000, 0)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x106, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_48E0():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E0)

    def lambda_48EE():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48EE)

    def lambda_48FC():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_48FC)

    def lambda_490A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_490A)
    Sleep(500)

    ChrTalk(    #193
        0x106,
        "#052FHey, what was that sound?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x9, 0x80)

    def lambda_494B():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_494B)

    def lambda_495B():

        label("loc_495B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_495B")

    QueueWorkItem2(0x101, 1, lambda_495B)

    def lambda_496C():

        label("loc_496C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_496C")

    QueueWorkItem2(0x102, 1, lambda_496C)

    def lambda_497D():

        label("loc_497D")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_497D")

    QueueWorkItem2(0x106, 1, lambda_497D)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0x9, 0x105, 0x1388, 0x1F40, 0x0)
    OP_92(0x9, 0x105, 0xFA0, 0x1770, 0x0)
    OP_92(0x9, 0x105, 0xBB8, 0xFA0, 0x0)
    OP_92(0x9, 0x105, 0x7D0, 0x7D0, 0x0)
    OP_44(0x106, 0x1)
    OP_8C(0x106, 180, 0)
    OP_8E(0x9, 0x7292, 0x384, 0x41DC, 0x5DC, 0x0)
    OP_44(0x101, 0x1)
    OP_8C(0x101, 45, 0)

    def lambda_49F5():
        OP_8C(0xFE, 270, 200)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_49F5)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x105, 3)
    SetChrFlags(0x105, 0x20)
    OP_8C(0x105, 225, 200)
    OP_8F(0x9, 0x7224, 0x64, 0x42C2, 0x3E8, 0x0)
    WaitChrThread(0x9, 0x3)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x9, 0x80)
    SetChrSubChip(0x105, 1)
    SetChrFlags(0x105, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(    #194
        0x105,
        "#044FOh, Sieg. Where have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x106,
        "#055FWh-What the hell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#006F#4PThat's Sieg. He's Kloe's gyrfalcon\x01",
            "companion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x106,
        "#055FWhew... As long as he's friendly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x9,
        (
            "#310FScreeee!\x02\x03",

            "Scree, scree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x105,
        (
            "#047FUnderstood.\x02\x03",

            "#042FThank you, Sieg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        "#311FScree! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x106,
        (
            "#551FNow I've seen everything.\x02\x03",

            "#051FSo, missy. What did your friend\x01",
            "there tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x105,
        (
            "#042FThe whereabouts of the ruffians who\x01",
            "assaulted Theresa, evidently.\x02\x03",

            "It seems that he saw the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        "#051FHa ha ha! That's a good one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#006F#4PNice going, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#010F#6PYes, most impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        "#311FScree! ♪\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0x106,
        (
            "#055FNow wait one damn minute!\x02\x03",

            "You mean to tell me you actually\x01",
            "believe that load of bull?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#015F#6PWe've seen him communicate\x01",
            "several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#006F#4PHey, if you don't believe us,\x01",
            "you don't have to come along.\x02\x03",

            "Come on, guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x105,
        "#042FAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x9,
        "#310FScreee!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x105, 3)
    OP_8C(0x105, 270, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_4DFB():
        OP_8E(0xFE, 0x251C, 0x1770, 0x3584, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4DFB)
    Sleep(100)

    def lambda_4E1B():
        OP_8E(0xFE, 0x251C, 0x1770, 0x3584, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E1B)
    Sleep(100)

    def lambda_4E3B():

        label("loc_4E3B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4E3B")

    QueueWorkItem2(0x101, 1, lambda_4E3B)

    def lambda_4E4C():

        label("loc_4E4C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4E4C")

    QueueWorkItem2(0x102, 1, lambda_4E4C)
    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    def lambda_4E6C():
        OP_8E(0xFE, 0x251C, 0x1770, 0x3584, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E6C)
    Sleep(100)

    def lambda_4E8C():

        label("loc_4E8C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4E8C")

    QueueWorkItem2(0x106, 1, lambda_4E8C)

    def lambda_4E9D():
        OP_8E(0xFE, 0x251C, 0x1770, 0x3584, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E9D)
    Sleep(100)

    def lambda_4EBD():
        OP_8E(0xFE, 0x251C, 0x1770, 0x3584, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EBD)
    Sleep(500)
    OP_44(0x101, 0xFF)

    def lambda_4EE1():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EE1)
    Sleep(500)
    OP_44(0x102, 0xFF)

    def lambda_4F05():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F05)
    Sleep(100)

    def lambda_4F25():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F25)
    Sleep(1000)

    ChrTalk(    #212
        0x106,
        (
            "#055FUmm...\x02\x03",

            "#054FW-Wait up, you punks!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_62(0x106, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4F8E():
        OP_8E(0xFE, 0x2D64, 0xFBE, 0x3A84, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4F8E)
    OP_0D()
    OP_28(0x3E, 0x1, 0x2)
    OP_28(0x3E, 0x1, 0x4)
    OP_28(0x3E, 0x1, 0x8)
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/R2111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_46ED end

    def Function_18_4FCD(): pass

    label("Function_18_4FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50CE")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507C")
    OP_A2(0x6)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #213
        0x101,
        (
            "#000FHey, it's about noon, so why\x01",
            "don't we break for lunch?\x02\x03",

            "It'll just be a minute.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #214
        0x102,
        "#010FOkay. Let's find a place to eat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_50C7")

    label("loc_507C")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #215
        0x101,
        (
            "#000FIt'll just take a minute, so let's\x01",
            "find somewhere to eat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C7")

    Call(0, 19)
    Jump("loc_54ED")

    label("loc_50CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5151")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #216
        0x102,
        (
            "#010FThe highway is this way.\x02\x03",

            "I think the windmill outside of\x01",
            "town has a viewing platform on\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_54ED")

    label("loc_5151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A6")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F6")
    OP_A2(0x6)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #217
        0x102,
        (
            "#012FWait. We're not even sure where\x01",
            "that kid went.\x02\x03",

            "Let's figure out where he is first before\x01",
            "we start wandering aimlessly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529F")

    label("loc_51F6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #218
        0x102,
        (
            "#012FHold on a sec, Estelle. We still don't know\x01",
            "where that kid is.\x02\x03",

            "I think the best course of action now would\x01",
            "be to ask around town if anyone's seen him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529F")

    Call(0, 19)
    Jump("loc_54ED")

    label("loc_52A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_540D")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5331")

    ChrTalk(    #219
        0x106,
        (
            "#050FWe ain't got time to go back\x01",
            "to Ruan...\x02\x03",

            "Bah, whatever. I guess we'll\x01",
            "just have to bet on the bird.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5406")

    label("loc_5331")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #220
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",

            "We ain't got time to go back\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5395():
        TurnDirection(0x105, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5395)

    def lambda_53A3():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53A3)
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(    #221
        0x102,
        (
            "#012FIndeed.\x02\x03",

            "For now, let's just follow Sieg's\x01",
            "trail, and see where it leads.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5406")

    Call(0, 19)
    Jump("loc_54ED")

    label("loc_540D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54ED")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548E")

    ChrTalk(    #222
        0x106,
        (
            "#050FWe ain't got time to go back\x01",
            "to Ruan.\x02\x03",

            "Let's head back to the lighthouse\x01",
            "and settle this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54E9")

    label("loc_548E")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #223
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",

            "Let's head back to the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54E9")

    Call(0, 19)

    label("loc_54ED")

    Return()

    # Function_18_4FCD end

    def Function_19_54EE(): pass

    label("Function_19_54EE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_19_54EE end

    def Function_20_550A(): pass

    label("Function_20_550A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_558D")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #224
        0x102,
        (
            "#010FThe highway is this way.\x02\x03",

            "I think the windmill outside of\x01",
            "town has a viewing platform on\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_58DD")

    label("loc_558D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_568E")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5613")
    OP_A2(0x6)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #225
        0x102,
        (
            "#012FLet's figure out where that kid\x01",
            "went first.\x02\x03",

            "We can worry about following him\x01",
            "afterward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5687")

    label("loc_5613")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #226
        0x102,
        (
            "#012FLet's figure out where that kid\x01",
            "went first.\x02\x03",

            "From what the villagers said,\x01",
            "he was in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5687")

    Call(0, 21)
    Jump("loc_58DD")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583C")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_572E")

    ChrTalk(    #227
        0x101,
        (
            "#002FOops... This way leads to the\x01",
            "Krone Pass.\x02\x03",

            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5835")

    label("loc_572E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B6")

    ChrTalk(    #228
        0x102,
        (
            "#012FThe Manoria Byroad is this way.\x02\x03",

            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5835")

    label("loc_57B6")


    ChrTalk(    #229
        0x105,
        (
            "#042FThis way leads to the Manoria\x01",
            "Byroad.\x02\x03",

            "If we want to get back to Ruan,\x01",
            "we should use the east entrance\x01",
            "to the beach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5835")

    Call(0, 21)
    Jump("loc_58DD")

    label("loc_583C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58DD")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5860")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_5867")

    label("loc_5860")

    TurnDirection(0x102, 0x0, 400)

    label("loc_5867")


    ChrTalk(    #230
        0x102,
        (
            "#012FThe highway is this way.\x02\x03",

            "We have to find Matron Theresa first.\x01",
            "She's got to still be here, in Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)

    label("loc_58DD")

    Return()

    # Function_20_550A end

    def Function_21_58DE(): pass

    label("Function_21_58DE")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_21_58DE end

    def Function_22_58FA(): pass

    label("Function_22_58FA")

    SetPlaceName(0x58)
    Return()

    # Function_22_58FA end

    def Function_23_58FE(): pass

    label("Function_23_58FE")

    SetPlaceName(0x57)
    Return()

    # Function_23_58FE end

    def Function_24_5902(): pass

    label("Function_24_5902")

    SetPlaceName(0x59)
    Return()

    # Function_24_5902 end

    SaveToFile()

Try(main)
