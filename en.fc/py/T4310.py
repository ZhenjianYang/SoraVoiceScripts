from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4310   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Sergeant',                             # 13
        'Rianne',                               # 14
        'Sieg',                                 # 15
        'Nial',                                 # 16
        'Princess Klaudia',                     # 17
        '1st Lieutenant Schwarz',               # 18
        'Scherazard',                           # 19
        'Olivier',                              # 20
        'Carna',                                # 21
        'Anelace',                              # 22
        'Grant',                                # 23
        'Kurt',                                 # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Elder Noblewoman',                     # 31
        'Middle-Aged Nobleman',                 # 32
        'Noble Girl',                           # 33
        'Noble Boy',                            # 34
        'Middle-Aged Noblewoman',               # 35
        'Elder Nobleman',                       # 36
        'Noble Child',                          # 37
        'Scholar 2',                            # 38
        'Butler',                               # 39
        'Boy From Town',                        # 40
        ' ',                                    # 41
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT07/CH00510 ._CH',             # 08
        'ED6_DT07/CH01480 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT06/CH20143 ._CH',             # 0C
        'ED6_DT07/CH02090 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH00122 ._CH',             # 10
        'ED6_DT07/CH00514 ._CH',             # 11
        'ED6_DT07/CH00513 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01630 ._CH',             # 14
        'ED6_DT07/CH01260 ._CH',             # 15
        'ED6_DT07/CH01620 ._CH',             # 16
        'ED6_DT07/CH01320 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
        'ED6_DT06/CH20042 ._CH',             # 19
        'ED6_DT07/CH01180 ._CH',             # 1A
        'ED6_DT07/CH01200 ._CH',             # 1B
        'ED6_DT07/CH01210 ._CH',             # 1C
        'ED6_DT07/CH01220 ._CH',             # 1D
        'ED6_DT07/CH01230 ._CH',             # 1E
        'ED6_DT07/CH01490 ._CH',             # 1F
        'ED6_DT07/CH01470 ._CH',             # 20
        'ED6_DT07/CH01190 ._CH',             # 21
        'ED6_DT07/CH01560 ._CH',             # 22
        'ED6_DT07/CH01220 ._CH',             # 23
        'ED6_DT06/CH20113 ._CH',             # 24
        'ED6_DT07/CH00440 ._CH',             # 25
        'ED6_DT07/CH00441 ._CH',             # 26
        'ED6_DT07/CH01790 ._CH',             # 27
        'ED6_DT07/CH00500 ._CH',             # 28
        'ED6_DT07/CH00501 ._CH',             # 29
        'ED6_DT07/CH00444 ._CH',             # 2A
        'ED6_DT07/CH00443 ._CH',             # 2B
        'ED6_DT06/CH20114 ._CH',             # 2C
        'ED6_DT06/CH20115 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT07/CH00510P._CP',             # 08
        'ED6_DT07/CH01480P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT06/CH20143P._CP',             # 0C
        'ED6_DT07/CH02090P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH00122P._CP',             # 10
        'ED6_DT07/CH00514P._CP',             # 11
        'ED6_DT07/CH00513P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01630P._CP',             # 14
        'ED6_DT07/CH01260P._CP',             # 15
        'ED6_DT07/CH01620P._CP',             # 16
        'ED6_DT07/CH01320P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
        'ED6_DT06/CH20042P._CP',             # 19
        'ED6_DT07/CH01180P._CP',             # 1A
        'ED6_DT07/CH01200P._CP',             # 1B
        'ED6_DT07/CH01210P._CP',             # 1C
        'ED6_DT07/CH01220P._CP',             # 1D
        'ED6_DT07/CH01230P._CP',             # 1E
        'ED6_DT07/CH01490P._CP',             # 1F
        'ED6_DT07/CH01470P._CP',             # 20
        'ED6_DT07/CH01190P._CP',             # 21
        'ED6_DT07/CH01560P._CP',             # 22
        'ED6_DT07/CH01220P._CP',             # 23
        'ED6_DT06/CH20113P._CP',             # 24
        'ED6_DT07/CH00440P._CP',             # 25
        'ED6_DT07/CH00441P._CP',             # 26
        'ED6_DT07/CH01790P._CP',             # 27
        'ED6_DT07/CH00500P._CP',             # 28
        'ED6_DT07/CH00501P._CP',             # 29
        'ED6_DT07/CH00444P._CP',             # 2A
        'ED6_DT07/CH00443P._CP',             # 2B
        'ED6_DT06/CH20114P._CP',             # 2C
        'ED6_DT06/CH20115P._CP',             # 2D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 4420,
        Z                   = 250,
        Y                   = 72560,
        Direction           = 201,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5090,
        Z                   = 0,
        Y                   = 70990,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3560,
        Z                   = 250,
        Y                   = 71090,
        Direction           = 208,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4630,
        Z                   = 250,
        Y                   = 72900,
        Direction           = 165,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3480,
        Z                   = 250,
        Y                   = 72300,
        Direction           = 150,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4870,
        Z                   = 0,
        Y                   = 70280,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 66790,
        Direction           = 237,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6740,
        Z                   = 0,
        Y                   = 65120,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8300,
        Z                   = 0,
        Y                   = 63060,
        Direction           = 241,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6540,
        Z                   = 0,
        Y                   = 69410,
        Direction           = 239,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
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


    DeclEvent(
        X                   = -57400,
        Y                   = 1000,
        Z                   = 2550,
        Range               = -43640,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFCCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    ScpFunction(
        "Function_0_65A",          # 00, 0
        "Function_1_70A",          # 01, 1
        "Function_2_718",          # 02, 2
        "Function_3_72E",          # 03, 3
        "Function_4_D67",          # 04, 4
        "Function_5_1203",         # 05, 5
        "Function_6_142A",         # 06, 6
        "Function_7_443B",         # 07, 7
        "Function_8_4463",         # 08, 8
        "Function_9_4C67",         # 09, 9
    )


    def Function_0_65A(): pass

    label("Function_0_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_66D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_67B")
    OP_A3(0x3FB)
    Event(0, 8)

    label("loc_67B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_687"),
        (SWITCH_DEFAULT, "loc_69D"),
    )


    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69A")
    OP_A2(0x659)
    Event(0, 6)

    label("loc_69A")

    Jump("loc_69D")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_6F8")
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, -48300, 0, 18410, 90)
    SetChrPos(0x9, -48500, 0, 17000, 135)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)

    label("loc_6F8")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_65A end

    def Function_1_70A(): pass

    label("Function_1_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_1B(0x0, 0x0, 0x9)

    label("loc_717")

    Return()

    # Function_1_70A end

    def Function_2_718(): pass

    label("Function_2_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_718")

    label("loc_72D")

    Return()

    # Function_2_718 end

    def Function_3_72E(): pass

    label("Function_3_72E")

    EventBegin(0x0)
    OP_6D(19290, 0, 360, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(5020, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, 190, 0, -7530, 0)
    SetChrPos(0x101, -1330, 0, -8480, 0)
    SetChrPos(0x102, 570, 0, -8760, 0)
    FadeToBright(1000, 0)
    OP_6D(640, 0, -4630, 4000)
    Fade(1000)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#004FSo, this is the Erbe Royal Villa...\x02\x03",

            "It's gorgeous... Certainly gives\x01",
            "the castle a run for its mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#010FWell, it IS a royal family residence.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 11820, 0, -6220, 250)
    SetChrPos(0x9, 12550, 0, -5100, 250)
    SetChrPos(0xB, 14020, 0, -5780, 250)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x108, 100, 400)

    ChrTalk(    #2
        0x108,
        (
            "#5P#076FOops... Looks like the welcoming\x01",
            "committee's here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_947():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_947)

    def lambda_955():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_955)

    def lambda_963():
        OP_6D(6340, 0, -6950, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_963)

    def lambda_97B():
        OP_67(0, 4710, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97B)

    def lambda_993():
        OP_6C(68000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_993)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #3
        0x8,
        "Who are you people?!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFD44, 0x0, 0xFFFFE4F8, 0x1388, 0x0)
    OP_8E(0x101, 0x316, 0x0, 0xFFFFE82C, 0x1388, 0x0)
    OP_8C(0x101, 100, 0)

    ChrTalk(    #4
        0x101,
        (
            "#005F#5PYou don't need to know\x01",
            "our names!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#012F#5PWords will serve no purpose\x01",
            "here. Let's go!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A59():
        OP_6D(10400, 0, -6130, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A59)

    def lambda_A71():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A71)
    Sleep(50)

    def lambda_A8B():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8B)
    Sleep(50)

    def lambda_AA5():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_AA5)
    SetChrChipByIndex(0x8, 7)
    SetChrFlags(0x8, 0x1000)

    def lambda_AC4():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC4)
    Sleep(50)
    SetChrChipByIndex(0x9, 38)
    SetChrFlags(0x9, 0x1000)

    def lambda_AE8():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AE8)
    Sleep(50)
    SetChrChipByIndex(0xB, 38)
    SetChrFlags(0xB, 0x1000)

    def lambda_B0C():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B0C)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0xB, 0x1000)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_B6F"),
        (SWITCH_DEFAULT, "loc_B72"),
    )


    label("loc_B6F")

    OP_B4(0x0)
    Return()

    label("loc_B72")

    EventBegin(0x0)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0xB, 25)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrPos(0x8, 11700, 0, -9160, 176)
    SetChrPos(0x9, 12780, 0, -10830, 90)
    SetChrPos(0xB, 10700, 0, -11180, 296)
    OP_6D(10320, 0, -5900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 7960, 0, -6540, 90)
    SetChrPos(0x108, 9450, 0, -5900, 270)
    SetChrPos(0x102, 8270, 0, -5050, 90)
    FadeToBright(1000, 0)
    OP_6D(8640, 0, -5700, 1500)
    OP_0D()

    ChrTalk(    #6
        0x101,
        (
            "#002FNow, where's the princess\x01",
            "being held?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #7
        0x102,
        (
            "#012FThis place is huge.\x02\x03",

            "We'll just have to search it\x01",
            "room-by-room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x108,
        (
            "#072FIf we just hang around here,\x01",
            "you can bet we're going to\x01",
            "have more company, and soon.\x02\x03",

            "Let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_72E end

    def Function_4_D67(): pass

    label("Function_4_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_D6F")
    Return()

    label("loc_D6F")

    OP_A2(0x654)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52180, 0, 20500, 180)
    SetChrPos(0x9, -50170, 0, 20530, 180)
    SetChrChipByIndex(0x8, 39)
    SetChrChipByIndex(0x9, 39)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_DC7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_DC7)

    def lambda_DD5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD5)

    def lambda_DE3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE3)
    OP_6D(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, -50910, 0, 8080, 0)
    SetChrPos(0x102, -50140, 0, 6930, 0)
    SetChrPos(0x101, -52160, 0, 7020, 0)

    def lambda_E44():
        OP_8E(0xFE, 0xFFFF38C8, 0x0, 0x31EC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_E44)

    def lambda_E5F():
        OP_8E(0xFE, 0xFFFF34FE, 0x0, 0x2CF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5F)

    def lambda_E7A():
        OP_8E(0xFE, 0xFFFF3BDE, 0x0, 0x2E90, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7A)

    ChrTalk(    #9
        0x8,
        "#3PWho are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#3PWhy do you look so familiar?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 40)
    OP_0D()

    ChrTalk(    #11
        0x9,
        (
            "#3PH-Hey! You guys won the Martial\x01",
            "Arts Competition!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x8, 40)
    OP_0D()

    ChrTalk(    #12
        0x8,
        (
            "#3PThat means you're with the\x01",
            "Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        "#070F#2PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#006F#2PI don't suppose we could persuade\x01",
            "you to just forget you saw us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "#3PShut it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#3PWe're defenders of an impregnable\x01",
            "fortress. You want past us, you\x01",
            "have to go through us!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1051():
        OP_6D(-50570, 0, 20000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1051)
    SetChrChipByIndex(0x8, 41)

    def lambda_106E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_106E)
    Sleep(50)
    SetChrChipByIndex(0x8, 41)

    def lambda_108D():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_108D)

    def lambda_10A2():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_10A2)
    Sleep(50)

    def lambda_10C2():
        OP_92(0xFE, 0x8, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C2)
    Sleep(50)

    def lambda_10DC():
        OP_92(0xFE, 0x9, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10DC)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3AE, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_111D"),
        (SWITCH_DEFAULT, "loc_1120"),
    )


    label("loc_111D")

    OP_B4(0x0)
    Return()

    label("loc_1120")

    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x8, -48300, 0, 18410, 90)
    SetChrPos(0x9, -48500, 0, 17000, 135)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -50450, 0, 17110, 0)
    SetChrPos(0x108, -50450, 0, 17110, 0)
    SetChrPos(0x102, -50450, 0, 17110, 0)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x108, 0)
    OP_6D(-50450, 0, 17110, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_D67 end

    def Function_5_1203(): pass

    label("Function_5_1203")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139C")
    OP_A2(0x655)
    EventBegin(0x0)
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x1, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x2, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #18
        0x101,
        "#000FAwww, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FIt seems pretty solid, and the locking\x01",
            "mechanism is quite secure. We definitely\x01",
            "won't be able to get in without the key.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")

    ChrTalk(    #20
        0x108,
        (
            "#070FHm... I guess we'll have to\x01",
            "leave this place for later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1397")

    label("loc_134E")


    ChrTalk(    #21
        0x108,
        (
            "#070FHm... Maybe we should go talk\x01",
            "to that young chamberlain.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x8)

    label("loc_1397")

    EventEnd(0x1)
    Jump("loc_1424")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_13E9")
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_A2(0x658)
    OP_71(0x1, 0x10)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05Used Spare Key.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_64(0x0, 0x1)
    Jump("loc_1424")

    label("loc_13E9")

    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #23
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1424")

    ClearMapFlags(0x80)
    Return()

    # Function_5_1203 end

    def Function_6_142A(): pass

    label("Function_6_142A")

    EventBegin(0x0)
    OP_6D(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(57000, 0)
    OP_6E(500, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 50, 250, 68860, 180)
    SetChrPos(0xD, 6240, 0, 63940, 11)
    SetChrPos(0xF, 3070, 0, 58560, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -110, 0, 50960, 0)
    SetChrPos(0x102, -110, 0, 50960, 0)
    SetChrPos(0x108, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    SetChrPos(0x13, -110, 0, 50960, 0)
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0x12, -110, 0, 50960, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    def lambda_158A():

        label("loc_158A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_158A")

    QueueWorkItem2(0xD, 1, lambda_158A)

    def lambda_159B():

        label("loc_159B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_159B")

    QueueWorkItem2(0x1E, 1, lambda_159B)

    def lambda_15AC():

        label("loc_15AC")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15AC")

    QueueWorkItem2(0x1F, 1, lambda_15AC)

    def lambda_15BD():

        label("loc_15BD")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15BD")

    QueueWorkItem2(0x20, 1, lambda_15BD)

    def lambda_15CE():

        label("loc_15CE")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15CE")

    QueueWorkItem2(0x21, 1, lambda_15CE)

    def lambda_15DF():

        label("loc_15DF")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15DF")

    QueueWorkItem2(0x22, 1, lambda_15DF)

    def lambda_15F0():

        label("loc_15F0")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_15F0")

    QueueWorkItem2(0x23, 1, lambda_15F0)

    def lambda_1601():

        label("loc_1601")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1601")

    QueueWorkItem2(0x24, 1, lambda_1601)

    def lambda_1612():

        label("loc_1612")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1612")

    QueueWorkItem2(0x25, 1, lambda_1612)

    def lambda_1623():

        label("loc_1623")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1623")

    QueueWorkItem2(0x26, 1, lambda_1623)

    def lambda_1634():

        label("loc_1634")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1634")

    QueueWorkItem2(0x27, 1, lambda_1634)
    OP_1F(0x50, 0x12C)
    FadeToBright(1000, 0)

    def lambda_1654():
        OP_6D(750, 0, 56890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1654)

    def lambda_166C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_166C)

    def lambda_167E():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0xDFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_167E)
    Sleep(500)

    def lambda_169E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_169E)

    def lambda_16B0():
        OP_8E(0xFE, 0x302, 0x0, 0xDBEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16B0)
    Sleep(500)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_16E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_16E7)

    def lambda_16F9():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xDA34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_16F9)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 65535)

    def lambda_171E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_171E)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 65535)

    def lambda_1736():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1736)
    WaitChrThread(0x108, 0x1)
    SetChrChipByIndex(0x108, 65535)

    def lambda_174E():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_174E)
    WaitChrThread(0x101, 0x3)

    def lambda_1761():
        OP_6D(2460, 0, 58180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1761)
    TurnDirection(0xF, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #24
        0xF,
        "#143FY-You...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#006FYo!\x01",
            "We're here to save your bacon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#010FHello, Nial. You don't look in\x01",
            "too bad a shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xF,
        "#144FAre you serious?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x10,
        "Girl's Voice",
        "Estelle... Joshua...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x10,
        "Girl's Voice",
        (
            "I never thought I'd see\x01",
            "you here...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_187A():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_187A)
    Sleep(100)

    def lambda_188D():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_188D)
    Sleep(100)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #30
        0x101,
        "#2P#004F...Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_18BC():
        OP_6D(70, 250, 68760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18BC)

    def lambda_18D4():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18D4)

    def lambda_18EC():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18EC)
    Sleep(1500)

    def lambda_1901():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x1041E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1901)
    Sleep(100)

    def lambda_1921():
        OP_8E(0xFE, 0x1EA, 0x0, 0x1041E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1921)
    Sleep(300)

    def lambda_1941():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0x10266, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1941)
    Sleep(100)

    def lambda_1961():
        OP_8E(0xFE, 0x8AC, 0x0, 0x10568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1961)

    def lambda_197C():

        label("loc_197C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_197C")

    QueueWorkItem2(0x101, 0, lambda_197C)

    def lambda_198D():

        label("loc_198D")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_198D")

    QueueWorkItem2(0x102, 0, lambda_198D)

    def lambda_199E():

        label("loc_199E")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_199E")

    QueueWorkItem2(0x108, 1, lambda_199E)

    def lambda_19AF():

        label("loc_19AF")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_19AF")

    QueueWorkItem2(0xF, 1, lambda_19AF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #31
        0x101,
        (
            "#6P#501FY-You're the princess.\x02\x03",

            "#001FIt's a pleasure to meet you.\x01",
            "We're with the...Bracer...Guild...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #32
        0x10,
        "Girl in Dress",
        (
            "#406FI think it's a little late\x01",
            "for introductions.\x02\x03",

            "#401FSo, we meet again,\x01",
            "as promised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#6P#505FErr...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#6P#004F#3SKLOE!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(    #35
        0x10,
        "Kloe",
        (
            "#405FEstelle...\x02\x03",

            "I sincerely hope you're joking.\x01",
            "You ought to have recognized\x01",
            "me sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#6P#506FBut not with the dress, and\x01",
            "the hair, and the things...!\x02\x03",

            "#501FWhat happened?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#6P#017FPardon us, Kloe.\x02\x03",

            "Estelle doesn't know how\x01",
            "to doubt people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#6P#509FHey! What the hell's that\x01",
            "supposed to mean?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x10,
        "Kloe",
        (
            "#466FHa ha...\x01",
            "There's the Estelle I know.\x02\x03",

            "#401FAnd, Joshua...?\x02\x03",

            "You'll still use that name\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#6P#010FYes, since it seems to be\x01",
            "the one you'd prefer.\x02\x03",

            "Would you rather I use your\x01",
            "real name?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x10,
        "Kloe",
        (
            "#408FNo... But thank you.\x01",
            "I'm glad to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#6P#505F???\x02\x03",

            "Okay, so what are you\x01",
            "doing here, Kloe?\x02\x03",

            "And for that matter, why isn't\x01",
            "the princess here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "#145FUhh...\x01",
            "She's right in front of you.\x02\x03",

            "That's the queen's granddaughter,\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#6P#501F...Buh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_20(0x7D0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xD, 0x0)

    def lambda_1E52():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E52)
    OP_6C(45000, 1500)
    Sleep(500)
    OP_63(0x101)
    Sleep(400)

    ChrTalk(    #45
        0x101,
        "#005F#5S#2PAAAAAAAAAAAH!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_6E(480, 0)
    OP_44(0x108, 0xFF)
    OP_44(0xF, 0xFF)
    CloseMessageWindow()
    OP_1D(0x11)

    NpcTalk(    #46
        0x10,
        "Princess Klaudia",
        (
            "#466FI'm sorry that I couldn't\x01",
            "tell you...\x02\x03",

            "#405FI had planned to tell both of\x01",
            "you the truth when we next met\x01",
            "in Grancel...\x02\x03",

            "But then Colonel Richard had\x01",
            "me 'detained'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#580FUhh...but why?\x02\x03",

            "Why would the princess be hiding\x01",
            "out in an ordinary school...?!\x02\x03",

            "And why did you have us\x01",
            "call you 'Kloe'...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x10,
        "Princess Klaudia",
        (
            "#406FI'd like for you to keep\x01",
            "calling me that.\x02\x03",

            "My real name is Klaudia von Auslese...\x02\x03",

            "#401FKloe is a pet name that Jill\x01",
            "came up with using bits from\x01",
            "my whole name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#008FReally...\x02\x03",

            "Uh, then what about your hair?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #50
        0x10,
        "Princess Klaudia",
        (
            "#400FOh, this is just a wig.\x02\x03",

            "If I had the same hairdo as when\x01",
            "I was on campus, it would probably\x01",
            "just create trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "#141FCan't believe I missed the\x01",
            "connection myself.\x02\x03",

            "I've seen your picture often enough, and\x01",
            "I remember you from the mayoral scandal in\x01",
            "Ruan, but I never put two and two together...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x10,
        "Princess Klaudia",
        (
            "#466FHa ha... I'm sorry.\x02\x03",

            "It doesn't seem that Uncle Dunan\x01",
            "or Mayor Dalmore recognized me,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#007FOh, yeah...and the duke's even\x01",
            "related to you.\x02\x03",

            "#004FOh! I forgot something important.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "\x07\x05Estelle explained the whole story, including how they had come to rescue\x01",
            "Kloe at the queen's behest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #55
        0x10,
        "Princess Klaudia",
        (
            "#404FI see...\x02\x03",

            "#403FTo all three of you...\x02\x03",

            "#406FI extend my deepest gratitude\x01",
            "for coming to rescue me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#001FAw, it was nothing.\x02\x03",

            "Heck, if we'd known that it was \x01",
            "our Kloe in here, no one would've\x01",
            "had to ask us!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #57
        0x10,
        "Princess Klaudia",
        "#405FE-Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#019FHa ha... No doubt.\x02\x03",

            "#010FYou should save your thanks for\x01",
            "Her Majesty, as she's the one\x01",
            "who deserves them.\x02\x03",

            "She had no concern for herself...\x01",
            "just that we should save you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x108,
        (
            "#074FI think your safety will give\x01",
            "her the strength to resist the\x01",
            "colonel's demands.\x02\x03",

            "#072FThough doing so may endanger\x01",
            "her life...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x108, 400)

    NpcTalk(    #60
        0x10,
        "Princess Klaudia",
        (
            "#403FYes...\x01",
            "That is her way.\x02\x03",

            "If something is not done, then\x01",
            "she is in grave danger...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -230, 0, 55310, 346)
    SetChrChipByIndex(0x8, 37)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xC, 1020, 0, 56140, 0)
    SetChrPos(0x8, 50, 0, 54770, 0)
    OP_20(0x5DC)

    NpcTalk(    #61
        0xC,
        "Man's Voice",
        "#1PI think I've seen enough of this little farce.\x02",
    )

    CloseMessageWindow()
    OP_21()

    def lambda_2707():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2707)

    def lambda_2715():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2715)

    def lambda_2723():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2723)

    def lambda_2731():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2731)

    def lambda_273F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_273F)

    def lambda_274D():
        OP_6D(680, 0, 60840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_274D)

    def lambda_2765():
        OP_6E(500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2765)
    Sleep(500)
    OP_1D(0x56)
    Sleep(1500)

    ChrTalk(    #62
        0xD,
        "#2PP-Princess...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #63
        0x10,
        "Princess Klaudia",
        "#407FRianne!\x02",
    )

    CloseMessageWindow()

    def lambda_27BA():
        OP_6D(850, 0, 60760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27BA)

    def lambda_27D2():
        OP_6E(450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_27D2)
    SetChrChipByIndex(0x101, 0)

    def lambda_27E7():
        OP_8E(0xFE, 0xFFFFFDEE, 0x0, 0xEF4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27E7)
    Sleep(200)
    SetChrChipByIndex(0x102, 2)

    def lambda_280C():
        OP_8E(0xFE, 0x258, 0x0, 0xF19A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_280C)
    Sleep(100)
    SetChrChipByIndex(0x108, 4)

    def lambda_2831():
        OP_8E(0xFE, 0xFFFFF754, 0x0, 0xF1B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2831)
    Sleep(200)

    def lambda_2851():
        OP_8E(0xFE, 0xA, 0x0, 0xF820, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2851)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #64
        0x101,
        "#580FWhat the--?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    NpcTalk(    #65
        0x10,
        "Princess Klaudia",
        (
            "#403FShe's General Morgan's granddaughter...\x02\x03",

            "He's imprisoned at the Haken Gate.\x01",
            "I'd say they're taking her to keep\x01",
            "him from causing any trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#012FJust as they did with you\x01",
            "and Her Majesty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xC,
        "#2PThis isn't just some idle threat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xC,
        (
            "#2PEvery man in the Special Ops\x01",
            "has a dream, and we will stop\x01",
            "at NOTHING to achieve it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#005FAnd that's something you're\x01",
            "PROUD of?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #70
        0x10,
        "Princess Klaudia",
        (
            "#402FI'll make you a deal, Sergeant.\x02\x03",

            "Please, take me as your hostage,\x01",
            "rather than the child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xC,
        "#2PHa... Not a chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xC,
        (
            "#2PI know I said we'll stop at nothing, but even\x01",
            "we don't have the nerve to harm a member of the\x01",
            "royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xC,
        (
            "#2PGeneral Morgan's grandkid, on the other hand,\x01",
            "suits our needs just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xC,
        (
            "#2PShe's a valuable hostage, and it's not going to\x01",
            "cause any real problems if she was to end up\x01",
            "getting hurt.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x10,
        "Princess Klaudia",
        "#407FYou're a monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#509FI'd have said 'coward,' myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#075FPathetic, disgusting, sick...\x01",
            "Pick an adjective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        "#2PHeh. You can talk all you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "#2PIt's almost time for the patrols to\x01",
            "return from the Royal Avenue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xC,
        (
            "#2PThen we can round up the Guardsmen\x01",
            "and the bracers. Not bad for one\x01",
            "night's work!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0x12,
        "Woman's Voice",
        (
            "#1POh, I'm afraid that won't\x01",
            "be happening.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x12,
        "Woman's Voice",
        (
            "#1PWe already took your buddies\x01",
            "out on our way over here.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2DF8():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DF8)

    def lambda_2E06():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E06)

    def lambda_2E14():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E14)

    def lambda_2E22():
        OP_6D(500, 0, 59390, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E22)
    OP_6E(500, 800)

    def lambda_2E43():

        label("loc_2E43")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E43")

    QueueWorkItem2(0xC, 1, lambda_2E43)

    def lambda_2E54():

        label("loc_2E54")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E54")

    QueueWorkItem2(0x8, 1, lambda_2E54)

    def lambda_2E65():

        label("loc_2E65")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2E65")

    QueueWorkItem2(0xD, 1, lambda_2E65)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0x12, 0x20)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 16)
    ClearChrFlags(0x12, 0x80)
    OP_1D(0x2F)

    def lambda_2E9C():

        label("loc_2E9C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2E9C")

    QueueWorkItem2(0x12, 1, lambda_2E9C)
    OP_96(0x12, 0xFFFFF7A4, 0x0, 0xD5C0, 0x3E8, 0x1F40)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x12, 0x2, 0x4, 0xBB8)
    PlayEffect(0x8, 0xFF, 0xFF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x8, 0x12, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 43)

    def lambda_2F1E():
        OP_94(0x1, 0xFE, 0xB4, 0xBB8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F1E)
    OP_99(0x12, 0x4, 0x9, 0xBB8)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(    #83 op#A op#5
        0x8,
        "#2P#10AAgh!\x05\x02",
    )

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 42)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_2F65():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F65)
    Sleep(500)

    def lambda_2F7A():
        OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xD912, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F7A)
    Sleep(100)
    OP_8F(0xC, 0x6CC, 0x0, 0xDACA, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_96(0x12, 0xFFFFF858, 0x0, 0xDA16, 0x1F4, 0x1F40)
    TurnDirection(0xD, 0x12, 400)
    Sleep(200)

    ChrTalk(    #84
        0xC,
        "#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xD,
        "#1P*sniffle*...\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #86
        0xD,
        "#3S#1PWAAAAAAHHHH!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_3039():

        label("loc_3039")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_3039")

    QueueWorkItem2(0x101, 1, lambda_3039)

    def lambda_304A():

        label("loc_304A")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_304A")

    QueueWorkItem2(0x102, 1, lambda_304A)

    def lambda_305B():

        label("loc_305B")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_305B")

    QueueWorkItem2(0x108, 1, lambda_305B)

    def lambda_306C():

        label("loc_306C")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_306C")

    QueueWorkItem2(0xF, 1, lambda_306C)

    def lambda_307D():

        label("loc_307D")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_307D")

    QueueWorkItem2(0x10, 1, lambda_307D)

    ChrTalk(    #87
        0x12,
        (
            "#021F#5PThere, there...\x01",
            "It's all right...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x12, 0xFF)
    OP_8C(0x12, 45, 400)

    ChrTalk(    #88
        0x12,
        (
            "#020FHi, you two.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#004FSch-Schera?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#014FYou came...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "#2PDamn it all... Who the hell\x01",
            "do you think you are?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #92
        0x13,
        "Young Man's Voice",
        (
            "#1P*sigh*... Some people just\x01",
            "have no manners.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp008_00.eff")
    SetChrPos(0x28, 1590, 1000, 54930, 0)
    PlayEffect(0x0, 0xFF, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x28, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x8, 0xFF, 0xFF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 18)

    def lambda_3243():
        OP_96(0xFE, 0xBD6, 0x0, 0xDFFC, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3243)

    ChrTalk(    #93 op#A op#5
        0xC,
        "#10AGah...\x05\x02",
    )

    Sleep(400)

    def lambda_3276():

        label("loc_3276")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3276")

    QueueWorkItem2(0x12, 1, lambda_3276)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x12, 90, 0)

    def lambda_3299():
        OP_96(0xFE, 0x442, 0x0, 0xDDCC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3299)
    Sleep(200)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x12, 0x2, 0x4, 0xFA0)
    PlayEffect(0x8, 0xFF, 0xFF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x4)

    def lambda_3304():
        OP_6D(6320, 0, 57730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3304)

    def lambda_331C():
        OP_8F(0xFE, 0x2508, 0x1F4, 0xDCE6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_331C)
    OP_99(0x12, 0x4, 0x9, 0x7D0)
    WaitChrThread(0xC, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 17)

    ChrTalk(    #94 op#A op#5
        0xC,
        "#10AOOF!\x05\x02",
    )

    PlayEffect(0x12, 0xFF, 0xC, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6B(1800, 0)
    OP_6B(1760, 80)
    Sleep(500)
    OP_8F(0xC, 0x2512, 0x0, 0xDCE6, 0x3E8, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xC, 0x0, 0x3, 0x7D0)

    ChrTalk(    #95
        0x12,
        "#027F#5PThink of that as my special gift.\x02",
    )

    CloseMessageWindow()
    OP_6D(280, 0, 59100, 2000)

    ChrTalk(    #96
        0x101,
        (
            "#509FThat's just cruel...\x02\x03",

            "#004FHey, who fired that shot...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#014F...Olivier, I'd guess.\x02",
    )

    CloseMessageWindow()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 14)
    TurnDirection(0x12, 0x13, 400)
    OP_22(0xA6, 0x0, 0x64)

    NpcTalk(    #98
        0x13,
        "Young Man's Voice",
        "#1PBingo! ♪\x02",
    )

    CloseMessageWindow()

    def lambda_34B9():

        label("loc_34B9")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34B9")

    QueueWorkItem2(0x12, 1, lambda_34B9)

    def lambda_34CA():

        label("loc_34CA")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34CA")

    QueueWorkItem2(0xD, 1, lambda_34CA)

    def lambda_34DB():

        label("loc_34DB")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34DB")

    QueueWorkItem2(0x101, 1, lambda_34DB)

    def lambda_34EC():

        label("loc_34EC")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34EC")

    QueueWorkItem2(0x102, 1, lambda_34EC)

    def lambda_34FD():

        label("loc_34FD")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_34FD")

    QueueWorkItem2(0x108, 1, lambda_34FD)

    def lambda_350E():

        label("loc_350E")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_350E")

    QueueWorkItem2(0xF, 1, lambda_350E)

    def lambda_351F():

        label("loc_351F")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_351F")

    QueueWorkItem2(0x10, 1, lambda_351F)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3540():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3540)

    def lambda_3552():
        OP_8E(0xFE, 0x1E, 0x0, 0xD7F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3552)
    Sleep(100)
    OP_6D(550, 0, 58110, 2000)

    ChrTalk(    #99
        0x13,
        (
            "#031FAnd the star makes his dramatic entrance!\x01",
            "Please, hold your applause until after\x01",
            "the performance has ended...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)

    def lambda_3600():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xDF34, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3600)
    Sleep(200)
    SetChrChipByIndex(0x102, 65535)

    def lambda_3625():
        OP_8E(0xFE, 0xF0, 0x0, 0xE2C2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3625)
    Sleep(200)
    SetChrChipByIndex(0x108, 65535)

    def lambda_364A():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xE25E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_364A)
    Sleep(300)

    def lambda_366A():
        OP_8E(0xFE, 0x78, 0x0, 0xE90C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_366A)
    Sleep(200)

    def lambda_368A():
        OP_8E(0xFE, 0x9A6, 0x0, 0xE902, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_368A)
    OP_44(0x12, 0xFF)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x11)

    ChrTalk(    #100
        0x108,
        (
            "#3P#071FHa ha... And the drama turns\x01",
            "into a comedy!\x02\x03",

            "#070FNice seeing you again, Scherazard.\x01",
            "It's been a long time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 400)

    ChrTalk(    #101
        0x12,
        (
            "#021F#4PIndeed, it has.\x02\x03",

            "#020FI never thought I'd find you in Liberl.\x02\x03",

            "But I was honestly quite relieved\x01",
            "when I heard that you'd fallen in\x01",
            "with Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x108,
        (
            "#3P#070FHa ha. Well, I think you're over-\x01",
            "estimating my capabilities...\x01",
            "like usual.\x02\x03",

            "#071FAs for you...you've only become\x01",
            "more beautiful.\x02\x03",

            "I barely even recognized you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        "#520F#4PO-Oh...really?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 400)
    Sleep(200)
    TurnDirection(0x13, 0x108, 400)
    Sleep(200)
    TurnDirection(0x13, 0x12, 400)

    ChrTalk(    #104
        0x13,
        (
            "#032FHmmm... I am suddenly brimming over\x01",
            "with something akin to jealousy.\x02\x03",

            "#034FAm I merely a toy, to be used\x01",
            "when convenient, and cast aside\x01",
            "when boredom sets in?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(    #105
        0x12,
        (
            "#027F#4PHey, Olivier. Aina's been wanting\x01",
            "to see you.\x02\x03",

            "She's hoping to go out for\x01",
            "drinks again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(    #106
        0x13,
        (
            "#034FForgive me. I have committed\x01",
            "a grave offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#6P#506FI swear...\x01",
            "None of you ever change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        (
            "#014FI'm glad to see you, Schera.\x02\x03",

            "But I thought that the Royal\x01",
            "Army had the checkpoints\x01",
            "completely sealed off...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)

    def lambda_3AC3():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AC3)
    TurnDirection(0x12, 0x102, 400)

    ChrTalk(    #109
        0x12,
        (
            "#021F#4PYes...but we crossed Valleria\x01",
            "Lake by boat.\x02\x03",

            "And docked at Grancel Harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#010FThat's one way around a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#6P#505FBut how did you wind up falling\x01",
            "in with the failed...excuse me,\x01",
            "'Traveling'...musician?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3BC0)

    ChrTalk(    #112
        0x12,
        (
            "#025F#4PWe ran into each other at the\x01",
            "local guild branch.\x02\x03",

            "He was like a lost puppy, so I\x01",
            "didn't have much choice other\x01",
            "than to bring him along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x13,
        (
            "#031FHa ha ha...\x02\x03",

            "I simply couldn't allow such an\x01",
            "amusing and interesting show\x01",
            "to go on without me...\x02\x03",

            "#030FAnd may I ask who this\x01",
            "fair lady is?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)

    def lambda_3D02():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3D02)
    OP_8E(0x102, 0x3AC, 0x0, 0xE36C, 0x7D0, 0x0)
    TurnDirection(0x102, 0x10, 400)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #114
        0x101,
        (
            "#6P#006FOh, right. Introductions.\x02\x03",

            "This is the queen's granddaughter,\x01",
            "Her Highness Princess Klaudia.\x02\x03",

            "She's a friend of ours.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DB5():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DB5)

    def lambda_3DC3():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DC3)
    OP_44(0x10, 0xFF)

    NpcTalk(    #115
        0x10,
        "Princess Klaudia",
        (
            "#401FIt is a pleasure to meet\x01",
            "you both.\x02\x03",

            "Thank you very much for\x01",
            "coming to help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x12,
        (
            "#021F#4PThink nothing of it. I'm simply\x01",
            "doing my duty as a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x13,
        (
            "#035FAnd I could scarcely consider myself\x01",
            "a gentleman if I did not leap to the\x01",
            "aid of a lovely lady of noble birth.\x02\x03",

            "#030FThe honor and pleasure at this\x01",
            "meeting is entirely my own.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #118
        0x11,
        "Woman's Voice",
        "#1PYour Highness! Are you well?\x02",
    )

    CloseMessageWindow()

    def lambda_3FAC():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3FAC)

    def lambda_3FBA():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FBA)

    def lambda_3FC8():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FC8)

    def lambda_3FD6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3FD6)

    def lambda_3FE4():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3FE4)

    def lambda_3FF2():
        OP_8F(0xFE, 0x4A6, 0x0, 0xD9EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3FF2)

    def lambda_400D():
        OP_8F(0xFE, 0xFFFFF948, 0x0, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_400D)
    Sleep(500)

    def lambda_402D():

        label("loc_402D")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_402D")

    QueueWorkItem2(0x101, 1, lambda_402D)

    def lambda_403E():

        label("loc_403E")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_403E")

    QueueWorkItem2(0x102, 1, lambda_403E)

    def lambda_404F():

        label("loc_404F")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_404F")

    QueueWorkItem2(0x108, 1, lambda_404F)

    def lambda_4060():

        label("loc_4060")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_4060")

    QueueWorkItem2(0x13, 1, lambda_4060)

    def lambda_4071():

        label("loc_4071")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_4071")

    QueueWorkItem2(0x12, 1, lambda_4071)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x1000)
    SetChrChipByIndex(0x11, 44)

    def lambda_4091():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4091)

    def lambda_40A3():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xDF7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_40A3)
    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x4)

    def lambda_40D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_40D7)

    def lambda_40E9():
        OP_8E(0xFE, 0x33E, 0x0, 0xE8C6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_40E9)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 45)
    SetChrSubChip(0x11, 2)
    WaitChrThread(0xE, 0x1)
    OP_43(0xE, 0x1, 0x0, 0x7)
    OP_A2(0x0)

    NpcTalk(    #119
        0x10,
        "Princess Klaudia",
        "#409FJulia...! Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xE,
        "#2PScree!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A5(0x0)
    OP_97(0xE, 0x82, 0xE8C6, 0xFFFEA070, 0x1388, 0x1)
    OP_97(0xE, 0x82, 0xE8C6, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0xE, 0x20)

    def lambda_4191():

        label("loc_4191")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_4191")

    QueueWorkItem2(0xE, 2, lambda_4191)

    def lambda_41A4():
        OP_8F(0xFE, 0xFFFFFD26, 0x258, 0xE0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_41A4)
    OP_8C(0xE, 45, 100)
    WaitChrThread(0xE, 0x1)

    def lambda_41CB():
        OP_8F(0xFE, 0xFFFFFD26, 0x0, 0xE0C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_41CB)
    WaitChrThread(0xE, 0x1)
    OP_44(0xE, 0x2)
    Fade(500)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 36)
    SetChrSubChip(0x11, 1)
    OP_0D()

    ChrTalk(    #121
        0xE,
        (
            "#311F#6PScreescree!\x02\x03",

            "Screeeeeeee!!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #122
        0x10,
        "Princess Klaudia",
        (
            "#408FHa ha, good. I'm happy to\x01",
            "see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        (
            "#171F#4PThank goodness you're unharmed...\x02\x03",

            "I was so worried...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #124
        0x10,
        "Princess Klaudia",
        "#401FThe feeling is mutual.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #125
        (
            "\x07\x05Before long, the bracers involved in the diversion and the Royal Guardsmen\x01",
            "joined forces.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #126
        (
            "\x07\x05After seeing to it that the rescued hostages could get some rest, Estelle\x01",
            "and company gathered to assess their current situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_28(0x4B, 0x4, 0x10)
    OP_28(0x4C, 0x4, 0x10)
    OP_28(0x4C, 0x1, 0x40)
    OP_28(0x4C, 0x1, 0x80)
    OP_28(0x4C, 0x1, 0x100)
    OP_28(0x4D, 0x4, 0x2)
    OP_28(0x4D, 0x4, 0x4)
    OP_28(0x4D, 0x1, 0x1)
    OP_28(0x4D, 0x1, 0x2)
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_142A end

    def Function_7_443B(): pass

    label("Function_7_443B")

    OP_A6(0x0)

    label("loc_443E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445F")
    OP_97(0xFE, 0x82, 0xE8C6, 0xFFFA81C0, 0x1388, 0x1)
    OP_48()
    Jump("loc_443E")

    label("loc_445F")

    OP_A3(0x0)
    Return()

    # Function_7_443B end

    def Function_8_4463(): pass

    label("Function_8_4463")

    EventBegin(0x0)
    OP_6D(1040, 130, 67720, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -40, 250, 70880, 180)
    SetChrPos(0x102, -2410, 0, 67020, 45)
    SetChrPos(0x13, -3610, 0, 67070, 61)
    SetChrPos(0x108, -3890, 0, 68290, 80)
    SetChrPos(0x101, 2540, 0, 67490, 320)
    SetChrPos(0x10, 1280, 0, 67070, 2)
    SetChrPos(0x12, 2980, 0, 66110, 297)
    SetChrPos(0x14, -730, 0, 65269, 0)
    SetChrPos(0x16, 180, 0, 64510, 0)
    SetChrPos(0x15, -950, 0, 63940, 0)
    SetChrPos(0x17, -2170, 0, 64410, 0)
    SetChrPos(0x18, -1770, 0, 61620, 0)
    SetChrPos(0x18, 70, 0, 61620, 0)
    SetChrPos(0x18, 1840, 0, 61620, 0)
    SetChrPos(0x18, -1770, 0, 59790, 0)
    SetChrPos(0x18, 70, 0, 59790, 0)
    SetChrPos(0x18, 1840, 0, 59790, 0)
    SetChrChipByIndex(0x10, 24)

    ChrTalk(    #127
        0x11,
        (
            "#170FOkay, here's how we're going to\x01",
            "free Grancel Castle and the queen.\x02\x03",

            "First, Joshua and two others will\x01",
            "infiltrate the Grancel Sewers.\x02\x03",

            "You'll proceed to the Royal Guard\x01",
            "Room and open the castle gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#010FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x108,
        "#070FTime to light a few fireworks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x13,
        (
            "#030FHa ha... Well, it does seem\x01",
            "appropriate for the beginning\x01",
            "of the final act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        (
            "#170FAs soon as the gates are open, the Guardsmen\x01",
            "and four of the bracers will make their way\x01",
            "to the castle by way of the streets.\x02\x03",

            "We need to make a real spectacle\x01",
            "to draw all of the guards together\x01",
            "in one place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        "#840FYou're in good hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x16,
        (
            "#821FAll right! I've been looking\x01",
            "forward to this!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #134
        0x11,
        (
            "#170FAnd finally...\x02\x03",

            "Your Highness, are you certain\x01",
            "I cannot get you to reconsider?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10,
        (
            "#040FI'm sorry...but I must be there\x01",
            "to help my grandmother.\x02\x03",

            "Also, I know how to pilot\x01",
            "an airship...\x02\x03",

            "I hope to be able to put\x01",
            "that skill to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        (
            "#170F...\x02\x03",

            "If I'd known this would happen,\x01",
            "I never would have taught you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#000FIt's okay, Lieutenant.\x02\x03",

            "We'll look after Kloe for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x12,
        (
            "#020FI swear she will be kept safe or\x01",
            "my nickname isn't the Silver Streak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x11,
        (
            "#170FI understand...\x01",
            "Please, do what you can.\x02\x03",

            "Once the men inside the castle have been\x01",
            "concentrated into one area, Estelle and her\x01",
            "team will set down in the Garden Terrace.\x02\x03",

            "Then, they will break into the\x01",
            "queen's room and rescue her.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #140
        0x11,
        (
            "#170FBoth operations will begin at the\x01",
            "stroke of the noon bell. Everyone\x01",
            "is to remain on alert until then.\x02\x03",

            "All right, you have your tasks.\x01",
            "Get to them! Dismissed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x18,
        "Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_4463 end

    def Function_9_4C67(): pass

    label("Function_9_4C67")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD3")

    ChrTalk(    #142
        0x101,
        (
            "#002FWe still haven't completed\x01",
            "Her Majesty's request.\x02\x03",

            "We have to find the princess!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAE")

    label("loc_4CD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3E")

    ChrTalk(    #143
        0x102,
        (
            "#012FWe can leave once we set\x01",
            "the hostages free.\x02\x03",

            "We still haven't found\x01",
            "the princess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAE")

    label("loc_4D3E")


    ChrTalk(    #144
        0x108,
        (
            "#072FWe still haven't found\x01",
            "the princess.\x02\x03",

            "Until then, we have to take out\x01",
            "every single enemy around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAE")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_4C67 end

    SaveToFile()

Try(main)
