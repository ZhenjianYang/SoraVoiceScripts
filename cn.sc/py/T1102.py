from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1102   ._SN',
        MapName             = 'Bose',
        Location            = 'T1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 43,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1102_1 ._SN',
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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '阿加特',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '乘客',                                 # 15
        '乘客',                                 # 16
        '乘客',                                 # 17
        '乘客',                                 # 18
        '乘客',                                 # 19
        '乘客',                                 # 20
        '奈尔',                                 # 21
        '朵洛希',                               # 22
        '尤莉亚上尉',                           # 23
        '摩尔根将军',                           # 24
        '接待员泰德',                           # 25
        '拉克斯',                               # 26
        '诺尔姆',                               # 27
        '贝尔娜',                               # 28
        '阿尔丹',                               # 29
        '科尔娜',                               # 30
        '莫莉',                                 # 31
        '赛希莉亚号乘客',                       # 32
        '赛希莉亚号乘客',                       # 33
        '赛希莉亚号乘客',                       # 34
        '赛希莉亚号乘客',                       # 35
        '赛希莉亚号乘客',                       # 36
        '佩特洛夫船长',                         # 37
        '乘务员诺拉',                           # 38
        '卡洛塔',                               # 39
        '沙库',                                 # 40
        '飞艇',                                 # 41
        '飞艇影',                               # 42
        '弗库利夫特',                           # 43
        '柏斯市·北街区',                       # 44
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH01110 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH01130 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT07/CH01150 ._CH',             # 0B
        'ED6_DT07/CH02060 ._CH',             # 0C
        'ED6_DT07/CH02070 ._CH',             # 0D
        'ED6_DT27/CH03580 ._CH',             # 0E
        'ED6_DT07/CH02080 ._CH',             # 0F
        'ED6_DT07/CH01290 ._CH',             # 10
        'ED6_DT06/CH20063 ._CH',             # 11
        'ED6_DT06/CH20129 ._CH',             # 12
        'ED6_DT06/CH20051 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
        'ED6_DT07/CH01210 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
        'ED6_DT07/CH01453 ._CH',             # 18
        'ED6_DT07/CH00051 ._CH',             # 19
        'ED6_DT07/CH00061 ._CH',             # 1A
        'ED6_DT07/CH01050 ._CH',             # 1B
        'ED6_DT07/CH01020 ._CH',             # 1C
        'ED6_DT07/CH01170 ._CH',             # 1D
        'ED6_DT07/CH01440 ._CH',             # 1E
        'ED6_DT07/CH01540 ._CH',             # 1F
        'ED6_DT26/CH20311 ._CH',             # 20
        'ED6_DT07/CH01460 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH01110P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH01130P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT07/CH01150P._CP',             # 0B
        'ED6_DT07/CH02060P._CP',             # 0C
        'ED6_DT07/CH02070P._CP',             # 0D
        'ED6_DT27/CH03580P._CP',             # 0E
        'ED6_DT07/CH02080P._CP',             # 0F
        'ED6_DT07/CH01290P._CP',             # 10
        'ED6_DT06/CH20063P._CP',             # 11
        'ED6_DT06/CH20129P._CP',             # 12
        'ED6_DT06/CH20051P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
        'ED6_DT07/CH01210P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
        'ED6_DT07/CH01453P._CP',             # 18
        'ED6_DT07/CH00051P._CP',             # 19
        'ED6_DT07/CH00061P._CP',             # 1A
        'ED6_DT07/CH01050P._CP',             # 1B
        'ED6_DT07/CH01020P._CP',             # 1C
        'ED6_DT07/CH01170P._CP',             # 1D
        'ED6_DT07/CH01440P._CP',             # 1E
        'ED6_DT07/CH01540P._CP',             # 1F
        'ED6_DT26/CH20311P._CP',             # 20
        'ED6_DT07/CH01460P._CP',             # 21
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 27300,
        Z                   = -10000,
        Y                   = 26800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 48500,
        Z                   = 1500,
        Y                   = 36800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 47600,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 49740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48340,
        Z                   = 0,
        Y                   = 12210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 44940,
        Z                   = 0,
        Y                   = 15680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 50290,
        Z                   = 0,
        Y                   = 16239,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 51900,
        Z                   = 0,
        Y                   = 13500,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 51890,
        Z                   = 0,
        Y                   = 14350,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 45050,
        Z                   = 0,
        Y                   = 11720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 48780,
        Z                   = 1500,
        Y                   = 43400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 48140,
        Z                   = 0,
        Y                   = 18710,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 29420,
        Z                   = -3000,
        Y                   = 17280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 50900,
        Z                   = 0,
        Y                   = 18020,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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


    DeclEvent(
        X                   = 48000,
        Y                   = -2000,
        Z                   = 25600,
        Range               = 52000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x6E8C,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
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
        TriggerX            = 25480,
        TriggerZ            = -3000,
        TriggerY            = 11080,
        TriggerRange        = 1600,
        ActorX              = 25480,
        ActorZ              = -1000,
        ActorY              = 11080,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
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
        TalkFunctionIndex   = 40,
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
        TalkFunctionIndex   = 41,
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
        TalkFunctionIndex   = 42,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_70E",          # 00, 0
        "Function_1_8A5",          # 01, 1
        "Function_2_9C5",          # 02, 2
        "Function_3_9E9",          # 03, 3
        "Function_4_9EE",          # 04, 4
        "Function_5_1148",         # 05, 5
        "Function_6_1470",         # 06, 6
        "Function_7_17CC",         # 07, 7
        "Function_8_1EC3",         # 08, 8
        "Function_9_24BB",         # 09, 9
        "Function_10_25FE",        # 0A, 10
        "Function_11_268A",        # 0B, 11
        "Function_12_2754",        # 0C, 12
        "Function_13_27F9",        # 0D, 13
        "Function_14_2870",        # 0E, 14
        "Function_15_28D5",        # 0F, 15
        "Function_16_2955",        # 10, 16
        "Function_17_2B71",        # 11, 17
        "Function_18_2D4D",        # 12, 18
        "Function_19_2E1B",        # 13, 19
        "Function_20_2F2A",        # 14, 20
        "Function_21_312C",        # 15, 21
        "Function_22_31A7",        # 16, 22
        "Function_23_36B2",        # 17, 23
        "Function_24_3E25",        # 18, 24
        "Function_25_431D",        # 19, 25
        "Function_26_5EA7",        # 1A, 26
        "Function_27_5F5A",        # 1B, 27
        "Function_28_5F97",        # 1C, 28
        "Function_29_5FC0",        # 1D, 29
        "Function_30_601B",        # 1E, 30
        "Function_31_6064",        # 1F, 31
        "Function_32_607B",        # 20, 32
        "Function_33_63CE",        # 21, 33
        "Function_34_6721",        # 22, 34
        "Function_35_684E",        # 23, 35
        "Function_36_689F",        # 24, 36
        "Function_37_697E",        # 25, 37
        "Function_38_73AC",        # 26, 38
        "Function_39_7433",        # 27, 39
        "Function_40_75B4",        # 28, 40
        "Function_41_762A",        # 29, 41
        "Function_42_7690",        # 2A, 42
        "Function_43_770C",        # 2B, 43
        "Function_44_7812",        # 2C, 44
    )


    def Function_0_70E(): pass

    label("Function_0_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_724")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_77E")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_743")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 25)
    Jump("loc_77E")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_762")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_77E")

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_77E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_802")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x19, 48770, 1500, 42170, 0)
    SetChrPos(0x1A, 31910, -10000, 26200, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_7FF")

    label("loc_7E9")

    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x25, 51300, 1500, 35740, 96)

    label("loc_7FF")

    Jump("loc_8A4")

    label("loc_802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_81B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_818")
    ClearChrFlags(0x1D, 0x80)

    label("loc_818")

    Jump("loc_8A4")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_836")
    SetChrPos(0x1C, 46320, 3000, -1140, 0)
    Jump("loc_8A4")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_867")
    SetChrFlags(0x1C, 0x80)
    SetChrPos(0x1A, 25620, -10000, 26830, 45)
    SetChrPos(0x1B, 25890, -3000, 17040, 0)
    Jump("loc_8A4")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_89D")
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrPos(0x19, 27300, -10000, 26800, 0)
    SetChrPos(0x1A, 48500, 1500, 36800, 0)
    Jump("loc_8A4")

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_8A4")

    label("loc_8A4")

    Return()

    # Function_0_70E end

    def Function_1_8A5(): pass

    label("Function_1_8A5")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE98A0, 0x230042)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    OP_B1("T1102_2")
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x7, 410)
    Jump("loc_93D")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_90C")
    OP_B1("T1102_3")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_93D")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_920")
    OP_B1("T1102_2")
    Jump("loc_93D")

    label("loc_920")

    OP_B1("T1102_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0x9, 0x4)

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_947")
    Jump("loc_97E")

    label("loc_947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_957")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_967")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_977")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_97E")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_97E")

    label("loc_97E")

    OP_64(0x1, 0x1)
    OP_A1(0x2A, 0xD)
    SetChrPos(0x2A, 26510, -3000, 10000, 135)
    OP_72(0xD, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C4")
    OP_65(0x1, 0x1)

    label("loc_9C4")

    Return()

    # Function_1_8A5 end

    def Function_2_9C5(): pass

    label("Function_2_9C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E8")
    OP_8D(0xFE, 45950, 15590, 50720, 11210, 1500)
    Jump("Function_2_9C5")

    label("loc_9E8")

    Return()

    # Function_2_9C5 end

    def Function_3_9E9(): pass

    label("Function_3_9E9")

    Call(0, 4)
    Return()

    # Function_3_9E9 end

    def Function_4_9EE(): pass

    label("Function_4_9EE")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A56")

    ChrTalk(    #0
        0x18,
        (
            "那里的客人们……\x01",
            "一直不肯离开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x18,
        (
            "这、这真是糟糕……\x01",
            "船暂时无法出发……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_AA6")

    label("loc_A56")


    ChrTalk(    #2
        0x18,
        (
            "嗯，一直在这里等\x01",
            "我们也实在是为难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x18,
        (
            "也不知道什么时候\x01",
            "才能恢复航行…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA6")

    Jump("loc_1144")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B16")

    ChrTalk(    #4
        0x18,
        (
            "被滞留在这里的客人\x01",
            "没有可去的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x18,
        (
            "现在准备把他们\x01",
            "安排在酒店了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)
    SetChrFlags(0x18, 0x10)
    OP_A2(0x0)
    Jump("loc_B5A")

    label("loc_B16")


    ChrTalk(    #6
        0x18,
        (
            "已经安排各位\x01",
            "住在旅馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x18,
        (
            "还要办理一些手续，\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jump("loc_1144")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BBA")

    ChrTalk(    #8
        0x18,
        (
            "听说捕获作战中\x01",
            "游击士立下了大功呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x18,
        (
            "哈哈，现在协会\x01",
            "一定很得意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5B")

    label("loc_BBA")


    ChrTalk(    #10
        0x18,
        (
            "呀，各位，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x18,
        (
            "听说捕获作战中\x01",
            "游击士立下了大功呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x18,
        (
            "空贼事件时也是，\x01",
            "这次已经是第二次让你们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x18,
        (
            "哈哈，现在协会\x01",
            "一定很得意吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C5B")

    Jump("loc_1144")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CB9")

    ChrTalk(    #14
        0x18,
        (
            "『埃尔赛尤』的行动也\x01",
            "开始紧张了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x18,
        (
            "捕获作战也\x01",
            "进入佳境了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D31")

    label("loc_CB9")


    ChrTalk(    #16
        0x18,
        (
            "『埃尔赛尤』的行动也\x01",
            "开始紧张了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x18,
        (
            "捕获作战也\x01",
            "进入佳境了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x18,
        (
            "希望赶快解决它，\x01",
            "然后解除飞行限制吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D31")

    Jump("loc_1144")

    label("loc_D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(    #19
        0x18,
        (
            "军队的舰艇\x01",
            "准备在这里着陆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x18,
        (
            "请各位在右手边\x01",
            "的第一飞船坪等待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0A")

    label("loc_D8D")

    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #21
        0x18,
        (
            "啊……\x01",
            "是各位游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x18,
        (
            "军队的舰艇\x01",
            "准备在这里着陆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x18,
        (
            "请在右手边的\x01",
            "的第一飞船坪等待。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E0A")

    Jump("loc_1144")

    label("loc_E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(    #24
        0x18,
        (
            "巨、巨大的影子\x01",
            "向西北方飞去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x18,
        (
            "不过船没有撞上，\x01",
            "就是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_E6E")


    ChrTalk(    #26
        0x18,
        (
            "巨、巨大的影子\x01",
            "从天上飞过去了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x18,
        (
            "那、那个\x01",
            "难道就是传说中的龙？！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EBB")

    Jump("loc_1144")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 3)), scpexpr(EXPR_END)), "loc_1021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F2E")

    ChrTalk(    #28
        0x18,
        (
            "最近定期船的航行也恢复了，\x01",
            "真让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x18,
        (
            "政变之后，\x01",
            "情况一直很稳定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDD")

    label("loc_F2E")


    ChrTalk(    #30
        0x18,
        (
            "最近定期船的航行也恢复了，\x01",
            "真让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x18,
        (
            "政变之后，\x01",
            "情况一直很稳定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x18,
        (
            "听说空贼团把船\x01",
            "夺走以后还很担心…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x18,
        (
            "不过之后他们就杳无音信了，\x01",
            "大概是逃到国外了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FDD")

    Jump("loc_101E")

    label("loc_FE0")


    ChrTalk(    #34
        0x18,
        (
            "阿加特先生\x01",
            "好像总是很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x18,
        (
            "偶尔也好好\x01",
            "休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101E")

    Jump("loc_1144")

    label("loc_1021")

    TurnDirection(0x18, 0x106, 0)

    ChrTalk(    #36
        0x18,
        "啊，阿加特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        "#051F哟，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x18,
        (
            "啊啊，是吗。\x01",
            "好像刚回来啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x18,
        "……今年也特意回乡看看吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        (
            "#053F不，这次是为了工作。\x02\x03",

            "#051F不过等解决之后\x01",
            "也准备回去看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x18,
        (
            "偶尔回去\x01",
            "休息一下也不坏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "那么，要是有需要的话\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x106,
        "#051F啊，那先这样啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A43)
    OP_A2(0x0)

    label("loc_1144")

    TalkEnd(0x18)
    Return()

    # Function_4_9EE end

    def Function_5_1148(): pass

    label("Function_5_1148")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(    #44
        0xFE,
        (
            "定期船的航行\x01",
            "也恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "延期的旅行这下\x01",
            "终于可以出发了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146C")

    label("loc_119B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #46
        0xFE,
        "定期船还没有恢复，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "旅行看来还是\x01",
            "延期比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1246")

    label("loc_11E5")


    ChrTalk(    #48
        0xFE,
        "定期船还没有恢复，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "军队的制度\x01",
            "什么时候才能解除呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "旅行看来还是\x01",
            "延期比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1246")

    Jump("loc_146C")

    label("loc_1249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_129F")

    ChrTalk(    #51
        0xFE,
        (
            "呼～我本来想去旅行的，\x01",
            "但定期船竟然停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "还真是不巧啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1333")

    label("loc_129F")


    ChrTalk(    #53
        0xFE,
        (
            "都是因为军队的制度，\x01",
            "所以飞船才会停航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "呼～我本来想去旅行的，\x01",
            "可为什么定期船会停航啊？！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "上次想要旅行的时候\x01",
            "就遇到了空贼事件呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1333")

    Jump("loc_146C")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_138D")

    ChrTalk(    #56
        0xFE,
        "那、那是什么啊？！那个怪物！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "从、从哪里冒出来的啊，\x01",
            "那种东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146C")

    label("loc_138D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_146C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13E6")

    ChrTalk(    #58
        0xFE,
        (
            "明天要去王都，\x01",
            "所以特意来定船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "可以的话，想定\x01",
            "下午的票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146C")

    label("loc_13E6")


    ChrTalk(    #60
        0xFE,
        (
            "明天要去王都，\x01",
            "所以特意来定船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "以前发生空贼事件的时候\x01",
            "定期船就遇到了很大的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "从那以后，飞船\x01",
            "就做了很多改变。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_146C")

    TalkEnd(0x1B)
    Return()

    # Function_5_1148 end

    def Function_6_1470(): pass

    label("Function_6_1470")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1500")

    ChrTalk(    #63
        0xFE,
        (
            "呼～飞船坪\x01",
            "我可是每天都来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "可为什么『埃尔赛尤』\x01",
            "出现的时候我偏偏不在！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "笨蛋笨蛋！！我真是个笨蛋！！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1576")

    label("loc_1500")


    ChrTalk(    #66
        0xFE,
        (
            "今天早上本来想来\x01",
            "拍摄飞船的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "但因为心情不好\x01",
            "就没有来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "结果没看到『埃尔赛尤』，\x01",
            "真是大受打击啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1576")

    Jump("loc_17C8")

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 6)), scpexpr(EXPR_END)), "loc_15CF")

    ChrTalk(    #69
        0xFE,
        (
            "竟、竟然会错过\x01",
            "埃尔赛尤号…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "笨蛋笨蛋！！我真是个笨蛋！！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1682")

    label("loc_15CF")


    ChrTalk(    #71
        0xFE,
        "喂、喂，你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "埃尔赛尤号\x01",
            "在这里着陆是真的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015F嗯，确实来了……\x02\x03",

            "不过已经飞走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)

    ChrTalk(    #74
        0xFE,
        "#3S啊───────\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "错、错过了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A46)

    label("loc_1682")

    Jump("loc_17C8")

    label("loc_1685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_17C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(    #76
        0xFE,
        (
            "虽然没有看到『埃尔赛尤』，\x01",
            "但也是个不错的摄影旅行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "要是以后再遇到的话，\x01",
            "一定把这次的也补拍回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C8")

    label("loc_1704")


    ChrTalk(    #78
        0xFE,
        (
            "呼～总算是\x01",
            "回到柏斯了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "我为了追随『埃尔赛尤』\x01",
            "在蔡斯和王都之间东奔西走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "结果还是没有遇到。\x01",
            "不过这次的摄影旅行也算不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "好！下次有机会的话\x01",
            "一定要拍到\x01",
            "最完美的照片！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_17C8")

    TalkEnd(0x1C)
    Return()

    # Function_6_1470 end

    def Function_7_17CC(): pass

    label("Function_7_17CC")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_18F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")

    ChrTalk(    #82
        0xFE,
        (
            "『赛希莉亚号』的引擎\x01",
            "没有发现任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "各零件也没有任何损伤，\x01",
            "简直就是完美无瑕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "导力器无法运转的原因\x01",
            "实在是不明白啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "看见现在这种结果，\x01",
            "真是让人抱有期待啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_18F4")

    label("loc_1898")


    ChrTalk(    #86
        0xFE,
        (
            "『赛希莉亚号』的引擎\x01",
            "没有发现任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "各零件也没有任何损伤，\x01",
            "简直就是完美无瑕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F4")

    Jump("loc_1EBF")

    label("loc_18F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AD")

    ChrTalk(    #88
        0xFE,
        (
            "慎重起见，还是再检查一次\x01",
            "『赛希莉亚号』的引擎吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "如果和导力器瘫痪的理由相同的话，\x01",
            "就要检查一下装置了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "好好调查一下内部，\x01",
            "确认一下停止时的状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A13")

    label("loc_19AD")


    ChrTalk(    #91
        0xFE,
        (
            "慎重起见，还是再检查一次\x01",
            "『赛希莉亚号』的引擎吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "好好调查一下内部，\x01",
            "确认一下停止时的状况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A13")

    Jump("loc_1EBF")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A7A")

    ChrTalk(    #93
        0xFE,
        "接下来就是『林德号』了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "好，这艘船的整备，\x01",
            "我们也不会出现一分钟的误差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACD")

    label("loc_1A7A")


    ChrTalk(    #95
        0xFE,
        (
            "很好！\x01",
            "接下来就是『林德号』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "定期船通航以后，\x01",
            "果然干劲就是不同了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1ACD")

    Jump("loc_1EBF")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1B30")

    ChrTalk(    #97
        0xFE,
        (
            "噢，是你们啊。\x01",
            "调查进行得怎么样了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "虽然不知道是什么事件，\x01",
            "总之要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBF")

    label("loc_1B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B99")

    ChrTalk(    #99
        0xFE,
        (
            "『埃尔赛尤』是艘比\x01",
            "传闻中更优秀的船啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "不但性能优秀，\x01",
            "整备性之高也非常了得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6E")

    label("loc_1B99")


    ChrTalk(    #101
        0xFE,
        "呼，『埃尔赛尤』吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "虽然我是第一次对这艘船进行整备，\x01",
            "不过确实是前所未见的好船啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "不但性能优秀，\x01",
            "整备性也非常高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "细微的检查整备\x01",
            "是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "如果在非常时期，\x01",
            "就需要迅速调整状态。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C6E")

    Jump("loc_1EBF")

    label("loc_1C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CC0")

    ChrTalk(    #106
        0xFE,
        (
            "军队的船\x01",
            "马上要准备着陆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "我们也要准备\x01",
            "迎接才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D55")

    label("loc_1CC0")


    ChrTalk(    #108
        0xFE,
        (
            "军队的船\x01",
            "马上要准备着陆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "我们也要准备\x01",
            "迎接才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "定期船都停止了，\x01",
            "这次的战斗实在是不得了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "但如今也\x01",
            "只有祈祷努力有效果了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D55")

    Jump("loc_1EBF")

    label("loc_1D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DAC")

    ChrTalk(    #112
        0xFE,
        "……古代龙吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "那真是太危险了…\x01",
            "这事情肯定会很严重啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E01")

    label("loc_1DAC")


    ChrTalk(    #114
        0xFE,
        (
            "难道…\x01",
            "刚才那东西…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "……古代龙……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "那真是太危险了…\x01",
            "要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1E01")

    Jump("loc_1EBF")

    label("loc_1E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E55")

    ChrTalk(    #117
        0xFE,
        (
            "到『林德号』来之前\x01",
            "还有些时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "来检查一下\x01",
            "材料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBF")

    label("loc_1E55")


    ChrTalk(    #119
        0xFE,
        (
            "好！『赛希莉亚号』\x01",
            "没有问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "到『林德号』来之前\x01",
            "还有些时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "趁现在检查一下\x01",
            "材料吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1EBF")

    TalkEnd(0x19)
    Return()

    # Function_7_17CC end

    def Function_8_1EC3(): pass

    label("Function_8_1EC3")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F58")

    ChrTalk(    #122
        0xFE,
        (
            "『赛希莉亚号』\x01",
            "还和以前一样停在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "连拉克斯主任\x01",
            "好像也都很头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "我还是第一次看到。\x01",
            "主任一脸那种表情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1FAA")

    label("loc_1F58")


    ChrTalk(    #125
        0xFE,
        (
            "连拉克斯主任\x01",
            "好像也都很头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "我还是第一次看到。\x01",
            "主任一脸那种表情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAA")

    Jump("loc_24B7")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2065")

    ChrTalk(    #127
        0xFE,
        (
            "不只是『赛希莉亚号』，\x01",
            "诱导灯和各种设施也都无法运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "虽然以前也发生过类似故障，\x01",
            "但从来都没有这么严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "难道说这也是因为\x01",
            "昨天晚上异变的影响吗…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_20DB")

    label("loc_2065")


    ChrTalk(    #130
        0xFE,
        (
            "不只是『赛希莉亚号』，\x01",
            "诱导灯和各种设施也都无法运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "虽然以前也发生过类似故障，\x01",
            "但从来都没有这么严重啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    Jump("loc_24B7")

    label("loc_20DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_21C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(    #132
        0xFE,
        (
            "托你们的福，\x01",
            "定期船终于恢复航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "超市也开始营业了，\x01",
            "这下总算是回到正轨了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C0")

    label("loc_2147")


    ChrTalk(    #134
        0xFE,
        (
            "托你们的福，\x01",
            "定期船终于恢复航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "超市也开始营业了，\x01",
            "这下总算是回到正轨了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "好！我们也要加油工作啊！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_21C0")

    Jump("loc_24B7")

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_227E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(    #137
        0xFE,
        (
            "真没想到『埃尔赛尤』\x01",
            "会在这着陆啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227B")

    label("loc_21FD")


    ChrTalk(    #138
        0xFE,
        (
            "真，真没想到『埃尔赛尤』\x01",
            "会在这着陆啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "有些紧张，但现在\x01",
            "还是要冷静工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "这也多亏拉克斯主任\x01",
            "平时的指导啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_227B")

    Jump("loc_24B7")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_232C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22BE")

    ChrTalk(    #141
        0xFE,
        (
            "定期船停止航行了，\x01",
            "不过王国军的飞船来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2329")

    label("loc_22BE")


    ChrTalk(    #142
        0xFE,
        (
            "定期船停止航行了，\x01",
            "不过王国军的飞船来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "虽然已经提前做了准备，\x01",
            "但对定期船来说还是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2329")

    Jump("loc_24B7")

    label("loc_232C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_23B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2366")

    ChrTalk(    #144
        0xFE,
        (
            "刚、刚才飞过去\x01",
            "的那个怪物是什么！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B5")

    label("loc_2366")


    ChrTalk(    #145
        0xFE,
        (
            "刚、刚才飞过去\x01",
            "的那个怪物是什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "简、简直和定期船\x01",
            "一样大啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_23B5")

    Jump("loc_24B7")

    label("loc_23B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(    #147
        0xFE,
        (
            "好，总算是把\x01",
            "『赛希莉亚号』送上天了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "定期船从着陆到出航\x01",
            "的时间很短，真是麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2425")


    ChrTalk(    #149
        0xFE,
        (
            "『赛希莉亚号』\x01",
            "按原定时间出航……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "各种设备没有异常…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "好！这次也要\x01",
            "准时起飞才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "定期船从着陆到出航\x01",
            "的时间很短，真是麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_24B7")

    TalkEnd(0x1A)
    Return()

    # Function_8_1EC3 end

    def Function_9_24BB(): pass

    label("Function_9_24BB")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_25FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2517")

    ChrTalk(    #153
        0xFE,
        (
            "我以后也许\x01",
            "还会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "各位，如果方便的话，\x01",
            "请代我向她问好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FA")

    label("loc_2517")


    ChrTalk(    #155
        0xFE,
        (
            "啊，各位…\x01",
            "谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1011F啊～莉拉的婶婶……\x02\x03",

            "您要回自治州了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #157
        0xFE,
        (
            "嗯，虽然离开她有些寂寞，\x01",
            "但我的目的已经达到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "请代我向莉拉\x01",
            "问好吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1006F嗯……\x02\x03",

            "也向您全家问好哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "好的，那么再见啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_25FA")

    TalkEnd(0x1D)
    Return()

    # Function_9_24BB end

    def Function_10_25FE(): pass

    label("Function_10_25FE")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2659")

    ChrTalk(    #161
        0xFE,
        (
            "真是的，定期船\x01",
            "到底什么时候才能起飞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "啊～～已经等得\x01",
            "急死了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2686")

    label("loc_2659")


    ChrTalk(    #163
        0xFE,
        (
            "真是的，定期船\x01",
            "到底什么时候才能起飞啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2686")

    TalkEnd(0x1E)
    Return()

    # Function_10_25FE end

    def Function_11_268A(): pass

    label("Function_11_268A")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_26D8")

    ChrTalk(    #164
        0xFE,
        "我就在这里一直等吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "这样要能起飞的话\x01",
            "马上就可以知道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2750")

    label("loc_26D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272D")

    ChrTalk(    #166
        0xFE,
        (
            "真是的……\x01",
            "要等到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "我可是急着\x01",
            "要回卢安呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2750")

    label("loc_272D")


    ChrTalk(    #168
        0xFE,
        (
            "真是的……\x01",
            "要等到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2750")

    TalkEnd(0x1F)
    Return()

    # Function_11_268A end

    def Function_12_2754(): pass

    label("Function_12_2754")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")

    ChrTalk(    #169
        0xFE,
        "似乎是原因不明的故障。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "虽然使用了这么多年，\x01",
            "但还是第一次遇到。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_27F5")

    label("loc_27AE")


    ChrTalk(    #171
        0xFE,
        "似乎是原因不明的故障。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "导力器无法运转，\x01",
            "或许也是同样原因吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F5")

    TalkEnd(0x20)
    Return()

    # Function_12_2754 end

    def Function_13_27F9(): pass

    label("Function_13_27F9")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2845")

    ChrTalk(    #173
        0xFE,
        (
            "真头疼啊…\x01",
            "竟然会被困在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "孩子也在一起…\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_286C")

    label("loc_2845")


    ChrTalk(    #175
        0xFE,
        (
            "真头疼啊…\x01",
            "竟然会被困在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286C")

    TalkEnd(0x21)
    Return()

    # Function_13_27F9 end

    def Function_14_2870(): pass

    label("Function_14_2870")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B4")

    ChrTalk(    #176
        0xFE,
        (
            "喂，那船\x01",
            "到底怎么了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "为什么还不出发？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_28D1")

    label("loc_28B4")


    ChrTalk(    #178
        0xFE,
        (
            "喂，那船\x01",
            "到底怎么了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D1")

    TalkEnd(0x22)
    Return()

    # Function_14_2870 end

    def Function_15_28D5(): pass

    label("Function_15_28D5")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292C")

    ChrTalk(    #179
        0xFE,
        (
            "没想到定期船\x01",
            "它不能动了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "真是没办法，\x01",
            "接下来还有工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2951")

    label("loc_292C")


    ChrTalk(    #181
        0xFE,
        (
            "真是没办法，\x01",
            "接下来还有工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2951")

    TalkEnd(0x23)
    Return()

    # Function_15_28D5 end

    def Function_16_2955(): pass

    label("Function_16_2955")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F0")

    ChrTalk(    #182
        0xFE,
        (
            "呼，和我想的一样，\x01",
            "船没有任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "引擎停止运转\x01",
            "也是和之前那些现象相同吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "……完全束手无策了。\x01",
            "我们什么也做不了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_2A4E")

    label("loc_29F0")


    ChrTalk(    #185
        0xFE,
        (
            "引擎停止运转\x01",
            "也是和之前那些现象相同吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "所以我们完全束手无策了。\x01",
            "我们什么也做不了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4E")

    Jump("loc_2B6D")

    label("loc_2A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF5")

    ChrTalk(    #187
        0xFE,
        (
            "这次完全不是故障，\x01",
            "以前的解决方法全都没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "这里的梯子也准备了紧急时刻用的\x01",
            "手摇伸缩设备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "希望客人们也能多了解\x01",
            "一些导力原理啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_2B6D")

    label("loc_2AF5")


    ChrTalk(    #190
        0xFE,
        (
            "呼，不管怎么说，\x01",
            "故障在起飞前出现还算是幸运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "如果要是飞到一半时遇到这种情况的话，\x01",
            "现在大家就都要去见女神了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6D")

    TalkEnd(0x24)
    Return()

    # Function_16_2955 end

    def Function_17_2B71(): pass

    label("Function_17_2B71")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD9")

    ChrTalk(    #192
        0xFE,
        (
            "定期船的恢复看来\x01",
            "是个很麻烦的问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "各位维修员也都\x01",
            "在抱着头烦恼。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2C31")

    label("loc_2BD9")


    ChrTalk(    #194
        0xFE,
        (
            "定期船的恢复看来\x01",
            "是个很麻烦的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "公社那边现在已经正在考虑\x01",
            "什么对策了吧…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C31")

    Jump("loc_2D49")

    label("loc_2C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF1")

    ChrTalk(    #196
        0xFE,
        (
            "停在这里的是\x01",
            "今天早上的航班…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "如果故障严重的话，\x01",
            "就没法出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "幸好客人们都没受伤，\x01",
            "还是值得高兴的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "如果起飞之后再遇到故障的话，\x01",
            "那可就不得了了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2D49")

    label("loc_2CF1")


    ChrTalk(    #200
        0xFE,
        (
            "停在这里的是\x01",
            "今天早上的航班…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "航行到底要到什么时候才能恢复，\x01",
            "我们也不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D49")

    TalkEnd(0x25)
    Return()

    # Function_17_2B71 end

    def Function_18_2D4D(): pass

    label("Function_18_2D4D")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCD")

    ChrTalk(    #202
        0xFE,
        (
            "定购的商品今天\x01",
            "本来可以收到的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "可是定期船停运了。\x01",
            "呼～真没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "只能赶快去找替代用\x01",
            "的商品了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_2E17")

    label("loc_2DCD")


    ChrTalk(    #205
        0xFE,
        (
            "定购的商品今天\x01",
            "本来可以收到的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "只能赶快去找替代用\x01",
            "的商品了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E17")

    TalkEnd(0x26)
    Return()

    # Function_18_2D4D end

    def Function_19_2E1B(): pass

    label("Function_19_2E1B")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED0")

    ChrTalk(    #207
        0xFE,
        (
            "呼呼……\x01",
            "定期船停运了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "导力器停了，\x01",
            "船不能动也是当然的啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "不过，真让人头疼啊。\x01",
            "这样的话，就没办法做货物输出工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "只能在当地\x01",
            "找找买家了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_2F26")

    label("loc_2ED0")


    ChrTalk(    #211
        0xFE,
        (
            "定期船无法航行了，\x01",
            "货物输出工作也就没法做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "现在也只能在当地\x01",
            "找找买家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F26")

    TalkEnd(0x27)
    Return()

    # Function_19_2E1B end

    def Function_20_2F2A(): pass

    label("Function_20_2F2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    OP_6D(76390, 30000, 24550, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    StopSound(0xA410, 0x3D090, 0x0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0x28, 62250, 10650, 41990, 0)
    OP_6F(0x7, 60)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62250, 5650, 41990, 0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 100)
    SetChrFlags(0x1A, 0x80)
    OP_22(0x79, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x16)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    WaitChrThread(0x28, 0x0)
    OP_48()
    Fade(1000)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_6D(55790, 1500, 37990, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    OP_71(0xB, 0x4)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0x7, 411)
    OP_70(0x7, 0x1C2)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x7)
    OP_43(0xE, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xF, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x10, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x11, 0x1, 0x0, 0x15)
    Sleep(1200)
    OP_43(0x12, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xB, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xA, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x15)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_2F2A end

    def Function_21_312C(): pass

    label("Function_21_312C")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 62290, 1600, 42020, 180)
    OP_8E(0xFE, 0xF352, 0x5DC, 0x93EE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xDD72, 0x5DC, 0x93EE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xC0F8, 0x5DC, 0x93EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC0F8, 0x0, 0x6018, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_21_312C end

    def Function_22_31A7(): pass

    label("Function_22_31A7")


    def lambda_31AD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_31AD)

    def lambda_31C8():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_31C8)
    Sleep(100)

    def lambda_31E8():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_31E8)

    def lambda_3203():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3203)
    Sleep(100)

    def lambda_3223():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3223)

    def lambda_323E():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_323E)
    Sleep(100)

    def lambda_325E():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_325E)
    Sleep(100)

    def lambda_327B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_327B)

    def lambda_3296():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3296)
    Sleep(100)

    def lambda_32B6():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_32B6)

    def lambda_32D1():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_32D1)
    Sleep(100)

    def lambda_32F1():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_32F1)

    def lambda_330C():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_330C)
    Sleep(100)

    def lambda_332C():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_332C)

    def lambda_3347():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3347)
    Sleep(100)

    def lambda_3367():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3367)

    def lambda_3382():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3382)
    Sleep(100)

    def lambda_33A2():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_33A2)

    def lambda_33BD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_33BD)
    Sleep(100)

    def lambda_33DD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_33DD)
    Sleep(3200)

    def lambda_33FD():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_33FD)

    def lambda_3418():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3418)
    Sleep(200)

    def lambda_3438():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3438)

    def lambda_3453():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3453)
    Sleep(200)

    def lambda_3473():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3473)

    def lambda_348E():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_348E)
    Sleep(200)

    def lambda_34AE():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_34AE)

    def lambda_34C9():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_34C9)
    Sleep(200)

    def lambda_34E9():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_34E9)

    def lambda_3504():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_3504)
    Sleep(200)

    def lambda_3524():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3524)

    def lambda_353F():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_353F)
    Sleep(200)

    def lambda_355F():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_355F)

    def lambda_357A():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_357A)
    Sleep(200)

    def lambda_359A():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_359A)

    def lambda_35B5():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_35B5)
    Sleep(100)

    def lambda_35D5():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_35D5)

    def lambda_35F0():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_35F0)
    Sleep(100)

    def lambda_3610():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3610)

    def lambda_362B():
        OP_8F(0xFE, 0xF32A, 0xFFFFE9EE, 0xA406, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_362B)
    WaitChrThread(0x28, 0x1)
    WaitChrThread(0x29, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62250, -5650, 41990, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_B0(0x7, 0x3C)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x1)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_70(0xA, 0xC8)
    Sleep(2500)
    OP_44(0x101, 0x1)
    Return()

    # Function_22_31A7 end

    def Function_23_36B2(): pass

    label("Function_23_36B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36BF")
    Return()

    label("loc_36BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD6")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36EC")
    Call(0, 38)
    Call(0, 39)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_36EC")

    OP_A2(0x1A1D)
    Fade(1000)
    Call(0, 34)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 49200, 250, 25720, 0)
    SetChrPos(0x103, 48730, 0, 24660, 0)
    SetChrPos(0x105, 49640, 0, 24560, 0)
    SetChrPos(0x108, 48740, 0, 23580, 0)
    SetChrPos(0x104, 49910, 0, 23460, 0)

    def lambda_3790():
        OP_8E(0xFE, 0xC030, 0x5DC, 0x8322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3790)
    Sleep(300)

    def lambda_37B0():
        OP_8E(0xFE, 0xBE5A, 0x5DC, 0x7EB7, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37B0)
    Sleep(70)

    def lambda_37D0():
        OP_8E(0xFE, 0xC2EC, 0x5DC, 0x7ED6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37D0)
    Sleep(300)

    def lambda_37F0():
        OP_8E(0xFE, 0xBE64, 0x5DC, 0x7A76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37F0)
    Sleep(80)

    def lambda_3810():
        OP_8E(0xFE, 0xC2F6, 0x5DC, 0x7A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3810)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    StopSound(0xA410, 0x38270, 0x1770)

    def lambda_384A():
        OP_6D(53530, 1500, 39100, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384A)

    def lambda_3862():
        OP_67(0, 8530, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3862)

    def lambda_387A():
        OP_6B(4300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_387A)

    def lambda_388A():
        OP_6E(431, 6000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_388A)
    Sleep(1500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(1500)
    OP_8C(0x101, 45, 400)
    Sleep(3000)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x1)
    Fade(1000)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #213
        0x101,
        (
            "#1015F嗯～军队的飞艇\x01",
            "好像还没来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_399B")

    ChrTalk(    #214
        0x103,
        (
            "#020F想买东西的话\x01",
            "现在倒是还有时间…\x02\x03",

            "怎么办呢？艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A33")

    label("loc_399B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(    #215
        0x108,
        (
            "#070F想买东西的话\x01",
            "现在倒是还有时间…\x02\x03",

            "怎么办？艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A33")

    label("loc_39F3")


    ChrTalk(    #216
        0x103,
        (
            "#020F想买东西的话\x01",
            "现在倒是还有时间…\x02\x03",

            "怎么办呢？艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A33")

    OP_8C(0x101, 180, 400)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【等待军舰到来】\x01",      # 0
            "【先回到街上】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B96")

    ChrTalk(    #217
        0x101,
        (
            "#1006F嗯～还是先回街上\x01",
            "买些东西吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 35)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 50090, 0, 24550, 180)
    SetChrPos(0x103, 50090, 0, 24550, 180)
    SetChrPos(0x104, 50090, 0, 24550, 180)
    SetChrPos(0x105, 50090, 0, 24550, 180)
    SetChrPos(0x108, 50090, 0, 24550, 180)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_30(0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Jump("loc_3BD3")

    label("loc_3B96")


    ChrTalk(    #218
        0x101,
        (
            "#1006F那么，就在这里\x01",
            "等军舰到来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 24)

    label("loc_3BD3")

    Jump("loc_3E22")

    label("loc_3BD6")

    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_3BF4"),
        (2, "loc_3C20"),
        (3, "loc_3C48"),
        (4, "loc_3C74"),
        (7, "loc_3CA9"),
        (SWITCH_DEFAULT, "loc_3CD9"),
    )


    label("loc_3BF4")


    ChrTalk(    #219
        0x101,
        (
            "#1015F在１０点之前\x01",
            "都算是空闲时间…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3C20")

    TurnDirection(0x103, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #220
        0x103,
        "#023F啊，还有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3C48")

    TurnDirection(0x104, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #221
        0x104,
        "#033F啊，还有别的事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3C74")

    TurnDirection(0x105, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #222
        0x105,
        (
            "#040F军舰马上就要来了，\x01",
            "等等吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3CA9")

    TurnDirection(0x108, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #223
        0x108,
        "#073F喂，没有别的事情了吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3CD9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【等待军舰到来】\x01",      # 0
            "【先回到街上】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DDC")
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 50090, 0, 24550, 180)
    SetChrPos(0x103, 50090, 0, 24550, 180)
    SetChrPos(0x104, 50090, 0, 24550, 180)
    SetChrPos(0x105, 50090, 0, 24550, 180)
    SetChrPos(0x108, 50090, 0, 24550, 180)
    OP_0D()
    Jump("loc_3E22")

    label("loc_3DDC")

    FadeToBright(300, 0)

    ChrTalk(    #224
        0x101,
        (
            "#1006F那么，就在这里\x01",
            "等军舰到来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 24)

    label("loc_3E22")

    EventEnd(0x0)
    Return()

    # Function_23_36B2 end

    def Function_24_3E25(): pass

    label("Function_24_3E25")

    EventBegin(0x0)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_6D(50030, 1500, 34090, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(107000, 0)
    OP_6E(282, 0)
    SetChrPos(0x101, 51300, 1500, 34000, 270)
    SetChrPos(0x8, 50450, 1500, 32850, 315)
    SetChrPos(0xA, 50510, 1500, 35270, 225)
    SetChrPos(0x9, 48710, 1500, 33730, 45)
    SetChrPos(0xD, 48780, 1500, 35090, 135)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #225
        0x101,
        (
            "#1011F#5P来接我们的军用飞艇\x01",
            "一定是艘很威风的装甲艇吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xA,
        (
            "#040F你是说警备飞艇吗。\x02\x03",

            "那是当然的，\x01",
            "因为那是军队主力飞行舰艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x8,
        (
            "#026F火力、装载量、机动性\x01",
            "全都无比优秀的\x01",
            "王国军用飞艇…\x02\x03",

            "#020F在１０年前开发出来之后\x01",
            "也经过了多次改良，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xA,
        (
            "#047F是的，除了基本性能做了强化外，\x01",
            "还追加了各种\x01",
            "新装甲和武器。\x02\x03",

            "#040F巡哨机、侦察机、攻击机……\x02\x03",

            "在不断的改进之下，\x01",
            "如今已经组建了一支\x01",
            "性能全面的舰队了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xD,
        (
            "#070F#6P嗯……\x01",
            "不愧是飞船的先进国家啊！\x02\x03",

            "#075F共和国虽然也有飞行舰队，\x01",
            "不过完全就是纸老虎呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        (
            "#035F呵呵，我们帝国也是一样。\x02\x03",

            "#030F虽然也有飞行舰队，\x01",
            "但主力军毕竟还是战车部队。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    OP_20(0xBB8)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #231
        (
            "\x07\x05──王国军所属舰艇\x01",
            "即将在第一飞船坪降落。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #232
        (
            "\x07\x05请无关人员\x01",
            "迅速撤离。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #233
        0x101,
        "#1006F喔！来了吗？\x02",
    )

    CloseMessageWindow()
    OP_22(0x125, 0x1, 0x14)
    Sleep(400)
    OP_24(0x125, 0x1E)
    Sleep(400)
    OP_24(0x125, 0x28)
    Sleep(400)
    OP_24(0x125, 0x32)
    Sleep(400)
    OP_24(0x125, 0x3C)
    Sleep(400)
    OP_24(0x125, 0x46)
    Sleep(400)
    OP_24(0x125, 0x50)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x101,
        (
            "#1015F啊，那个？\x02\x03",

            "那种引擎的声音\x01",
            "我好像从没听过呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        "#044F这是……\x02",
    )

    CloseMessageWindow()

    def lambda_428F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_428F)
    Sleep(100)

    def lambda_42A2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_42A2)
    Sleep(100)

    def lambda_42B5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_42B5)
    Sleep(100)

    def lambda_42C8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_42C8)
    Sleep(100)
    OP_8C(0xD, 45, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #236
        0x101,
        "#1004F#4P啊！\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x100000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3E25 end

    def Function_25_431D(): pass

    label("Function_25_431D")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    OP_6D(76390, 30000, 28060, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 51120, 1800, 37530, 90)
    SetChrPos(0x8, 49540, 1500, 37920, 90)
    SetChrPos(0x9, 49180, 1500, 36690, 90)
    SetChrPos(0xA, 50880, 1800, 38460, 90)
    SetChrPos(0xD, 49140, 1500, 38860, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    StopSound(0xA410, 0x3D090, 0x0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 251)
    SetChrPos(0x28, 62500, 17500, 44000, 0)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62500, -2000, 44000, 0)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 100)
    OP_71(0xB, 0x4)
    FadeToBright(1000, 0)
    Call(0, 33)
    Fade(500)
    OP_6D(51270, 1800, 38190, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    StopSound(0xA410, 0x222E0, 0x0)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_70(0xA, 0xC8)
    Sleep(2500)

    ChrTalk(    #237
        0x101,
        (
            "#1008F#6P啊、啊哈哈……\x02\x03",

            "我们要乘坐的飞船\x01",
            "竟然是『埃尔赛尤』吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xA,
        (
            "#044F#6P昨天和尤莉亚联络的时候\x01",
            "她并没有说过啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 62300, 1500, 38740, 270)
    SetChrPos(0x15, 62370, 1500, 40090, 270)
    SetChrChipByIndex(0x15, 17)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x7, 1888)
    OP_70(0x7, 0x758)
    OP_73(0x7)
    Sleep(500)

    NpcTalk(    #239
        0x14,
        "男人的声音",
        "#3P哟～艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #240
        0x15,
        "女孩的声音",
        "#3P好久不见了～大家！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4682():
        OP_6D(55520, 1500, 39550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4682)

    def lambda_469A():
        OP_67(0, 5390, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_469A)

    def lambda_46B2():
        OP_6B(4040, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_46B2)

    def lambda_46C2():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_46C2)

    def lambda_46D2():
        OP_6E(236, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_46D2)

    def lambda_46E2():

        label("loc_46E2")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_46E2")

    QueueWorkItem2(0x101, 1, lambda_46E2)

    def lambda_46F3():

        label("loc_46F3")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_46F3")

    QueueWorkItem2(0x8, 1, lambda_46F3)

    def lambda_4704():

        label("loc_4704")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_4704")

    QueueWorkItem2(0x9, 1, lambda_4704)

    def lambda_4715():

        label("loc_4715")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_4715")

    QueueWorkItem2(0xA, 1, lambda_4715)

    def lambda_4726():

        label("loc_4726")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_4726")

    QueueWorkItem2(0xD, 1, lambda_4726)

    def lambda_4737():
        OP_8E(0xFE, 0xE68C, 0x5DC, 0x97C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4737)
    Sleep(500)

    def lambda_4757():
        OP_8E(0xFE, 0xE77C, 0x5DC, 0x9C04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4757)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x101, 400)
    WaitChrThread(0x15, 0x1)
    TurnDirection(0x15, 0x101, 400)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)

    ChrTalk(    #241
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        "#023F#6P你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x14,
        (
            "#141F#2P嘿嘿，真是\x01",
            "奇妙的再会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x15,
        (
            "#151F#2P请多关照啊～\x01",
            "艾丝蒂尔和大家！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1004F#6P为、为、为……\x02\x03",

            "为什么奈尔和朵洛希\x01",
            "也会在埃尔赛尤号上！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x16, 62600, 1500, 42300, 180)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x80)
    Sleep(500)

    NpcTalk(    #246
        0x16,
        "女性的声音",
        (
            "#7P……由我来\x01",
            "做个说明吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48CC():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48CC)

    def lambda_48DA():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_48DA)

    def lambda_48E8():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_48E8)

    def lambda_48F6():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_48F6)

    def lambda_4904():
        TurnDirection(0xFE, 0x16, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4904)

    def lambda_4912():

        label("loc_4912")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_4912")

    QueueWorkItem2(0x101, 1, lambda_4912)

    def lambda_4923():

        label("loc_4923")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_4923")

    QueueWorkItem2(0xA, 1, lambda_4923)

    def lambda_4934():

        label("loc_4934")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_4934")

    QueueWorkItem2(0xD, 1, lambda_4934)

    def lambda_4945():

        label("loc_4945")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_4945")

    QueueWorkItem2(0x14, 1, lambda_4945)

    def lambda_4956():

        label("loc_4956")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_4956")

    QueueWorkItem2(0x15, 1, lambda_4956)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    OP_8E(0x16, 0xF488, 0x5DC, 0x9AE2, 0x7D0, 0x0)
    OP_8E(0x16, 0xE86C, 0x5DC, 0x93EE, 0x7D0, 0x0)
    OP_8E(0x16, 0xE100, 0x5DC, 0x93EE, 0x7D0, 0x0)
    TurnDirection(0x16, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)

    def lambda_49C8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_49C8)
    Sleep(100)

    def lambda_49DB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_49DB)

    ChrTalk(    #247
        0x101,
        "#1004F#6P啊，尤莉亚小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xA,
        (
            "#542F#6P尤莉亚……怎么回事。\x02\x03",

            "你昨天也没有告诉过我\x01",
            "埃尔赛尤号会来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x16,
        (
            "#171F#2P呵呵，为了给殿下一个惊喜，\x01",
            "所以故意保密了。\x02\x03",

            "还请您原谅啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "#045F#6P尤莉亚……你真是的。\x02\x03",

            "#048F不过使用『埃尔赛尤』\x01",
            "是祖母大人的意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x16,
        "#170F#2P嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1008F#6P啊……\x01",
            "为什么女王陛下会……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x16,
        (
            "#176F#2P将知名的最新战舰投入使用的话，\x01",
            "可以缓解人们因巨龙出现\x01",
            "而产生的恐惧和不安…\x02\x03",

            "#170F正是出于这种考虑才会下达此决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1006F#6P啊，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x9,
        (
            "#031F#6P呼，不愧是艾莉茜雅陛下啊。\x02\x03",

            "#030F那几位记者的同行\x01",
            "也是因为这个理由吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x14,
        (
            "#141F#2P嗯，没错。\x02\x03",

            "这次龙的出现\x01",
            "给大家带来的恐慌实在是非同寻常。\x02\x03",

            "所以要通过我们的报道来\x01",
            "避免国民们的不安和动摇。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x14, 400)

    ChrTalk(    #257
        0x16,
        "#178F#6P奈尔先生，还请您……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x16, 400)
    Sleep(500)

    ChrTalk(    #258
        0x14,
        (
            "#147F#5P我知道啦～～\x01",
            "机密的事情我是不会写出来的！\x02\x03",

            "#140F不过，为了保证公正，\x01",
            "还请让我进行深入些的调查啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x16,
        "#176F#6P……明白了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x17, 62600, 1500, 42300, 180)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x80)

    NpcTalk(    #260
        0x17,
        "老人的声音",
        (
            "#7P呼……\x01",
            "你们来得很准时啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4E64():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E64)

    def lambda_4E72():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4E72)

    def lambda_4E80():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E80)

    def lambda_4E8E():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4E8E)

    def lambda_4E9C():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4E9C)

    def lambda_4EAA():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4EAA)

    def lambda_4EB8():

        label("loc_4EB8")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4EB8")

    QueueWorkItem2(0x101, 1, lambda_4EB8)

    def lambda_4EC9():

        label("loc_4EC9")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4EC9")

    QueueWorkItem2(0xA, 1, lambda_4EC9)

    def lambda_4EDA():

        label("loc_4EDA")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4EDA")

    QueueWorkItem2(0xD, 1, lambda_4EDA)

    def lambda_4EEB():

        label("loc_4EEB")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4EEB")

    QueueWorkItem2(0x14, 1, lambda_4EEB)

    def lambda_4EFC():

        label("loc_4EFC")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4EFC")

    QueueWorkItem2(0x15, 1, lambda_4EFC)

    def lambda_4F0D():

        label("loc_4F0D")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4F0D")

    QueueWorkItem2(0x16, 1, lambda_4F0D)
    OP_43(0x17, 0x0, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x16, 0x0, 0x0, 0x1C)
    WaitChrThread(0x17, 0x0)
    OP_44(0xA, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)

    def lambda_4F46():
        OP_8C(0x14, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F46)

    def lambda_4F54():
        OP_8C(0x15, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F54)

    def lambda_4F62():
        OP_8C(0x16, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4F62)

    ChrTalk(    #261
        0x101,
        "#1004F#6P啊，摩尔根将军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x8,
        (
            "#027F#6P您能允许我们同行，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x17,
        (
            "#163F#2P哼，这也是女王陛下\x01",
            "的意思。\x02\x03",

            "#160F为了不让你们误会，我话说在前。\x01",
            "你们这次只不过\x01",
            "是同行者而已。\x02\x03",

            "参加作战的基本还是我们，\x01",
            "你们只要老老实实地旁观就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#6P嗯，没问题。\x02\x03",

            "如果军队能顺利完成任务的话，\x01",
            "我们自然不会有什么意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xD,
        (
            "#071F#6P让我们好好欣赏\x01",
            "一场漂亮的战斗吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x17,
        (
            "#163F#2P呼……好了。\x02\x03",

            "#160F公主殿下，请到这边来。\x01",
            "我来给您做向导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xA,
        "#043F#6P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x17,
        (
            "#160F#2P这是王室的船，总不能让您\x01",
            "以客人的身份乘坐。\x02\x03",

            "那样会影响到大家的士气的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xA,
        "#047F#3P……我明白了。\x02",
    )

    CloseMessageWindow()
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xA, 0x0, 0x0, 0x1D)
    Sleep(1000)

    def lambda_51DA():
        OP_6D(56780, 1800, 39570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51DA)
    OP_43(0x17, 0x0, 0x0, 0x1E)

    def lambda_51F9():

        label("loc_51F9")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_51F9")

    QueueWorkItem2(0x14, 1, lambda_51F9)

    def lambda_520A():

        label("loc_520A")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_520A")

    QueueWorkItem2(0x15, 1, lambda_520A)

    def lambda_521B():

        label("loc_521B")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_521B")

    QueueWorkItem2(0x16, 1, lambda_521B)
    Sleep(5000)

    ChrTalk(    #270
        0x101,
        (
            "#1007F#6P呼～将军还是\x01",
            "和以前一个样子啊。\x02\x03",

            "#1019F真是的，为什么就不能\x01",
            "认同我们游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    OP_8C(0x16, 270, 400)
    Sleep(500)

    ChrTalk(    #271
        0x16,
        (
            "#171F#2P呵呵，那种顽固的老人家，\x01",
            "要是态度突然转变了\x01",
            "那才让人觉得奇怪呢。\x02\x03",

            "各位的向导\x01",
            "就由我来担任吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 315, 400)

    def lambda_5320():
        OP_6D(55700, 1500, 38800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5320)

    def lambda_5338():
        OP_6B(3800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5338)

    def lambda_5348():
        OP_8E(0xFE, 0xE100, 0x5DC, 0x93EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5348)
    Sleep(100)

    def lambda_5368():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5368)
    Sleep(100)

    def lambda_537B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_537B)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 270, 400)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x16, 18)
    Sleep(100)
    OP_99(0x16, 0x0, 0x1, 0x5DC)
    Sleep(500)

    ChrTalk(    #272
        0x16,
        (
            "#178F#2P那么──\x01",
            "欢迎你们！各位游击士！\x02\x03",

            "欢迎登上王室亲卫队所属的\x01",
            "巡洋舰『埃尔赛尤』！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x75, 0x0, 0x64)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_6F(0x7, 1)
    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    FadeToBright(1500, 0)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 200)
    OP_70(0xA, 0x64)
    Sleep(2500)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x28, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_5537():
        OP_6D(59670, 1800, 67060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5537)

    def lambda_554F():
        OP_67(0, 8260, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_554F)

    def lambda_5567():
        OP_6B(3830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5567)

    def lambda_5577():
        OP_6C(204000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5577)

    def lambda_5587():
        OP_6E(593, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5587)

    def lambda_5597():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_5597)

    def lambda_55AD():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_55AD)
    Sleep(400)

    def lambda_55C8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_55C8)

    def lambda_55DE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_55DE)
    Sleep(400)

    def lambda_55F9():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_55F9)

    def lambda_560F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_560F)
    Sleep(400)

    def lambda_562A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_562A)

    def lambda_5640():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5640)
    Sleep(300)

    def lambda_565B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_565B)

    def lambda_5671():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5671)
    Sleep(300)

    def lambda_568C():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_568C)

    def lambda_56A2():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_56A2)
    Sleep(300)

    def lambda_56BD():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_56BD)

    def lambda_56D3():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_56D3)
    Sleep(300)

    def lambda_56EE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_56EE)

    def lambda_5704():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5704)
    Sleep(200)

    def lambda_571F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_571F)

    def lambda_5735():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5735)
    Sleep(200)

    def lambda_5750():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_5750)

    def lambda_5766():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5766)
    Sleep(200)

    def lambda_5781():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_5781)

    def lambda_5797():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5797)
    Sleep(200)

    def lambda_57B2():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_57B2)

    def lambda_57C8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_57C8)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(49170, 1500, 37540, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 49530, 1500, 28520, 0)
    SetChrPos(0xC, 48750, 1500, 28520, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_0D()

    NpcTalk(    #273
        0xB,
        "青年的声音",
        "#3P来晚了吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0xB, 25)

    def lambda_58E4():
        OP_8E(0xFE, 0xC17A, 0x5DC, 0x9344, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_58E4)
    Sleep(500)
    SetChrChipByIndex(0xC, 26)

    def lambda_5909():
        OP_8E(0xC, 0xBE6E, 0x5DC, 0x925E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5909)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)

    ChrTalk(    #274
        0xC,
        "#065F已、已经飞走了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xB,
        (
            "#551F#5P可恶，要是再早点起床\x01",
            "出发就好了……\x02\x03",

            "#051F没办法，龙的事\x01",
            "就交给艾丝蒂尔她们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #276
        0xC,
        (
            "#560F#4P是、是啊。\x02\x03",

            "#562F可是可是……呜呜呜。\x02\x03",

            "人家好想坐一次\x01",
            "『埃尔赛尤』呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #277
        0xB,
        (
            "#051F#5P怎么回事，\x01",
            "机械瘾又发作了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "#560F#4P可是…\x01",
            "那上面有很多新型装备呢…\x02\x03",

            "可以容纳８个新型引擎的\x01",
            "引擎管道…\x02\x03",

            "拥有高效率处理情报机能\x01",
            "的次世代型运算器…\x02\x03",

            "#067F哈～真是好期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xB,
        (
            "#551F#5P真是的……\x01",
            "两只眼睛又开始发亮了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "#067F#4P嘿嘿……\x02\x03",

            "#064F不过，阿加特哥哥，\x01",
            "我们接下来该怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xB,
        (
            "#053F#5P是啊……\x02\x03",

            "#051F那就先去找把\x01",
            "替代用的重剑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "#063F#4P啊，是吗……\x02\x03",

            "原来那把已经断成那样了，\x01",
            "没办法修理了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xB,
        (
            "#053F#5P嗯，所以只能重新买一把了。\x02\x03",

            "#552F南街区的武器店\x01",
            "应该就有那类武器吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, 49650, 1500, 28520, 0)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x18, 255)

    NpcTalk(    #284
        0x18,
        "青年的声音",
        "#3P阿加特！\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5C8C():
        OP_6D(49650, 1500, 35920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C8C)

    def lambda_5CA4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CA4)
    Sleep(50)

    def lambda_5CB7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5CB7)
    OP_8E(0x18, 0xC094, 0x5DC, 0x8A3E, 0xFA0, 0x0)

    ChrTalk(    #285
        0xB,
        "#052F#6P哟！泰德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xC,
        "#064F接待员哥哥……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x18,
        (
            "#2P啊～还好\x01",
            "赶上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x18,
        (
            "#2P现在导力通信已经恢复了，\x01",
            "你们要和『埃尔赛尤』联络吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xB,
        (
            "#053F#6P啊……不用了。\x02\x03",

            "#051F不过，你是特意跑来\x01",
            "确认我们是否登上船了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x18,
        "#2P啊，其实是一半一半啦，因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x18,
        (
            "#2P昨天在整理最后一批包裹时\x01",
            "发现了一个寄给阿加特你\x01",
            "的快递包裹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        "#052F#6P给我的快递包裹？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x18,
        (
            "#2P嗯，是署名拉赛尔\x01",
            "的小包裹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xB,
        "#055F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xC,
        "#065F爷、爷爷寄来的？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_431D end

    def Function_26_5EA7(): pass

    label("Function_26_5EA7")

    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x96)
    OP_73(0x7)
    OP_6F(0x7, 151)
    OP_70(0x7, 0x14A)
    Sleep(3300)
    OP_75(0x8, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x1)
    Sleep(250)
    OP_74(0x8, 0x0, 0x2)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x3)
    Sleep(250)
    OP_74(0x8, 0x0, 0x4)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x8, 0x0, 0x5)
    Sleep(250)
    OP_74(0x8, 0x0, 0x6)
    Sleep(250)
    OP_74(0x8, 0x0, 0x7)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x1AE)
    Return()

    # Function_26_5EA7 end

    def Function_27_5F5A(): pass

    label("Function_27_5F5A")

    OP_8E(0xFE, 0xF488, 0x5DC, 0x9CA4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE916, 0x5DC, 0x94CA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE006, 0x5DC, 0x93BC, 0x7D0, 0x0)
    Return()

    # Function_27_5F5A end

    def Function_28_5F97(): pass

    label("Function_28_5F97")

    OP_8E(0xFE, 0xE682, 0x5DC, 0x9416, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE718, 0x5DC, 0x9092, 0x7D0, 0x0)
    Return()

    # Function_28_5F97 end

    def Function_29_5FC0(): pass

    label("Function_29_5FC0")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xD21E, 0x5DC, 0x9434, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE9C0, 0x5DC, 0x9498, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF28A, 0x5DC, 0x9C7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF32A, 0x5DC, 0xA348, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_5FC0 end

    def Function_30_601B(): pass

    label("Function_30_601B")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xE9C0, 0x5DC, 0x9498, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF28A, 0x5DC, 0x9C7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF32A, 0x5DC, 0xA348, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_601B end

    def Function_31_6064(): pass

    label("Function_31_6064")

    OP_72(0x7, 0x20)
    OP_73(0x7)
    OP_6F(0x7, 600)
    OP_70(0x7, 0x32A)
    Return()

    # Function_31_6064 end

    def Function_32_607B(): pass

    label("Function_32_607B")

    OP_43(0x101, 0x3, 0x0, 0x1F)
    OP_22(0x79, 0x0, 0x64)

    def lambda_608D():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_608D)

    def lambda_60A8():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_60A8)
    Sleep(100)

    def lambda_60C8():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_60C8)
    Sleep(100)

    def lambda_60E8():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_60E8)
    Sleep(100)

    def lambda_6108():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6108)

    def lambda_6123():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6123)
    Sleep(100)

    def lambda_6140():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6140)
    Sleep(100)

    def lambda_6160():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6160)
    Sleep(100)

    def lambda_6180():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6180)
    Sleep(100)

    def lambda_61A0():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_61A0)
    Sleep(100)

    def lambda_61C0():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_61C0)
    Sleep(100)

    def lambda_61E0():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_61E0)
    Sleep(100)

    def lambda_6200():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6200)
    Sleep(100)

    def lambda_6220():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6220)

    def lambda_623B():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_623B)
    Sleep(3500)

    def lambda_625B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_625B)
    Sleep(100)

    def lambda_627B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_627B)
    Sleep(100)

    def lambda_629B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_629B)
    Sleep(100)

    def lambda_62BB():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_62BB)
    Sleep(100)

    def lambda_62DB():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_62DB)
    Sleep(100)

    def lambda_62FB():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_62FB)
    Sleep(100)

    def lambda_631B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_631B)
    Sleep(100)

    def lambda_633B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_633B)
    Sleep(100)

    def lambda_635B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_635B)
    Sleep(100)

    def lambda_637B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_637B)
    WaitChrThread(0x28, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_44(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Return()

    # Function_32_607B end

    def Function_33_63CE(): pass

    label("Function_33_63CE")

    OP_43(0x101, 0x3, 0x0, 0x1F)
    OP_22(0x125, 0x0, 0x64)

    def lambda_63E0():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_63E0)

    def lambda_63FB():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_63FB)
    Sleep(100)

    def lambda_641B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_641B)
    Sleep(100)

    def lambda_643B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_643B)
    Sleep(100)

    def lambda_645B():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_645B)

    def lambda_6476():
        OP_6D(76390, 20000, 24550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6476)
    Sleep(100)

    def lambda_6493():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6493)
    Sleep(100)

    def lambda_64B3():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_64B3)
    Sleep(100)

    def lambda_64D3():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_64D3)
    Sleep(100)

    def lambda_64F3():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_64F3)
    Sleep(100)

    def lambda_6513():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6513)
    Sleep(100)

    def lambda_6533():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6533)
    Sleep(100)

    def lambda_6553():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6553)
    Sleep(100)

    def lambda_6573():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6573)

    def lambda_658E():
        OP_8F(0xFE, 0xF424, 0xFFFFEC14, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_658E)
    Sleep(3500)

    def lambda_65AE():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_65AE)
    Sleep(100)

    def lambda_65CE():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_65CE)
    Sleep(100)

    def lambda_65EE():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_65EE)
    Sleep(100)

    def lambda_660E():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_660E)
    Sleep(100)

    def lambda_662E():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_662E)
    Sleep(100)

    def lambda_664E():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_664E)
    Sleep(100)

    def lambda_666E():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_666E)
    Sleep(100)

    def lambda_668E():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_668E)
    Sleep(100)

    def lambda_66AE():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_66AE)
    Sleep(100)

    def lambda_66CE():
        OP_8F(0xFE, 0xF424, 0x0, 0xABE0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_66CE)
    WaitChrThread(0x28, 0x1)
    OP_23(0x125)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_44(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Return()

    # Function_33_63CE end

    def Function_34_6721(): pass

    label("Function_34_6721")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6767")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67C1")
    RemoveParty(0x3, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A9")
    AddParty(0x3, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_67C1")

    label("loc_67A9")

    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_67C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_681B")
    RemoveParty(0x4, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6803")
    AddParty(0x4, 0xF9, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_681B")

    label("loc_6803")

    AddParty(0x4, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_681B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_684D")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_684D")

    Return()

    # Function_34_6721 end

    def Function_35_684E(): pass

    label("Function_35_684E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6862")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_6862")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6876")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)

    label("loc_6876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_688A")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_688A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_689E")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_689E")

    Return()

    # Function_35_684E end

    def Function_36_689F(): pass

    label("Function_36_689F")

    EventBegin(0x0)
    OP_6D(66690, 9370, 39660, 0)
    OP_67(0, 45340, -55000, 0)
    OP_6B(900, 0)
    OP_6C(316000, 0)
    OP_6E(403, 0)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x7, 1)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    SetChrFlags(0x1A, 0x80)
    FadeToBright(2000, 0)

    def lambda_691D():
        OP_6D(66900, 7780, 39660, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_691D)

    def lambda_6935():
        OP_67(0, 34090, -55000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6935)
    Sleep(1000)

    def lambda_6952():
        OP_6B(700, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6952)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_36_689F end

    def Function_37_697E(): pass

    label("Function_37_697E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6995")
    Call(0, 38)
    AddParty(0x2, 0xF8, 0xFF)

    label("loc_6995")

    OP_6D(55720, 1500, 38000, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(122000, 0)
    OP_6E(236, 0)
    OP_A1(0x28, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0x28, 62500, 0, 44000, 0)
    OP_6F(0x7, 1)
    OP_A1(0x29, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0x29, 62500, -5100, 44000, 0)
    OP_75(0x8, 0x0, 0x0)
    OP_74(0x8, 0x0, 0x0)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 200)
    OP_71(0xB, 0x4)
    SetChrPos(0x101, 51260, 1800, 37530, 90)
    SetChrPos(0xB, 49290, 1500, 39050, 90)
    SetChrPos(0xC, 49650, 1500, 40020, 135)
    SetChrPos(0x108, 49230, 1500, 36580, 90)
    SetChrPos(0x105, 51230, 1800, 38480, 90)
    SetChrPos(0x103, 49640, 1500, 38070, 90)
    SetChrPos(0x104, 48700, 1500, 37550, 90)
    SetChrPos(0x17, 59050, 1500, 38120, 270)
    SetChrPos(0x16, 59700, 1500, 38870, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x16, 0x4)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 19)
    SetChrSubChip(0x105, 1)
    SetChrFlags(0x1A, 0x80)
    OP_22(0x75, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #296
        0x16,
        (
            "#176F接下来『埃尔赛尤』\x01",
            "要在柏斯上空进行巡航。\x02\x03",

            "#170F找到龙的居所之后\x01",
            "请马上和我们联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        "#1006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x105,
        (
            "#048F#6P找到龙的住处之后\x01",
            "我们会马上让基库帮忙传达的。\x02\x03",

            "我不在的时候\x01",
            "你也要乖乖在艾丝蒂尔身边待着哦，\x01",
            "拜托啦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #299
        0x105,
        "基库",
        "#311F#5P啾⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x17,
        (
            "#163F殿下，如果您要同行的话，\x01",
            "请一定要小心啊！\x02\x03",

            "#160F……艾丝蒂尔·布莱特。\x01",
            "还有阿加特·科洛斯纳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#1004F啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xB,
        "#052F#6P……怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x17,
        (
            "#163F如果龙从峡谷中逃脱的话，\x01",
            "我们军队会负起责任做好最完善的处理的。\x02\x03",

            "无论如何，我也不会让利贝尔的国民\x01",
            "再受到第二次伤害。\x02\x03",

            "#160F所以，你们不要害怕失败，\x01",
            "照你们的意思去做吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1025F摩尔根将军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xB,
        (
            "#051F#6P……你竟然会\x01",
            "说出这样的话来。\x02\x03",

            "难道太阳从西边升起了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x17,
        "#163F哼，这只是场面话而已。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 0, 400)
    Sleep(500)

    ChrTalk(    #307
        0x17,
        "#160F#2P……上尉！出发了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x16,
        "#171F是！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    def lambda_6E59():

        label("loc_6E59")

        TurnDirection(0x101, 0x28, 400)
        OP_48()
        Jump("loc_6E59")

    QueueWorkItem2(0x103, 2, lambda_6E59)

    def lambda_6E6A():

        label("loc_6E6A")

        TurnDirection(0x103, 0x28, 400)
        OP_48()
        Jump("loc_6E6A")

    QueueWorkItem2(0x103, 3, lambda_6E6A)

    def lambda_6E7B():

        label("loc_6E7B")

        TurnDirection(0x105, 0x28, 400)
        OP_48()
        Jump("loc_6E7B")

    QueueWorkItem2(0x105, 3, lambda_6E7B)

    def lambda_6E8C():

        label("loc_6E8C")

        TurnDirection(0x108, 0x28, 400)
        OP_48()
        Jump("loc_6E8C")

    QueueWorkItem2(0x108, 3, lambda_6E8C)

    def lambda_6E9D():

        label("loc_6E9D")

        TurnDirection(0x104, 0x28, 400)
        OP_48()
        Jump("loc_6E9D")

    QueueWorkItem2(0x104, 3, lambda_6E9D)

    def lambda_6EAE():

        label("loc_6EAE")

        TurnDirection(0xB, 0x28, 400)
        OP_48()
        Jump("loc_6EAE")

    QueueWorkItem2(0xB, 3, lambda_6EAE)

    def lambda_6EBF():

        label("loc_6EBF")

        TurnDirection(0xC, 0x28, 400)
        OP_48()
        Jump("loc_6EBF")

    QueueWorkItem2(0xC, 3, lambda_6EBF)
    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0xA, 200)
    OP_70(0xA, 0x64)
    Sleep(2500)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x28, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x28, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x28, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x28, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_6F9E():
        OP_6D(59670, 1800, 67060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F9E)

    def lambda_6FB6():
        OP_67(0, 8260, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FB6)

    def lambda_6FCE():
        OP_6B(3830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6FCE)

    def lambda_6FDE():
        OP_6C(204000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6FDE)

    def lambda_6FEE():
        OP_6E(593, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6FEE)

    def lambda_6FFE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6FFE)

    def lambda_7014():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7014)
    Sleep(400)

    def lambda_702F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_702F)

    def lambda_7045():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7045)
    Sleep(400)

    def lambda_7060():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7060)

    def lambda_7076():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7076)
    Sleep(400)

    def lambda_7091():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7091)

    def lambda_70A7():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_70A7)
    Sleep(300)

    def lambda_70C2():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_70C2)

    def lambda_70D8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_70D8)
    Sleep(300)

    def lambda_70F3():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_70F3)

    def lambda_7109():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7109)
    Sleep(300)

    def lambda_7124():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7124)

    def lambda_713A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_713A)
    Sleep(300)

    def lambda_7155():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7155)

    def lambda_716B():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_716B)
    Sleep(200)

    def lambda_7186():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7186)

    def lambda_719C():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_719C)
    Sleep(200)

    def lambda_71B7():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_71B7)

    def lambda_71CD():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_71CD)
    Sleep(200)

    def lambda_71E8():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_71E8)

    def lambda_71FE():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_71FE)
    Sleep(200)

    def lambda_7219():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_7219)

    def lambda_722F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_722F)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x103, 0x2)
    OP_44(0x103, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x108, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0xB, 0x3)
    OP_44(0xC, 0x3)
    SetChrName("")

    AnonymousTalk(    #309
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择固定队员外的一名同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x1A24)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1103   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_37_697E end

    def Function_38_73AC(): pass

    label("Function_38_73AC")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7426"),
        (1, "loc_742C"),
        (SWITCH_DEFAULT, "loc_7432"),
    )


    label("loc_7426")

    OP_A2(0x1200)
    Jump("loc_7432")

    label("loc_742C")

    OP_A2(0x1201)
    Jump("loc_7432")

    label("loc_7432")

    Return()

    # Function_38_73AC end

    def Function_39_7433(): pass

    label("Function_39_7433")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74E3")
    AddParty(0x2, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_74E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7530")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7518")
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7530")

    label("loc_7518")

    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_7530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_757D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7565")
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_757D")

    label("loc_7565")

    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_757D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_75A2")
    AddParty(0x7, 0xFF, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_75A2")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_39_7433 end

    def Function_40_75B4(): pass

    label("Function_40_75B4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #310
        (
            "\x07\x05定期船飞船坪\x01",
            "≡　前往洛连特市\x01",
            "≡　前往卢安市\x01",
            "≡　前往埃雷波尼亚帝国\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_75B4 end

    def Function_41_762A(): pass

    label("Function_41_762A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #311
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　『利贝尔飞船公社』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_762A end

    def Function_42_7690(): pass

    label("Function_42_7690")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #312
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "   『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_42_7690 end

    def Function_43_770C(): pass

    label("Function_43_770C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7719")
    Return()

    label("loc_7719")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_772B")
    Return()

    label("loc_772B")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x18)"), scpexpr(EXPR_END)), "loc_7766")
    Call(0, 44)
    Jump("loc_780B")

    label("loc_7766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_7775")
    Call(0, 44)
    Jump("loc_780B")

    label("loc_7775")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_77CD")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #313
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_780B")

    label("loc_77CD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #314
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_780B")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_43_770C end

    def Function_44_7812(): pass

    label("Function_44_7812")

    TalkBegin(0x18)

    ChrTalk(    #315
        0x18,
        (
            "嗯，照片上的小女孩\x01",
            "已经想不起来是谁了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x18,
        (
            "很遗憾，大概和飞船坪中\x01",
            "的客人们无关吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x18,
        (
            "可能已经有哪处的人家\x01",
            "将她养育成人了吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_44_7812 end

    SaveToFile()

Try(main)
