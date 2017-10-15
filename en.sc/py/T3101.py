from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Priam',                                # 9
        'Irene',                                # 10
        'Rehmann',                              # 11
        'Gundolf',                              # 12
        'Elise',                                # 13
        'Vince',                                # 14
        'Ray',                                  # 15
        'Factory Chief Murdock',                # 16
        'Maintenance Chief Gustav',             # 17
        'Citizen',                              # 18
        'Citizen',                              # 19
        'Citizen',                              # 20
        'Citizen',                              # 21
        'Citizen',                              # 22
        'Citizen',                              # 23
        'Citizen',                              # 24
        'Citizen',                              # 25
        'Citizen',                              # 26
        'Citizen',                              # 27
        'Citizen',                              # 28
        'Citizen',                              # 29
        'Citizen',                              # 30
        'Citizen',                              # 31
        'Citizen',                              # 32
        'Citizen',                              # 33
        'Citizen',                              # 34
        'Citizen',                              # 35
        'Citizen',                              # 36
        'Citizen',                              # 37
        'Citizen',                              # 38
        'Citizen',                              # 39
        'Citizen',                              # 40
        'Citizen',                              # 41
        'Citizen',                              # 42
        ' ',                                    # 43
        'Stain',                                # 44
        'Constance',                            # 45
        'Zeiss Landing Port',                   # 46
        'Zeiss - City Block',                   # 47
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01750 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01470 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH02620 ._CH',             # 07
        'ED6_DT07/CH02440 ._CH',             # 08
        'ED6_DT07/CH01100 ._CH',             # 09
        'ED6_DT07/CH01110 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01290 ._CH',             # 0E
        'ED6_DT07/CH01160 ._CH',             # 0F
        'ED6_DT07/CH01170 ._CH',             # 10
        'ED6_DT07/CH01180 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01250 ._CH',             # 13
        'ED6_DT07/CH01270 ._CH',             # 14
        'ED6_DT07/CH01290 ._CH',             # 15
        'ED6_DT07/CH01680 ._CH',             # 16
        'ED6_DT07/CH01690 ._CH',             # 17
        'ED6_DT07/CH01200 ._CH',             # 18
        'ED6_DT07/CH01230 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01750P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01470P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH02620P._CP',             # 07
        'ED6_DT07/CH02440P._CP',             # 08
        'ED6_DT07/CH01100P._CP',             # 09
        'ED6_DT07/CH01110P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01290P._CP',             # 0E
        'ED6_DT07/CH01160P._CP',             # 0F
        'ED6_DT07/CH01170P._CP',             # 10
        'ED6_DT07/CH01180P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01250P._CP',             # 13
        'ED6_DT07/CH01270P._CP',             # 14
        'ED6_DT07/CH01290P._CP',             # 15
        'ED6_DT07/CH01680P._CP',             # 16
        'ED6_DT07/CH01690P._CP',             # 17
        'ED6_DT07/CH01200P._CP',             # 18
        'ED6_DT07/CH01230P._CP',             # 19
    )

    DeclNpc(
        X                   = -26340,
        Z                   = 8000,
        Y                   = 65489,
        Direction           = 74,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -18800,
        Z                   = 8000,
        Y                   = 64430,
        Direction           = 164,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -24430,
        Z                   = 8000,
        Y                   = 68160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24460,
        Z                   = 8000,
        Y                   = 67320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -14900,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -16239,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -19310,
        Z                   = 8000,
        Y                   = 60470,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
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
        Direction           = 0,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        X                   = -48400,
        Z                   = 25180,
        Y                   = 59290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -41320,
        Z                   = 22000,
        Y                   = 50520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
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
        X                   = 28060,
        Z                   = 8000,
        Y                   = 58980,
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
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = -52000,
        TriggerZ            = 25000,
        TriggerY            = 59710,
        TriggerRange        = 1700,
        ActorX              = -52000,
        ActorZ              = 26000,
        ActorY              = 59710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6BE",          # 00, 0
        "Function_1_78F",          # 01, 1
        "Function_2_839",          # 02, 2
        "Function_3_86F",          # 03, 3
        "Function_4_F18",          # 04, 4
        "Function_5_16DF",         # 05, 5
        "Function_6_1C38",         # 06, 6
        "Function_7_2612",         # 07, 7
        "Function_8_2819",         # 08, 8
        "Function_9_2EA3",         # 09, 9
        "Function_10_3194",        # 0A, 10
        "Function_11_330C",        # 0B, 11
        "Function_12_367A",        # 0C, 12
        "Function_13_3A3A",        # 0D, 13
        "Function_14_3BA4",        # 0E, 14
        "Function_15_3BE6",        # 0F, 15
        "Function_16_3C28",        # 10, 16
        "Function_17_3C6A",        # 11, 17
        "Function_18_3CB4",        # 12, 18
        "Function_19_3D03",        # 13, 19
        "Function_20_3D31",        # 14, 20
        "Function_21_3D35",        # 15, 21
    )


    def Function_0_6BE(): pass

    label("Function_0_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_707")
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -49500, 25000, 57820, 270)
    OP_8C(0x2B, 270, 0)
    SetChrPos(0x2C, -45970, 25180, 58340, 270)
    ClearChrFlags(0x2C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_704")

    label("loc_704")

    Jump("loc_777")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_720")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_777")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_743")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_777")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_75C")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_777")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_78E")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_78E")

    Return()

    # Function_0_6BE end

    def Function_1_78F(): pass

    label("Function_1_78F")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x230052)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_809")
    OP_6F(0x0, 59)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 59)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_76(0xFF, 0x21, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_10(0x4, 0x0)
    Jump("loc_82C")

    label("loc_809")

    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x2A, 0x0, 0x0, 0x2)

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_838")
    OP_64(0x0, 0x1)

    label("loc_838")

    Return()

    # Function_1_78F end

    def Function_2_839(): pass

    label("Function_2_839")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_843")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86E")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_843")

    label("loc_86E")

    Return()

    # Function_2_839 end

    def Function_3_86F(): pass

    label("Function_3_86F")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88C")
    OP_A9(0x9C)
    TalkEnd(0x8)
    Return()

    label("loc_88C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")
    TalkEnd(0x8)
    Return()

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_9F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98F")

    ChrTalk(    #0
        0xFE,
        (
            "Hey, welcome.\x01",
            "Want something cold to drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "From what I hear, the orbment charging\x01",
            "stations aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "That's exactly the time for a drink!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Drink one down in a go. Easy\x01",
            "as pie energy restoration!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9F5")

    label("loc_98F")


    ChrTalk(    #4
        0xFE,
        "Exactly the time for a drink!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "We've got energy drinks, nutrition drinks,\x01",
            "any kind of drink!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F5")

    Jump("loc_F14")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE0")

    ChrTalk(    #6
        0xFE,
        (
            "The frenzy when the orbments stopped\x01",
            "was incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Chief Murdock tried his best to explain,\x01",
            "but people just wouldn't be satisfied\x01",
            "with anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Even I couldn't find the will to\x01",
            "sell my drinks.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B7E")

    label("loc_AE0")


    ChrTalk(    #9
        0xFE,
        "The frenzy a bit ago was incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "The tension was so thick you could have\x01",
            "cut it with a knife. Poor Chief Murdock\x01",
            "looked like he wanted to cry. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E")

    Jump("loc_F14")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BF2")

    ChrTalk(    #11
        0xFE,
        "The factory ship just left port a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Seems like a bunch of researchers boarded.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C62")

    label("loc_BF2")


    ChrTalk(    #13
        0xFE,
        "The factory ship just left port a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Feels like it's been a while\x01",
            "since I've seen that ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C62")

    Jump("loc_F14")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CDE")

    ChrTalk(    #15
        0xFE,
        (
            "Apparently the factory ship is preparing\x01",
            "to depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "They said it's going to Leiston Fortress.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D71")

    label("loc_CDE")


    ChrTalk(    #17
        0xFE,
        (
            "Apparently the factory ship is preparing\x01",
            "to depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Rehmann looked really motivated for once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Must be some really important job.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D71")

    Jump("loc_F14")

    label("loc_D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_DDB")

    ChrTalk(    #20
        0xFE,
        "Hey, good work. How about a drink?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I've got all kinds of good drinks for the body.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F14")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(    #22
        0x8,
        "Phew! That earthquake was quite the shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "Well, when you're shocked, you should\x01",
            "have something to drink and calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F14")

    label("loc_E6E")


    ChrTalk(    #24
        0x8,
        "Phew! That earthquake was quite the shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "Well, when you're shocked, you should\x01",
            "have something to drink and calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "So, how about a cold drink?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F14")

    TalkEnd(0x8)
    Return()

    # Function_3_86F end

    def Function_4_F18(): pass

    label("Function_4_F18")

    TalkBegin(0x9)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F35")
    OP_A9(0x9D)
    TalkEnd(0x9)
    Return()

    label("loc_F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F46")
    TalkEnd(0x9)
    Return()

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_10F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1053")

    ChrTalk(    #27
        0xFE,
        (
            "Ah, welcome.\x01",
            "Would you like some flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "No matter how frustrated you let yourself\x01",
            "get, that won't make things better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "That's exactly the time I hope people will\x01",
            "stop and look at the flowers. Flowers can\x01",
            "be quite calming, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_10ED")

    label("loc_1053")


    ChrTalk(    #30
        0xFE,
        (
            "No matter how frustrated you let yourself\x01",
            "get, that won't make things better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "In that case, enjoy some flowers and\x01",
            "feel the calm wash over you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10ED")

    Jump("loc_16DB")

    label("loc_10F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C0")

    ChrTalk(    #32
        0xFE,
        (
            "The furor at the central factory\x01",
            "was terribly scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "All of the people in the town had\x01",
            "really scary expressions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "...I never want to go through\x01",
            "something like that again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11FA")

    label("loc_11C0")


    ChrTalk(    #35
        0xFE,
        (
            "The furor at the central factory\x01",
            "was terribly scary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FA")

    Jump("loc_16DB")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #36
        0xFE,
        (
            "When you're busy and stressed out is\x01",
            "exactly when I wish people would stop\x01",
            "and enjoy some flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "*sigh* It seems I need to put more\x01",
            "effort into getting that message across.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_12C7")


    ChrTalk(    #38
        0xFE,
        (
            "All the people at the central\x01",
            "factory seem so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Those are EXACTLY the people I'd like\x01",
            "to take a look at some flowers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "*sigh* They always just pass right by.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1381")

    Jump("loc_16DB")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_141E")

    ChrTalk(    #41
        0xFE,
        (
            "When you're pressed for space,\x01",
            "I recommend small flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "You can enjoy a wide variety of flower\x01",
            "colors in a very small space.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148F")

    label("loc_141E")


    ChrTalk(    #43
        0xFE,
        (
            "Lately, small, more conservative flowers\x01",
            "have been popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "They're a good accent for a flower bed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_148F")

    Jump("loc_16DB")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_153B")

    ChrTalk(    #45
        0xFE,
        (
            "I don't just carry flowers for viewing, you know!\x01",
            "I also have some that can be used in cooking,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "I'd be most glad if you took a look.\x02",
    )

    CloseMessageWindow()
    Jump("loc_160D")

    label("loc_153B")


    ChrTalk(    #47
        0xFE,
        (
            "Welcome.\x01",
            "How about a flower to brighten your day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I don't just carry flowers for viewing, you know!\x01",
            "I also have some that can be used in cooking,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "I'd be most glad if you took a look.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_160D")

    Jump("loc_16DB")

    label("loc_1610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_16DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1681")

    ChrTalk(    #50
        0x9,
        (
            "Seems like it shook quite hard at\x01",
            "the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        "I heard screams all the way here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_1681")


    ChrTalk(    #52
        0x9,
        "Thank goodness... All my stock is safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        "I haven't been so surprised in ages.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_16DB")

    TalkEnd(0x9)
    Return()

    # Function_4_F18 end

    def Function_5_16DF(): pass

    label("Function_5_16DF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_18B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")

    ChrTalk(    #54
        0xFE,
        (
            "Apparently some of the army's\x01",
            "patrol ships have crashed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "It was a bit of luck that the factory\x01",
            "ship didn't end the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "In that sense, we're still well off, I'd say.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_18B4")

    label("loc_17B1")


    ChrTalk(    #57
        0xFE,
        (
            "Apparently some of the army's\x01",
            "patrol ships have crashed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "If the factory ship had been in the air\x01",
            "at the same time, it would've been\x01",
            "way worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It's not got the mobility of a patrol ship,\x01",
            "you see. There's no way it could manage\x01",
            "a glide landing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B4")

    Jump("loc_1C34")

    label("loc_18B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1978")

    ChrTalk(    #60
        0xFE,
        (
            "The factory ship can't get\x01",
            "out of the dock anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Even the maintenance crew can't\x01",
            "do anything for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Well, I'm just the pilot, so\x01",
            "not much more I can do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_19FA")

    label("loc_1978")


    ChrTalk(    #63
        0xFE,
        (
            "If the orbal engines ain't workin,\x01",
            "I'm out of a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "If there was a poet around, I'm sure\x01",
            "he'd call me a wingless bird.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FA")

    Jump("loc_1C34")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A86")

    ChrTalk(    #65
        0xFE,
        (
            "Combining the new engine model\x01",
            "with the Arseille, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Just thinking about it gives me shivers\x01",
            "of excitement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B3E")

    label("loc_1A86")


    ChrTalk(    #67
        0xFE,
        (
            "The big job recently is the Arseille\x01",
            "drive change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "We're gonna put the new model\x01",
            "engine in that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "We're scheduled to go to Leiston Fortress\x01",
            "and do the job there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B3E")

    Jump("loc_1C34")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1C34")

    ChrTalk(    #70
        0xFE,
        (
            "Phew! Anyway, I'm just glad the shaking\x01",
            "started after we docked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If things go pear-shaped when descending,\x01",
            "there's not much we pilots can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I bet the guys piloting the scheduled liners\x01",
            "sweat over that way more than me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C34")

    TalkEnd(0xA)
    Return()

    # Function_5_16DF end

    def Function_6_1C38(): pass

    label("Function_6_1C38")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 1)), scpexpr(EXPR_END)), "loc_1CB9")

    ChrTalk(    #73
        0xFE,
        (
            "I'll leave the military request\x01",
            "or whatever to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Well, then, take care in the capital\x01",
            "or whatever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_20C8")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #75
        0xFE,
        "Oh, hey, it's Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        "#052FGundolf, you back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "Heh, only just.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Feel a bit bad askin' you to keep\x01",
            "an eye out every time I go away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(    #79
        0xFE,
        (
            "That reminds me, I think I owe\x01",
            "you a lot, missy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I've heard about the successes of Estelle Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I know it's a bit late, but congratulations\x01",
            "on your promotion to full bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1008FAhaha, thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Still, seems like you got saddled with a\x01",
            "pretty big pain of a case right off the bat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Well, it's tradition to use the best of us\x01",
            "the hardest, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "By the way, you leavin' Zeiss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1006FYeah, we're going to the capital.\x02\x03",

            "Apparently we got an official request\x01",
            "from the army of all things.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #87
        0xFE,
        "Huh, an army request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I didn't hear anything about\x01",
            "that when I was over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        "#050FGuess you musta just missed it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #90
        0xFE,
        "Ah, man. Bad timing, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Well, whatever. I'll leave that to you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #92
        0xFE,
        "Take care in the capital or whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1001FYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_260B")

    label("loc_20C8")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #94
        0xFE,
        (
            "Oh, hey. Who could it be but Scherazard,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x103,
        (
            "#023FGundolf?\x02\x03",

            "Back in Zeiss, are we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "Heh, just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "Still, feels like it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Looks like you've become an even\x01",
            "better woman than last I saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        (
            "#021FWhy, thank you.\x02\x03",

            "#027FHowever, flattery will get you nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Heh, just you taking care of things\x01",
            "while I was away's plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I get dispatched out a lot, after all.\x01",
            "I keep havin' to leave Zeiss to\x01",
            "someone else.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(    #102
        0xFE,
        (
            "I think I owe this missy here\x01",
            "even more now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "I've heard about the successes of Estelle Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I know it's a bit late, but congratulations\x01",
            "on your promotion to full bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1008FAhaha, thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Still, seems like you got saddled with a\x01",
            "pretty big pain of a case right off the bat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Well, it's the tradition to use\x01",
            "the best of us the hardest, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "By the way, you leavin' Zeiss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1006FYeah, we're going to the capital.\x02\x03",

            "Apparently we got an official request\x01",
            "from the army of all things.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #110
        0xFE,
        "Huh, an army request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I didn't hear anything about\x01",
            "that when I was over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#023FSeems like you just missed it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #113
        0xFE,
        "Ah, man. Bad timing, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Well, whatever. I'll leave that to you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xFE,
        "Take care in the capital or whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1001FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_260B")

    OP_A2(0x1641)

    label("loc_260E")

    TalkEnd(0xB)
    Return()

    # Function_6_1C38 end

    def Function_7_2612(): pass

    label("Function_7_2612")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2735")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_26B3")

    ChrTalk(    #117
        0xFE,
        (
            "There's no more space to put\x01",
            "flower beds on that veranda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "If I want to put down more flower\x01",
            "beds, maybe I need to get a new shelf.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2732")

    label("loc_26B3")


    ChrTalk(    #119
        0xFE,
        (
            "I'd like to make a flower bed of just\x01",
            "small flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "But there really isn't any\x01",
            "space on the veranda, is there...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2732")

    Jump("loc_2815")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_279F")

    ChrTalk(    #121
        0xFE,
        (
            "Modest yet elegant...\x01",
            "Small flowers are cute, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Almost like me in my youth.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2815")

    label("loc_279F")


    ChrTalk(    #123
        0xFE,
        "My, this is adorable as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Extravagant ones are lovely, too, but small\x01",
            "flowers are pleasantly modest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2815")

    TalkEnd(0xC)
    Return()

    # Function_7_2612 end

    def Function_8_2819(): pass

    label("Function_8_2819")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_299E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2922")

    ChrTalk(    #125
        0xFE,
        "I wonder how something so big is floating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Maybe it's equipped with the same kind\x01",
            "of orbal engine as an airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Well, that's one idea, but it all seems\x01",
            "impossible, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "After all, all orbments aren't working.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_299B")

    label("loc_2922")


    ChrTalk(    #129
        0xFE,
        (
            "That island is floating based on\x01",
            "a different power than we know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "After all, all orbments have stopped working.\x02",
    )

    CloseMessageWindow()

    label("loc_299B")

    Jump("loc_2E9F")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A83")

    ChrTalk(    #131
        0xFE,
        "Incredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "That floating object is so big it's mind-blowing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "If I knew the distance, I'd be able\x01",
            "to estimate its size, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I'll just have to wait for the\x01",
            "Royal Army's investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2B1A")

    label("loc_2A83")


    ChrTalk(    #135
        0xFE,
        "That floating object is so big it's mind-blowing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I want to calculate the distance as soon as\x01",
            "possible so I can get an estimate of its size.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1A")

    Jump("loc_2E9F")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2B9F")

    ChrTalk(    #137
        0xFE,
        "Mom's seriously forgotten her original goal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Where, I wonder, did the plan to\x01",
            "deal with the earthquakes go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9F")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(    #139
        0xFE,
        (
            "I'm always amazed by Professor\x01",
            "Russell's inventions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "After all, that kind of genius comes\x01",
            "once in a lifetime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCE")

    label("loc_2C28")

    TurnDirection(0xD, 0x107, 0)

    ChrTalk(    #141
        0xFE,
        "Ah, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "It's been a while. Since last Sunday School,\x01",
            "I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        (
            "#560FHello, Vince.\x02\x03",

            "Shopping with your mom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "Yes, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Working again today, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x107,
        (
            "#060FYeah, I'm gonna go place some\x01",
            "new measuring equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "One of Professor Russell's inventions?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I hope you'll give me a detailed\x01",
            "explanation next Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Well, see you then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        "#061FAh, yeah, later!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2DCE")

    Jump("loc_2E9F")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2E9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2E1E")

    ChrTalk(    #151
        0xFE,
        (
            "Also, mother, you planted this\x01",
            "species just a bit ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9F")

    label("loc_2E1E")


    ChrTalk(    #152
        0xFE,
        "Mother, please, remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "The reason you were fixing the flower\x01",
            "beds was to prepare for an earthquake\x01",
            "not... *sigh*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2E9F")

    TalkEnd(0xD)
    Return()

    # Function_8_2819 end

    def Function_9_2EA3(): pass

    label("Function_9_2EA3")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F59")

    ChrTalk(    #154
        0xFE,
        (
            "Of course, if I'm going to go for it\x01",
            "I'm going to aim for something utterly\x01",
            "unique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Heh heh, when I return I will order\x01",
            "the needed samples immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3006")

    label("loc_2F59")


    ChrTalk(    #156
        0xFE,
        (
            "Heh, I have decided what to grow\x01",
            "next in the greenhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "This time the theme will be 'healing.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I hope I can create something\x01",
            "that grants peace to people.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3006")

    Jump("loc_3190")

    label("loc_3009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3075")

    ChrTalk(    #159
        0xFE,
        "I see, for observing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Certainly that is one of the\x01",
            "reasons people love plants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3190")

    label("loc_3075")


    ChrTalk(    #161
        0xFE,
        "I see, flowers for a bit of decoration...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I would like at least one pot to\x01",
            "brighten up the lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Still, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "The viewpoint of something to be appreciated\x01",
            "visually is also interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "After all, that certainly is one of\x01",
            "the reasons people love plants.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3190")

    TalkEnd(0xE)
    Return()

    # Function_9_2EA3 end

    def Function_10_3194(): pass

    label("Function_10_3194")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(    #166
        0xFE,
        (
            "When that floating object appeared,\x01",
            "the sky seemed like it shone gold\x01",
            "for a moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "Speaking from a septium perspective,\x01",
            "gold represents 'space'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "There may be a connection between the two.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3308")

    label("loc_3278")


    ChrTalk(    #169
        0xFE,
        (
            "I came because I heard you\x01",
            "could see that object, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "I didn't think it would be that big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "What is happening in this kingdom?\x02",
    )

    CloseMessageWindow()

    label("loc_3308")

    TalkEnd(0xFE)
    Return()

    # Function_10_3194 end

    def Function_11_330C(): pass

    label("Function_11_330C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_34CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3458")

    ChrTalk(    #172
        0xFE,
        "I thought the end of the world was coming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "It seems the true twilight is still a bit away,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Maybe I should go back to my\x01",
            "workplace and get a parasol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "Too much sun gives you wrinkles,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "If I'm going to be summoned to heaven,\x01",
            "I'd like to go as beautiful as I am now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_34CC")

    label("loc_3458")


    ChrTalk(    #177
        0xFE,
        "It seems the end of the world isn't here yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Maybe I should go back to my\x01",
            "workplace and get a parasol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CC")

    Jump("loc_3676")

    label("loc_34CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3676")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(    #179
        0xFE,
        (
            "Working while something like that is\x01",
            "hanging over our heads seems ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "I'm sure the world will end before long.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "To spend my last hours at my workplace\x01",
            "is absolutely something I refuse to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3676")

    label("loc_35B9")


    ChrTalk(    #182
        0xFE,
        (
            "Working while something like that is\x01",
            "hanging over our heads seems ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Those still hunched over their desks at\x01",
            "a time like this have no perspective on\x01",
            "what really matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3676")

    TalkEnd(0xFE)
    Return()

    # Function_11_330C end

    def Function_12_367A(): pass

    label("Function_12_367A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    SetChrPos(0xF, -35290, 10000, 59780, 90)
    SetChrPos(0x10, -35230, 10000, 58160, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -33900, 10000, 56360, 331)
    SetChrPos(0x8, -32920, 10000, 61360, 211)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x11, -33530, 10000, 57330, 270)
    SetChrPos(0x12, -33050, 10000, 58910, 270)
    SetChrPos(0x13, -33880, 10000, 61340, 225)
    SetChrPos(0x14, -32500, 10000, 60280, 270)
    SetChrPos(0x15, -32360, 10000, 57680, 270)
    SetChrPos(0x16, -31130, 9600, 59060, 270)
    SetChrPos(0x17, -30660, 9100, 60320, 270)
    SetChrPos(0x18, -30670, 9200, 57500, 270)
    SetChrPos(0x19, -29220, 8000, 58710, 270)
    SetChrPos(0x1A, -29090, 8000, 60610, 270)
    SetChrPos(0x1B, -27830, 8000, 57460, 270)
    SetChrPos(0x1C, -27220, 8000, 59380, 270)
    SetChrPos(0x1D, -27240, 8000, 61340, 225)
    SetChrPos(0x1E, -25050, 8000, 57430, 270)
    SetChrPos(0x1F, -23040, 8000, 59720, 270)
    SetChrPos(0x20, -22340, 8000, 61820, 270)
    SetChrPos(0x21, -21800, 8000, 56830, 315)
    SetChrPos(0x22, -23720, 8000, 58160, 270)
    SetChrPos(0x23, -20480, 8000, 59330, 270)
    SetChrPos(0x24, -19770, 8000, 57860, 270)
    SetChrPos(0x25, -25080, 8000, 60640, 270)
    SetChrPos(0x26, -23770, 8000, 55620, 315)
    SetChrPos(0x27, -8950, 7510, 56760, 270)
    SetChrPos(0x28, -7210, 6760, 56690, 270)
    SetChrPos(0x29, -7900, 7010, 61680, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6D(-14360, 8000, 59650, 0)
    OP_67(0, 8840, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(299000, 0)
    OP_6E(455, 0)
    OP_43(0xF, 0x1, 0x0, 0x11)
    OP_43(0x10, 0x1, 0x0, 0x12)
    OP_43(0x27, 0x0, 0x0, 0xE)
    OP_43(0x28, 0x0, 0x0, 0xF)
    OP_43(0x29, 0x0, 0x0, 0x10)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_C8(0x200, 0x46, "C_PLAC23._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_39D4():
        OP_6D(-35500, 10000, 59580, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39D4)

    def lambda_39EC():
        OP_67(0, 7230, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_39EC)

    def lambda_3A04():
        OP_6C(314000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3A04)
    OP_6E(513, 7000)
    Sleep(1000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R0203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_367A end

    def Function_13_3A3A(): pass

    label("Function_13_3A3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA3")
    OP_62(0x11, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x1B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x20, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x25, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x17, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x21, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x26, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x18, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x23, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sleep(500)
    OP_62(0x15, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    Jump("Function_13_3A3A")

    label("loc_3BA3")

    Return()

    # Function_13_3A3A end

    def Function_14_3BA4(): pass

    label("Function_14_3BA4")

    OP_8E(0xFE, 0xFFFFD08A, 0x1F40, 0xDE58, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBDB6, 0x1F40, 0xE31C, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Return()

    # Function_14_3BA4 end

    def Function_15_3BE6(): pass

    label("Function_15_3BE6")

    OP_8E(0xFE, 0xFFFFD08A, 0x1F40, 0xDE58, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFB3AC, 0x1F40, 0xDB2E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Return()

    # Function_15_3BE6 end

    def Function_16_3C28(): pass

    label("Function_16_3C28")

    OP_8E(0xFE, 0xFFFFD044, 0x1F40, 0xF0C8, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFB24E, 0x1F40, 0xEC5E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Return()

    # Function_16_3C28 end

    def Function_17_3C6A(): pass

    label("Function_17_3C6A")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3C7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CB3")
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_3C7C")

    label("loc_3CB3")

    Return()

    # Function_17_3C6A end

    def Function_18_3CB4(): pass

    label("Function_18_3CB4")

    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3CCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D02")
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_3CCB")

    label("loc_3D02")

    Return()

    # Function_18_3CB4 end

    def Function_19_3D03(): pass

    label("Function_19_3D03")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400D0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_19_3D03 end

    def Function_20_3D31(): pass

    label("Function_20_3D31")

    SetPlaceName(0x85)
    Return()

    # Function_20_3D31 end

    def Function_21_3D35(): pass

    label("Function_21_3D35")

    SetPlaceName(0x81)
    Return()

    # Function_21_3D35 end

    SaveToFile()

Try(main)
