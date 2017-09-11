from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0100   ._SN',
            'ED6_DT01/T0100_1 ._SN',
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
        'Aina',                                 # 9
        'Luke',                                 # 10
        'Pat',                                  # 11
        'Claire',                               # 12
        'Freemont',                             # 13
        'Ellie',                                # 14
        'Armand',                               # 15
        'Ellie',                                # 16
        'Armand',                               # 17
        'Yuni',                                 # 18
        'Charles',                              # 19
        'Radmira',                              # 20
        'Ida',                                  # 21
        'Aryll',                                # 22
        'Aryll',                                # 23
        'Professor Alba',                       # 24
        'Nial',                                 # 25
        'Dorothy',                              # 26
        'Scherazard',                           # 27
        'Target Camera',                        # 28
        'Pigeon',                               # 29
        'Pigeon',                               # 30
        'Pigeon',                               # 31
        'Pigeon',                               # 32
        'Pigeon',                               # 33
        "Rolent - Mayor's Residence",           # 34
        'Rolent Landing Port',                  # 35
        'Elize Highway',                        # 36
        'Milch Main Road',                      # 37
        'Malga Trail',                          # 38
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH02560 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01170 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH01690 ._CH',             # 09
        'ED6_DT07/CH02050 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02070 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01700 ._CH',             # 0E
        'ED6_DT07/CH01700 ._CH',             # 0F
        'ED6_DT07/CH00020 ._CH',             # 10
        'ED6_DT07/CH01153 ._CH',             # 11
        'ED6_DT07/CH01143 ._CH',             # 12
        'ED6_DT07/CH01030 ._CH',             # 13
        'ED6_DT07/CH01033 ._CH',             # 14
        'ED6_DT07/CH01730 ._CH',             # 15
        'ED6_DT07/CH01731 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH02560P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01170P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH01690P._CP',             # 09
        'ED6_DT07/CH02050P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02070P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01700P._CP',             # 0E
        'ED6_DT07/CH01700P._CP',             # 0F
        'ED6_DT07/CH00020P._CP',             # 10
        'ED6_DT07/CH01153P._CP',             # 11
        'ED6_DT07/CH01143P._CP',             # 12
        'ED6_DT07/CH01030P._CP',             # 13
        'ED6_DT07/CH01033P._CP',             # 14
        'ED6_DT07/CH01730P._CP',             # 15
        'ED6_DT07/CH01731P._CP',             # 16
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
        X                   = 49900,
        Z                   = 0,
        Y                   = 72100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 46900,
        Z                   = 0,
        Y                   = 74100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 30422,
        Z                   = 0,
        Y                   = 40087,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 51829,
        Z                   = 0,
        Y                   = 35208,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 29979,
        Z                   = 0,
        Y                   = 17921,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 31832,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 36305,
        Z                   = 100,
        Y                   = 46015,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 39160,
        Z                   = 80,
        Y                   = 47020,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x12,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 72160,
        Z                   = 0,
        Y                   = 18851,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 62400,
        Z                   = 250,
        Y                   = 22000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 33500,
        Z                   = 0,
        Y                   = 45800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 39420,
        Z                   = 250,
        Y                   = 51560,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x115,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 38700,
        Z                   = 0,
        Y                   = 50720,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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
        Z                   = 0,
        Y                   = 80870,
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
        X                   = 44000,
        Y                   = 0,
        Z                   = 12250,
        Range               = 54000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2710,
        Unknown_18          = 0x0,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 18000,
        Y                   = 0,
        Z                   = 44000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x9088,
        Unknown_18          = 0x0,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = 25000,
        Y                   = 0,
        Z                   = 72000,
        Range               = 31000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x11364,
        Unknown_18          = 0x0,
        Unknown_1C          = 64,
    )

    DeclEvent(
        X                   = 55000,
        Y                   = -1000,
        Z                   = 57200,
        Range               = 61500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDB88,
        Unknown_18          = 0x10000,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 42000,
        Y                   = -1000,
        Z                   = 34400,
        Range               = 54000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8278,
        Unknown_18          = 0x10000,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 60900,
        Y                   = -1000,
        Z                   = 35800,
        Range               = 61900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAFC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 61850,
        Y                   = -1000,
        Z                   = 30150,
        Range               = 66550,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7DC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 80,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 82,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 83,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 84,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45000,
        TriggerZ            = 0,
        TriggerY            = 25400,
        TriggerRange        = 500,
        ActorX              = 45000,
        ActorZ              = 0,
        ActorY              = 25400,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 75,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 76,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_85E",          # 00, 0
        "Function_1_D0E",          # 01, 1
        "Function_2_E63",          # 02, 2
        "Function_3_FE0",          # 03, 3
        "Function_4_1119",         # 04, 4
        "Function_5_1252",         # 05, 5
        "Function_6_1276",         # 06, 6
        "Function_7_12F4",         # 07, 7
        "Function_8_1338",         # 08, 8
        "Function_9_1383",         # 09, 9
        "Function_10_13B3",        # 0A, 10
        "Function_11_15B6",        # 0B, 11
        "Function_12_172B",        # 0C, 12
        "Function_13_1F6D",        # 0D, 13
        "Function_14_23CE",        # 0E, 14
        "Function_15_433F",        # 0F, 15
        "Function_16_4BA1",        # 10, 16
        "Function_17_4D8F",        # 11, 17
        "Function_18_5095",        # 12, 18
        "Function_19_5435",        # 13, 19
        "Function_20_5986",        # 14, 20
        "Function_21_6149",        # 15, 21
        "Function_22_67BA",        # 16, 22
        "Function_23_67C9",        # 17, 23
        "Function_24_67D8",        # 18, 24
        "Function_25_67E7",        # 19, 25
        "Function_26_6811",        # 1A, 26
        "Function_27_6DB0",        # 1B, 27
        "Function_28_7C1D",        # 1C, 28
        "Function_29_8623",        # 1D, 29
        "Function_30_8644",        # 1E, 30
        "Function_31_866E",        # 1F, 31
        "Function_32_8678",        # 20, 32
        "Function_33_8682",        # 21, 33
        "Function_34_89CF",        # 22, 34
        "Function_35_89EF",        # 23, 35
        "Function_36_8A0F",        # 24, 36
        "Function_37_8A16",        # 25, 37
        "Function_38_9684",        # 26, 38
        "Function_39_96E6",        # 27, 39
        "Function_40_9736",        # 28, 40
        "Function_41_981E",        # 29, 41
        "Function_42_98D4",        # 2A, 42
        "Function_43_98EC",        # 2B, 43
        "Function_44_9980",        # 2C, 44
        "Function_45_A2DC",        # 2D, 45
        "Function_46_A31B",        # 2E, 46
        "Function_47_A35A",        # 2F, 47
        "Function_48_A3A7",        # 30, 48
        "Function_49_A3AE",        # 31, 49
        "Function_50_A49F",        # 32, 50
        "Function_51_A55B",        # 33, 51
        "Function_52_A60F",        # 34, 52
        "Function_53_A6C9",        # 35, 53
        "Function_54_A7A6",        # 36, 54
        "Function_55_A9DF",        # 37, 55
        "Function_56_AA7B",        # 38, 56
        "Function_57_AD92",        # 39, 57
        "Function_58_AE97",        # 3A, 58
        "Function_59_AF96",        # 3B, 59
        "Function_60_B09A",        # 3C, 60
        "Function_61_B181",        # 3D, 61
        "Function_62_B23A",        # 3E, 62
        "Function_63_B310",        # 3F, 63
        "Function_64_B549",        # 40, 64
        "Function_65_B5CE",        # 41, 65
        "Function_66_B84E",        # 42, 66
        "Function_67_B953",        # 43, 67
        "Function_68_BA52",        # 44, 68
        "Function_69_BB8C",        # 45, 69
        "Function_70_BC3E",        # 46, 70
        "Function_71_BE77",        # 47, 71
        "Function_72_C298",        # 48, 72
        "Function_73_CC1B",        # 49, 73
        "Function_74_CC37",        # 4A, 74
        "Function_75_CC85",        # 4B, 75
        "Function_76_CCC9",        # 4C, 76
        "Function_77_CD16",        # 4D, 77
        "Function_78_CD1A",        # 4E, 78
        "Function_79_CD1E",        # 4F, 79
        "Function_80_CD22",        # 50, 80
        "Function_81_CD26",        # 51, 81
        "Function_82_CD2A",        # 52, 82
        "Function_83_CD2E",        # 53, 83
        "Function_84_CD32",        # 54, 84
        "Function_85_CD36",        # 55, 85
        "Function_86_CD3A",        # 56, 86
        "Function_87_CD3E",        # 57, 87
        "Function_88_CD42",        # 58, 88
        "Function_89_CD46",        # 59, 89
    )


    def Function_0_85E(): pass

    label("Function_0_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_886")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8DA")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8AE")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    Jump("loc_8DA")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8DA")
    SetChrPos(0xD, 32000, 0, 21020, 0)
    SetChrPos(0xE, 31990, 0, 22540, 180)
    Jump("loc_8DA")

    label("loc_8DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x9, 48900, 0, 48800, 0)
    Jump("loc_A64")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_93F")
    SetChrPos(0x9, 68600, 0, 42100, 0)
    SetChrPos(0xA, 66000, 0, 40200, 225)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_975")
    SetChrPos(0x9, 48900, 0, 48800, 0)
    SetChrPos(0xA, 34900, 0, 38200, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_9AB")
    SetChrPos(0x9, 70160, 0, 16850, 0)
    SetChrPos(0xA, 72160, 0, 18850, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_9E8")
    SetChrPos(0x9, 70160, 0, 16850, 90)
    SetChrPos(0xA, 71160, 0, 17850, 225)
    SetChrPos(0x11, 72160, 0, 18850, 0)
    Jump("loc_A64")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x11, 45200, 0, 42700, 0)
    SetChrPos(0x9, 46900, 0, 74100, 0)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 49900, 0, 72100, 0)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_A64")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_END)), "loc_A64")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    OP_44(0x11, 0xFF)

    label("loc_A64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")

    label("loc_A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A95")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_B09")

    label("loc_A95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AB8")
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_B09")

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_ADD")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32150, 0, 28000, 45)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_B09")

    label("loc_ADD")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 45660, 0, 19400, 270)
    SetChrPos(0x12, 62400, 250, 22000, 270)

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1A")
    Jump("loc_B70")

    label("loc_B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B51")
    SetChrPos(0x14, 36320, 0, 57180, 135)
    ClearChrFlags(0x14, 0x40)
    SetChrChipByIndex(0x14, 19)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B70")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_B7E")
    OP_A3(0x3FA)
    Event(0, 71)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_B95")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 72)

    label("loc_B95")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BB1"),
        (119, "loc_BE9"),
        (110, "loc_C5B"),
        (122, "loc_CCA"),
        (2, "loc_CE0"),
        (SWITCH_DEFAULT, "loc_D0D"),
    )


    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD8")
    OP_28(0x9, 0x4, 0x10)
    Event(1, 35)
    Jump("loc_BE6")

    label("loc_BD8")

    ClearMapFlags(0x1)
    SetMapFlags(0x80)
    Event(1, 9)

    label("loc_BE6")

    Jump("loc_D0D")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")
    Jump("loc_D0D")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    SetChrPos(0x101, 48300, 0, 7432, 0)
    SetChrPos(0x102, 49500, 0, 6573, 0)
    OP_6D(49336, 0, 72554, 0)
    OP_6C(36000, 0)
    OP_6B(5000, 0)
    FadeToBright(500, 0)
    Event(0, 33)

    label("loc_C58")

    Jump("loc_D0D")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC7")
    ClearMapFlags(0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrPos(0x9, 57890, 0, 14350, 0)
    SetChrPos(0xA, 57890, 0, 14350, 0)
    OP_6D(49800, 0, 18520, 0)
    OP_6C(33000, 0)
    FadeToBright(500, 0)
    Event(0, 37)

    label("loc_CC7")

    Jump("loc_D0D")

    label("loc_CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDD")
    OP_A2(0x264)
    Event(0, 21)

    label("loc_CDD")

    Jump("loc_D0D")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_CEE")
    Event(0, 28)
    Jump("loc_D0A")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_D01")
    SetChrFlags(0x11, 0x80)
    Event(0, 26)
    Jump("loc_D0A")

    label("loc_D01")

    SetChrFlags(0x11, 0x80)
    Event(0, 27)

    label("loc_D0A")

    Jump("loc_D0D")

    label("loc_D0D")

    Return()

    # Function_0_85E end

    def Function_1_D0E(): pass

    label("Function_1_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D26")
    OP_B1("t0100_y")
    Jump("loc_D2F")

    label("loc_D26")

    OP_B1("t0100_n")

    label("loc_D2F")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x30001)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5A")
    OP_64(0x1, 0x1)
    Jump("loc_D6C")

    label("loc_D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")
    OP_64(0x1, 0x1)
    Jump("loc_D6C")

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D78")
    OP_64(0x2, 0x1)

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_D9E")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E62")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC9")
    OP_6F(0x25, 100)
    OP_6F(0x27, 100)
    OP_6F(0x29, 100)
    OP_6F(0x2B, 100)
    Jump("loc_E62")

    label("loc_DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF4")
    OP_6F(0x25, 50)
    OP_6F(0x27, 50)
    OP_6F(0x29, 50)
    OP_6F(0x2B, 50)
    Jump("loc_E62")

    label("loc_DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1F")
    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)
    Jump("loc_E62")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E46")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E62")

    label("loc_E46")

    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)

    label("loc_E62")

    Return()

    # Function_1_D0E end

    def Function_2_E63(): pass

    label("Function_2_E63")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E88")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_FCA")

    label("loc_E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_FCA")

    label("loc_EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_FCA")

    label("loc_EBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_FCA")

    label("loc_ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_FCA")

    label("loc_EEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F05")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_FCA")

    label("loc_F05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_FCA")

    label("loc_F1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F37")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_FCA")

    label("loc_F37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F50")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_FCA")

    label("loc_F50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F69")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_FCA")

    label("loc_F69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_FCA")

    label("loc_F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_FCA")

    label("loc_F9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_FCA")

    label("loc_FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_FCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_FCA")

    label("loc_FDF")

    Return()

    # Function_2_E63 end

    def Function_3_FE0(): pass

    label("Function_3_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_100D")

    label("loc_FE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_100A")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_FE7")

    label("loc_100A")

    Jump("loc_1118")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_103A")

    label("loc_1014")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1037")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_1014")

    label("loc_1037")

    Jump("loc_1118")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1067")

    label("loc_1041")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1064")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_1041")

    label("loc_1064")

    Jump("loc_1118")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1094")

    label("loc_106E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1091")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_106E")

    label("loc_1091")

    Jump("loc_1118")

    label("loc_1094")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1118")
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_1094")

    label("loc_1118")

    Return()

    # Function_3_FE0 end

    def Function_4_1119(): pass

    label("Function_4_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1146")

    label("loc_1120")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1143")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_1120")

    label("loc_1143")

    Jump("loc_1251")

    label("loc_1146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1173")

    label("loc_114D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1170")
    OP_8D(0xFE, 31500, 36600, 36600, 40300, 3000)
    Jump("loc_114D")

    label("loc_1170")

    Jump("loc_1251")

    label("loc_1173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_11A0")

    label("loc_117A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_119D")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_117A")

    label("loc_119D")

    Jump("loc_1251")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_11CD")

    label("loc_11A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11CA")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_11A7")

    label("loc_11CA")

    Jump("loc_1251")

    label("loc_11CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1251")
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_11CD")

    label("loc_1251")

    Return()

    # Function_4_1119 end

    def Function_5_1252(): pass

    label("Function_5_1252")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1275")
    OP_8D(0xFE, 25948, 43568, 37838, 41060, 3000)
    Jump("Function_5_1252")

    label("loc_1275")

    Return()

    # Function_5_1252 end

    def Function_6_1276(): pass

    label("Function_6_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_12A3")

    label("loc_127D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12A0")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_127D")

    label("loc_12A0")

    Jump("loc_12F3")

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_12D0")

    label("loc_12AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12CD")
    OP_8D(0xFE, 43800, 43900, 47136, 39800, 4000)
    Jump("loc_12AA")

    label("loc_12CD")

    Jump("loc_12F3")

    label("loc_12D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F3")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_12D0")

    label("loc_12F3")

    Return()

    # Function_6_1276 end

    def Function_7_12F4(): pass

    label("Function_7_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1322")

    label("loc_12FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_131F")
    OP_8D(0xFE, 31735, 16555, 28343, 23211, 2000)
    Jump("loc_12FC")

    label("loc_131F")

    Jump("loc_1337")

    label("loc_1322")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1337")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1322")

    label("loc_1337")

    Return()

    # Function_7_12F4 end

    def Function_8_1338(): pass

    label("Function_8_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135F")

    label("loc_1347")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1347")

    label("loc_135C")

    Jump("loc_1382")

    label("loc_135F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1382")
    OP_8D(0xFE, 63200, 17400, 61600, 22900, 2000)
    Jump("loc_135F")

    label("loc_1382")

    Return()

    # Function_8_1338 end

    def Function_9_1383(): pass

    label("Function_9_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B2")

    label("loc_139D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_139D")

    label("loc_13B2")

    Return()

    # Function_9_1383 end

    def Function_10_13B3(): pass

    label("Function_10_13B3")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15B5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157E")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_146E")

    def lambda_1452():

        label("loc_1452")

        OP_97(0xFE, 0xD6D8, 0xB824, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1452")

    QueueWorkItem2(0xFE, 1, lambda_1452)
    Jump("loc_148D")

    label("loc_146E")


    def lambda_1474():

        label("loc_1474")

        OP_97(0xFE, 0xD6D8, 0xB824, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1474")

    QueueWorkItem2(0xFE, 1, lambda_1474)

    label("loc_148D")

    SetChrChipByIndex(0xFE, 21)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_149C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14D4")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_14D4")

    label("loc_14CC")

    Sleep(15)
    Jump("loc_149C")

    label("loc_14D4")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 55000, 0, 47140, 74)

    label("loc_14F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_157B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1573")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 22)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    Jump("loc_157B")

    label("loc_1573")

    Sleep(500)
    Jump("loc_14F3")

    label("loc_157B")

    Jump("loc_15B2")

    label("loc_157E")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B2")

    def lambda_159A():
        OP_8D(0xFE, 51380, 38050, 58760, 43900, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_159A)

    label("loc_15B2")

    Jump("loc_13E7")

    label("loc_15B5")

    Return()

    # Function_10_13B3 end

    def Function_11_15B6(): pass

    label("Function_11_15B6")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05《Septian Calendar 1075》\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #1
        (
            "\x07\x05《Septian Calendar 1192》\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x05《Septian Calendar 1197》\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_11_15B6 end

    def Function_12_172B(): pass

    label("Function_12_172B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_18EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187F")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #3
        0xFE,
        (
            "Oh, it's Estelle.\x01",
            "You going somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#000FSomething like that.\x02\x03",

            "I'll be away from Rolent for a while.\x02\x03",

            "Don't cry yourself to sleep while\x01",
            "I'm gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Shaddup! Who's gonna cry themselves\x01",
            "to sleep over you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "...But, do you know when you'll be\x01",
            "coming back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#000FI have no idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EB")

    label("loc_187F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #9
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "...Hurry and come back, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#000FDid you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "N-Never mind.\x02",
    )

    CloseMessageWindow()

    label("loc_18EB")

    Jump("loc_1F69")

    label("loc_18EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1922")

    ChrTalk(    #13
        0xFE,
        (
            "What happened at Mayor Klaus'\x01",
            "place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D9")
    OP_A2(0x6)

    ChrTalk(    #14
        0xFE,
        (
            "Some news reporters came to do\x01",
            "a story on your dad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "My dad's a soldier in the Royal\x01",
            "Army, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "He's pretty plain and boring compared\x01",
            "to bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A13")

    label("loc_19D9")


    ChrTalk(    #17
        0xFE,
        (
            "Yeah, bracers are definitely cooler\x01",
            "than soldiers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A13")

    Jump("loc_1F69")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1ACE")

    ChrTalk(    #18
        0xFE,
        "I wish I could grow up now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I'd become a bracer and be\x01",
            "so successful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I must really suck if I got passed\x01",
            "up by the likes of Estelle, but\x01",
            "I guess that's life. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3F")
    OP_A2(0x6)

    ChrTalk(    #21
        0xFE,
        (
            "Mayor Klaus was weeding around\x01",
            "the clock tower earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Do mayors have to do those\x01",
            "kinds of jobs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#000FThat's his hobby. There are even rumors\x01",
            "that he really enjoys gardening, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#010FI wonder if that's why he's called\x01",
            "'Ol' Man Klaus'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#001FWell, aren't you glad that he's informal\x01",
            "and accessible for everyone like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1C3F")


    ChrTalk(    #26
        0xFE,
        (
            "Mayor Klaus was weeding around\x01",
            "the clock tower earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Do mayors have to do those\x01",
            "kinds of jobs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jump("loc_1F69")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1D12")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(    #28 op#5
        0x9,
        "I am Cassius Bright!\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(500)

    ChrTalk(    #29 op#5
        0x9,
        (
            "Turn and fight, you cowardly\x01",
            "monsters!\x05\x02",
        )
    )

    OP_4B(0x9, 0)
    Jump("loc_1F69")

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2F")
    OP_A2(0x6)

    ChrTalk(    #30
        0x9,
        (
            "H-Hmph! I just wanted to say I'm\x01",
            "grateful that you saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "I hate to admit it, but...you were\x01",
            "pretty cool, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "Not as cool as your dad,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "I've made up my mind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "I'm gonna make it my goal to\x01",
            "become a bracer, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E98")

    label("loc_1E2F")


    ChrTalk(    #36
        0x9,
        (
            "I can't get over how cool your\x01",
            "dad is, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "I'm sure any man would want\x01",
            "to be like Cassius.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E98")

    Jump("loc_1F69")

    label("loc_1E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1ED2")

    ChrTalk(    #38
        0x9,
        (
            "翡翠の塔にいるはず。\x01",
            "俺見たらバグだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3D")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(    #39 op#5
        0x9,
        "If you want to go with me...\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(800)

    ChrTalk(    #40 op#5
        0x9,
        "You're gonna have to catch me first!\x05\x02",
    )

    OP_4B(0x9, 0)
    Jump("loc_1F69")

    label("loc_1F3D")

    OP_4A(0x9, 0)

    ChrTalk(    #41 op#5
        0x9,
        "I'm the one who discovered it!\x05\x02",
    )

    OP_4B(0x9, 0)

    label("loc_1F69")

    TalkEnd(0x9)
    Return()

    # Function_12_172B end

    def Function_13_1F6D(): pass

    label("Function_13_1F6D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1FCB")

    ChrTalk(    #42
        0xFE,
        (
            "Mayor Klaus came rushing by\x01",
            "here in a hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2056")

    ChrTalk(    #44
        0xFE,
        (
            "The Liberl News, huh? That's the\x01",
            "magazine my dad always reads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The cover always has somebody\x01",
            "really famous or popular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_20C1")

    ChrTalk(    #46
        0xFE,
        (
            "We learned about the Bracer Guild\x01",
            "at Sunday School the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Bracers are so cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(    #48
        0xFE,
        (
            "The garden at the mayor's place\x01",
            "is so well kept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I heard that the mayor even\x01",
            "does it all himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_218C")
    OP_4A(0xA, 0)

    ChrTalk(    #50 op#5
        0xA,
        (
            "Luke, let up a little! Feels like all I\x01",
            "can do is run away...\x05\x02",
        )
    )

    OP_4B(0xA, 0)
    Jump("loc_23CA")

    label("loc_218C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    OP_A2(0x7)

    ChrTalk(    #51
        0xA,
        (
            "Thanks for saving us today,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "I wonder what would have happened\x01",
            "to us if you and Joshua hadn't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_22A7")


    ChrTalk(    #55
        0xA,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    Jump("loc_23CA")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2373")

    ChrTalk(    #57
        0xA,
        (
            "翡翠の塔にいるはずー。\x01",
            "見たら近藤までー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CA")

    label("loc_2373")

    OP_4A(0xA, 0)

    ChrTalk(    #58 op#5
        0xA,
        (
            "Take me with you! I'm the one\x01",
            "who told you about the place to\x01",
            "begin with.\x05\x02",
        )
    )

    OP_4B(0xA, 0)

    label("loc_23CA")

    TalkEnd(0xA)
    Return()

    # Function_13_1F6D end

    def Function_14_23CE(): pass

    label("Function_14_23CE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F9")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #59
        0xFE,
        (
            "Estelle, Joshua. Are you really\x01",
            "headed to Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#000FAh ha ha...I should have guessed\x01",
            "you'd know.\x02\x03",

            "You're always one of the first to\x01",
            "hear everything.\x02\x03",

            "There's a little something we need\x01",
            "to check on, so that's why we're\x01",
            "headed to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Not only is Cassius gone, but\x01",
            "now you two are leaving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Awww, I want to tag along!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #63
        0xFE,
        "Joshua, take me with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#014FI...uh...don't think that would be\x01",
            "a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "But, I'm concerned about other\x01",
            "incidents happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I get so worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2694")

    label("loc_25F9")


    ChrTalk(    #68
        0xFE,
        (
            "Okay, this time I'll wait here for you\x01",
            "like a good girl, so hurry back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "If all of you are gone, it's going to\x01",
            "be a big drain on my news sources!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2694")

    Jump("loc_433B")

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_27FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278F")
    OP_A2(0x8)

    ChrTalk(    #70
        0xB,
        "Ah! Estelle and Joshua! And...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0xB,
        "Wow! It's Schera, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        "#020FHi, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        (
            "All three bracers spoken of in town\x01",
            "together at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "Does this mean that something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F9")

    label("loc_278F")


    ChrTalk(    #75
        0xB,
        (
            "All three bracers spoken of in town\x01",
            "together at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xB,
        (
            "Does this mean that something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F9")

    Jump("loc_433B")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A02")
    OP_A2(0x8)

    ChrTalk(    #77
        0xB,
        (
            "Estelle, Joshua. I heard that you two've\x01",
            "had your fair share of accomplishments lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        (
            "Let's see... You drove the fiends\x01",
            "away from the Perzel Farm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "You rescued the miners at the\x01",
            "Malga Mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        (
            "And this last time you escorted\x01",
            "some reporters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#014FW-Wow, you certainly know a\x01",
            "lot for your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xB,
        "Yep, I sure do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "I wish those reporters would\x01",
            "hire me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xB,
        (
            "I think I'm perfect for the job\x01",
            "of a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#000F(That's probably true.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#010F(Ha ha...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_2A02")


    ChrTalk(    #87
        0xB,
        (
            "I wish those reporters would\x01",
            "hire me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "I think I'm perfect for the job\x01",
            "of a reporter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    Jump("loc_433B")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B70")
    OP_A2(0x8)

    ChrTalk(    #89
        0xB,
        (
            "I saw the mayor coming out\x01",
            "of the guild earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "Other than that, I've been seeing\x01",
            "Mr. Rinon's mother out in town a\x01",
            "lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        (
            "She's awfully suspicious if\x01",
            "you ask me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        (
            "But, I don't know which one I\x01",
            "should follow for more details...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA0")

    label("loc_2B70")


    ChrTalk(    #93
        0xB,
        (
            "Oh, there's a juicy story calling\x01",
            "my name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA0")

    Jump("loc_433B")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2C51")

    ChrTalk(    #94
        0xB,
        (
            "According to my sources, it looks\x01",
            "like there's been an incident at\x01",
            "the Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "I wonder if I should go barging into\x01",
            "the guild and report it to Aina?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433B")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB4")
    OP_A2(0x8)

    ChrTalk(    #96
        0xB,
        (
            "Hey, where did Cassius take\x01",
            "off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#000FUm, he's gone away on business\x01",
            "and won't be back for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xB,
        "Is that so... *sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xB,
        (
            "Cassius was the one who I was\x01",
            "most focused on. That's too bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#002FClaire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        (
            "I think that even if Cassius dressed\x01",
            "in normal attire, he'd still shine as\x01",
            "an adult male.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "By changing his style he'd express\x01",
            "himself as a characteristic beau\x01",
            "aside from the typical joe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "There's no doubt he'd be popular\x01",
            "on a whole new level, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#506FUm, Claire?\x01",
            "How old are you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#019FHa ha, she's a precocious one,\x01",
            "isn't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF2")

    label("loc_2EB4")


    ChrTalk(    #106
        0xFE,
        (
            "Awww, with Cassius gone, there's\x01",
            "not much to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF2")

    Jump("loc_433B")

    label("loc_2EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_378A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_302E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE3")
    OP_A2(0x8)

    ChrTalk(    #107
        0xB,
        (
            "I've heard that you two have had some\x01",
            "major success recently, Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "I knew I was right to keep my\x01",
            "eye on you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xB,
        "Tee hee, keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xB,
        "I'm a fan of the both of you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_302B")

    label("loc_2FE3")


    ChrTalk(    #111
        0xB,
        "Tee hee, keep up the good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xB,
        "I'm a fan of the both of you.\x02",
    )

    CloseMessageWindow()

    label("loc_302B")

    Jump("loc_3787")

    label("loc_302E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_3285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3241")
    OP_A2(0x8)

    ChrTalk(    #113
        0xB,
        (
            "Hey, Estelle and Joshua. Is it true\x01",
            "that you really became bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#000FYou're always one of the first to\x01",
            "hear everything, aren't you, Claire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "This is just what I expected!\x01",
            "I saw the potential in you both\x01",
            "way back. Yup, yup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        (
            "You're going to get out there and\x01",
            "earn a lot of success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xB,
        "I like Scherazard's adult charm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "But I'm partial to both you\x01",
            "and Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x101,
        "#506FH-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#019FI-I'll take that as a compliment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3282")

    label("loc_3241")


    ChrTalk(    #121
        0xB,
        "The drama's finally going to begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        "I'm so excited! ★\x02",
    )

    CloseMessageWindow()

    label("loc_3282")

    Jump("loc_3787")

    label("loc_3285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A7")
    OP_A2(0x8)

    ChrTalk(    #123
        0xB,
        "Ah...Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "Did the two of you really become\x01",
            "bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        "#010FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "That's because working in the media is\x01",
            "my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        (
            "I'm going to join the Liberl News Service and work\x01",
            "hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        "Don't take my information lightly, either.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #129
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "My gut feeling says that the two of you are going\x01",
            "to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        (
            "Isn't it romantic that you two lovers are bracers who\x01",
            "stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#000FL-Lovers?\x02\x03",

            "Joshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        (
            "You really don't understand anything,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "Joshua's adopted and things could go either way\x01",
            "in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        (
            "Plus, leaving it at that would surely please the\x01",
            "readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #138
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#000FI don't have a clue what she's\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "Anyway, I'm looking forward to the both of\x01",
            "you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3787")

    label("loc_36A7")


    ChrTalk(    #141
        0xB,
        (
            "The two valiant bracers who had each\x01",
            "others' backs and attempted  to escape from\x01",
            "the crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xB,
        (
            "Ahh...love could definitely grow between them\x01",
            "from that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_3787")

    Jump("loc_433B")

    label("loc_378A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3974")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(    #144
        0xB,
        (
            "Hey, Estelle and Joshua. Is it true\x01",
            "that you really became bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#000FYou're always one of the first to\x01",
            "hear everything, aren't you, Claire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "This is just what I expected!\x01",
            "I saw the potential in you both\x01",
            "way back. Yup, yup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "You're going to get out there and\x01",
            "earn a lot of success, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        "I like Scherazard's adult charm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xB,
        (
            "But I'm partial to both you\x01",
            "and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#506FH-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#019FI-I'll take that as a compliment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B5")

    label("loc_3974")


    ChrTalk(    #152
        0xB,
        "The drama's finally going to begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        "I'm so excited! ★\x02",
    )

    CloseMessageWindow()

    label("loc_39B5")

    Jump("loc_3E44")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA9")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(    #154
        0xB,
        "Ah...Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xB,
        (
            "Did the two of you really\x01",
            "become bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        "#010FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        (
            "That's because working in the\x01",
            "media is my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "I'm going to join the Liberl News\x01",
            "Service and work hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xB,
        (
            "Don't take my information lightly\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        (
            "My gut feeling says that the two of\x01",
            "you are going to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xB,
        (
            "Isn't it romantic that you two lovers\x01",
            "are bracers who stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#000FL-Lovers?\x02\x03",

            "#000FJoshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xB,
        (
            "You really don't understand\x01",
            "anything, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xB,
        (
            "Joshua's adopted and things could\x01",
            "go either way in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xB,
        (
            "Plus, leaving it at that would surely\x01",
            "please the readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xB,
        (
            "Anyway, I'm looking forward to\x01",
            "the both of you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E44")

    label("loc_3DA9")


    ChrTalk(    #171
        0xB,
        (
            "The two valiant bracers who had\x01",
            "each others' backs and attempted\x01",
            "to escape from the crisis...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_3E44")

    Jump("loc_433B")

    label("loc_3E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425C")
    OP_A2(0x8)
    OP_A2(0x214)

    ChrTalk(    #173
        0x101,
        "#001FGood morning, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        "Good morning, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "Did the two of you really\x01",
            "become bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        "#014FWhat? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xB,
        (
            "That's because working in the\x01",
            "media is my future goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xB,
        (
            "I'm going to join the Liberl News\x01",
            "Service and work hard as a reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        (
            "Don't take my information lightly\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #180
        0x101,
        "#506FO-Oh, sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xB,
        (
            "My gut feeling says that the two of\x01",
            "you are going to be in the tabloids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#506FAh ha ha ha, well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xB,
        (
            "Isn't it romantic that you two lovers\x01",
            "are bracers who stand for justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xB,
        (
            "I have this feeling that a juicy drama is\x01",
            "about to unfold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#008FL-Lovers?\x02\x03",

            "Joshua and I aren't lovers,\x01",
            "we're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xB,
        (
            "You really don't understand\x01",
            "anything, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xB,
        (
            "Joshua's adopted and things could\x01",
            "go either way in the future, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xB,
        (
            "Plus, leaving it at that would surely\x01",
            "please the readers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #189
        0x102,
        "#019FR-Readers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xB,
        (
            "Anyway, I'm looking forward to\x01",
            "the both of you in more ways than one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433B")

    label("loc_425C")


    ChrTalk(    #191
        0xB,
        (
            "The two valiant bracers who had\x01",
            "each others' backs and attempted\x01",
            "to escape from the crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xB,
        (
            "Ahh...love could definitely grow\x01",
            "between them from that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0xB,
        "This is so riveting...\x02",
    )

    CloseMessageWindow()

    label("loc_433B")

    TalkEnd(0xB)
    Return()

    # Function_14_23CE end

    def Function_15_433F(): pass

    label("Function_15_433F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4446")
    OP_A2(0x9)

    ChrTalk(    #194
        0xFE,
        (
            "Lately, my father-in-law has\x01",
            "been giving me job advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Coming from an industry veteran\x01",
            "there's a lot I can learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "It seems I've been pretty conceited\x01",
            "over my work in the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I feel pretty embarrassed about\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B8")

    label("loc_4446")


    ChrTalk(    #198
        0xFE,
        (
            "It seems I've been pretty conceited\x01",
            "over my work in the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "I feel pretty embarrassed about\x01",
            "it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B8")

    Jump("loc_4B9D")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_457E")
    OP_A2(0x9)

    ChrTalk(    #200
        0xFE,
        (
            "Although the work in the woods is\x01",
            "going smooth and lumber sales are\x01",
            "increasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "I can't figure it out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "My father-in-law just won't\x01",
            "acknowledge my efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460E")

    label("loc_457E")


    ChrTalk(    #203
        0xFE,
        (
            "Although the work in the woods is\x01",
            "going smooth and lumber sales are\x01",
            "increasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "My father-in-law just won't\x01",
            "acknowledge my efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460E")

    Jump("loc_4B9D")

    label("loc_4611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_46DB")

    ChrTalk(    #205
        0xFE,
        (
            "Lumber sales have been good and\x01",
            "I'm starting to feel confident I can\x01",
            "support my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "The work is going smooth and I'm\x01",
            "even on par with the output my\x01",
            "father-in-law was once doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_46DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_4780")

    ChrTalk(    #207
        0xFE,
        (
            "I got an additional lumber order\x01",
            "from the merchants in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "I'm going to work hard, so I can\x01",
            "sell a ton of lumber to the other\x01",
            "regions as well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_48EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4859")
    OP_A2(0x9)

    ChrTalk(    #209
        0xFE,
        (
            "In order to be with my wife,\x01",
            "I took over the timber business\x01",
            "from my father-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "Recently, I've started getting\x01",
            "used to this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "And I've even begun to feel\x01",
            "satisfied doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E8")

    label("loc_4859")


    ChrTalk(    #212
        0xFE,
        (
            "In order to be with my wife,\x01",
            "I took over the timber business\x01",
            "from my father-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Recently, I've started getting\x01",
            "used to this job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E8")

    Jump("loc_4B9D")

    label("loc_48EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4918")

    ChrTalk(    #214
        0xC,
        (
            "これを見たあなた。\x01",
            "バグです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E9")
    OP_A2(0x9)

    ChrTalk(    #215
        0xC,
        (
            "It seems like it's going to take a\x01",
            "bit longer for me to get the lumber\x01",
            "together for this order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xC,
        (
            "I must work hard to get my father-\x01",
            "in-law to acknowledge me...for my\x01",
            "wife's sake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A40")

    label("loc_49E9")


    ChrTalk(    #217
        0xC,
        (
            "I must work hard to get my father-\x01",
            "in-law to acknowledge me...for my\x01",
            "wife's sake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A40")

    Jump("loc_4B9D")

    label("loc_4A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B22")
    OP_A2(0x9)

    ChrTalk(    #218
        0xC,
        (
            "I'm just on my way over to the\x01",
            "forest of Mistwald to the south\x01",
            "of here for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        (
            "There was a merchant from Bose\x01",
            "who came here to buy lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xC,
        (
            "I need to get enough ready for\x01",
            "the order I received.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9D")

    label("loc_4B22")


    ChrTalk(    #221
        0xC,
        (
            "There was a merchant from Bose\x01",
            "who came here to buy lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xC,
        (
            "I need to get enough ready for\x01",
            "the order I received.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9D")

    TalkEnd(0xC)
    Return()

    # Function_15_433F end

    def Function_16_4BA1(): pass

    label("Function_16_4BA1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_4BFC")

    ChrTalk(    #223
        0x11,
        "Mayor Klaus just came by here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x11,
        (
            "He greeted me with such a\x01",
            "big voice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8B")

    label("loc_4BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4C54")

    ChrTalk(    #225
        0x11,
        (
            "Luke's been like that since\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x11,
        "Boys are so simpleminded.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D8B")

    label("loc_4C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4C87")

    ChrTalk(    #227
        0x11,
        (
            "I wonder where Luke and\x01",
            "Pat went...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8B")

    label("loc_4C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D62")
    OP_A2(0xA)

    ChrTalk(    #228
        0x11,
        "Oh, Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        "#010FGood morning, Yuni.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#000FAren't Luke and Pat with\x01",
            "you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x11,
        (
            "They were here just a minute\x01",
            "ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x11,
        (
            "The two of them suddenly took\x01",
            "off and went somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8B")

    label("loc_4D62")


    ChrTalk(    #233
        0x11,
        "I wonder where Luke and Pat went...\x02",
    )

    CloseMessageWindow()

    label("loc_4D8B")

    TalkEnd(0x11)
    Return()

    # Function_16_4BA1 end

    def Function_17_4D8F(): pass

    label("Function_17_4D8F")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAC")
    OP_A2(0xD)

    ChrTalk(    #234
        0xE,
        "Yesssssss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xE,
        "Listen to this, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xE,
        "I got her to go out with me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xE,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#000F(A single day? Uh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        (
            "#010F(I guess that could be called\x01",
            "a victory of perseverance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F00")

    label("loc_4EAC")


    ChrTalk(    #240
        0xE,
        (
            "Oh, Aidios... It was all worth the\x01",
            "single day of trouble I went through\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F00")

    Jump("loc_5091")

    label("loc_4F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5038")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD1")
    OP_A2(0xD)

    ChrTalk(    #241
        0xE,
        (
            "I've confessed to her several times\x01",
            "since this morning, but I can't get\x01",
            "her to accept my love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xE,
        (
            "It doesn't seem like she hates me\x01",
            "or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xE,
        "What am I doing wrong...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4FD1")


    ChrTalk(    #244
        0xE,
        (
            "I've confessed to her several times\x01",
            "since this morning, but I can't get\x01",
            "her to accept my love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5035")

    Jump("loc_5091")

    label("loc_5038")


    ChrTalk(    #245
        0xE,
        "Ahhh...that girl is so cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xE,
        (
            "I've got to be courageous and\x01",
            "try to talk to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5091")

    TalkEnd(0xE)
    Return()

    # Function_17_4D8F end

    def Function_18_5095(): pass

    label("Function_18_5095")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514E")
    OP_A2(0xD)

    ChrTalk(    #247
        0xFE,
        "Yesssssss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "I invited her to the queen's birthday\x01",
            "celebration and she said, 'yes.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "I'm going to have to get a part-time\x01",
            "job and save up some cash.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_518F")

    label("loc_514E")


    ChrTalk(    #250
        0xFE,
        (
            "I'm going to have to work hard\x01",
            "now and save up some cash...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518F")

    Jump("loc_5431")

    label("loc_5192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_530A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528E")
    OP_A2(0xD)

    ChrTalk(    #251
        0x10,
        (
            "It's a little ways off, but the\x01",
            "queen is having her birthday\x01",
            "celebration in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10,
        (
            "It's held every year leading up\x01",
            "to the Martial Arts Competition.\x01",
            "I hear it's a lively event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x10,
        "I invited her to the festival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5307")

    label("loc_528E")


    ChrTalk(    #254
        0x10,
        (
            "I invited her to the festival\x01",
            "in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x10,
        (
            "La la la...\x01",
            "There's something I want\x01",
            "to tell that girl there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5307")

    Jump("loc_5431")

    label("loc_530A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_537E")

    ChrTalk(    #256
        0x10,
        (
            "I meet and talk with her over\x01",
            "tea every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10,
        (
            "But the dating spots in Rolent\x01",
            "are pretty limited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5431")

    label("loc_537E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_53F4")

    ChrTalk(    #258
        0x10,
        "Oh, I'm so happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x10,
        (
            "Being able to spend each day with\x01",
            "someone I like...why, it's better\x01",
            "than bacon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5431")

    label("loc_53F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_5431")

    ChrTalk(    #260
        0x10,
        (
            "La la la...\x01",
            "Today is going to be our first date.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5431")

    TalkEnd(0x10)
    Return()

    # Function_18_5095 end

    def Function_19_5435(): pass

    label("Function_19_5435")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5606")
    OP_A2(0xB)

    ChrTalk(    #261
        0xD,
        (
            "It was when the stars had just\x01",
            "emerged from the veil of night\x01",
            "that he asked me here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xD,
        (
            "Sweetly, he whispered in my ear...\x01",
            "'I want you to be mine...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xD,
        "How romantic! ★\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xD,
        (
            "It's just the situation I've always\x01",
            "wanted to be in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#000F(Well, I guess it's not a bad place\x01",
            "and all, but...)\x02\x03",

            "#000F(The two of them came up\x01",
            "here just for that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        (
            "#010F(Haha. I guess this type of thing\x01",
            "can only be understood by those\x01",
            "involved.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5630")

    label("loc_5606")


    ChrTalk(    #267
        0xD,
        "Teehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xD,
        "I'm on cloud nine! ★\x02",
    )

    CloseMessageWindow()

    label("loc_5630")

    Jump("loc_5982")

    label("loc_5633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584C")
    OP_A2(0xB)

    ChrTalk(    #269
        0xD,
        "I'm so distressed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xD,
        (
            "He's my type, and I'd like to\x01",
            "accept his proposal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xD,
        (
            "...but this place is NOT my\x01",
            "ideal situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        (
            "#505FUmm... Is the place or whatever\x01",
            "really that important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xD,
        "Of course it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xD,
        (
            "This could be the memory of\x01",
            "a lifetime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xD,
        (
            "It may be the place that comes to\x01",
            "my mind when I'm an old grandma\x01",
            "and lying on my deathbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xD,
        (
            "I just can't accept an alleyway like\x01",
            "this as being THAT place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x102,
        (
            "#010FHaha. I guess this type of thing\x01",
            "can only be understood by those\x01",
            "involved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58FD")

    label("loc_584C")


    ChrTalk(    #278
        0xD,
        (
            "He has passionately confessed\x01",
            "his love to me several times...\x01",
            "but the situation isn't right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xD,
        (
            "It would be great if he'd just say it\x01",
            "to me in a bit more romantic place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58FD")

    Jump("loc_5982")

    label("loc_5900")


    ChrTalk(    #280
        0xD,
        (
            "The weather is so wonderful and\x01",
            "revitalizing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xD,
        (
            "I have this strange feeling that\x01",
            "something good is going to\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5982")

    TalkEnd(0xD)
    Return()

    # Function_19_5435 end

    def Function_20_5986(): pass

    label("Function_20_5986")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A89")
    OP_A2(0xB)

    ChrTalk(    #282
        0xFE,
        (
            "I waffled back and forth for a bit...but in the\x01",
            "end, I decided to go with him to the queen's\x01",
            "birthday celebration. As a couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "My mother is already going with\x01",
            "her friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "I'm sorry, Mother...but I want to\x01",
            "go with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C81")

    label("loc_5A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C5A")
    OP_A2(0xC)

    ChrTalk(    #285
        0xFE,
        (
            "The Royal City is like a huge\x01",
            "metropolis, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "The coruscating lamps of the sleepless\x01",
            "city...the elegant Grancel Castle resting\x01",
            "silently on the lakefront...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "The endless coming and going of people...the\x01",
            "energy and excitement from the stops lining the\x01",
            "streets...the festival parade and fireworks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "I get so excited just thinking\x01",
            "about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "And to think, I'll actually be going...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "I'm so excited I can hardly\x01",
            "even say it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C81")

    label("loc_5C5A")


    ChrTalk(    #291
        0xFE,
        "My heart is beating so quickly...\x02",
    )

    CloseMessageWindow()

    label("loc_5C81")

    Jump("loc_6145")

    label("loc_5C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5C")
    OP_A2(0xC)

    ChrTalk(    #292
        0xF,
        (
            "He invited me to go see the festival\x01",
            "with him in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xF,
        (
            "I'm so distressed! How am I going\x01",
            "to break the news to my mother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xF,
        (
            "What if he proposes to me\x01",
            "while we we're there?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DDB")

    label("loc_5D5C")

    OP_A2(0xC)

    ChrTalk(    #295
        0xF,
        (
            "He invited me to go see the festival\x01",
            "with him in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xF,
        (
            "What if he proposes to me\x01",
            "while we we're there?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDB")

    Jump("loc_6145")

    label("loc_5DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_5F95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F13")
    OP_A2(0xB)

    ChrTalk(    #297
        0xF,
        (
            "I'm really happy that I can meet\x01",
            "him every day like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xF,
        (
            "...but the places we go for dates\x01",
            "have really fallen into a rut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#502FHow typical. Boys really need to step up\x01",
            "their game! They have no imagination.\x01",
            "They're lazy, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x102,
        "#018F(Estelle, I can hear you...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F92")

    label("loc_5F13")


    ChrTalk(    #301
        0xF,
        (
            "I'm really happy that I can meet\x01",
            "him every day like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xF,
        (
            "...but the places we meet have\x01",
            "really gotten repetitive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F92")

    Jump("loc_6145")

    label("loc_5F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_5FFA")

    ChrTalk(    #303
        0xF,
        (
            "My boyfriend is really considerate.\x01",
            "I hope that I can be his number\x01",
            "one for all time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6145")

    label("loc_5FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_6145")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60DA")
    OP_A2(0xB)

    ChrTalk(    #304
        0xF,
        (
            "Heehee...\x01",
            "We just barely started going out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xF,
        (
            "Everything looks so bright and\x01",
            "promising to me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xF,
        (
            "I wonder if the world was always\x01",
            "this beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        "#007F(Our little world together...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6145")

    label("loc_60DA")


    ChrTalk(    #308
        0xF,
        (
            "Heehee...\x01",
            "Everything feels so fresh and bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xF,
        (
            "I wonder if the world was always\x01",
            "this beautiful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6145")

    TalkEnd(0xF)
    Return()

    # Function_20_5986 end

    def Function_21_6149(): pass

    label("Function_21_6149")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x0, 49730, 0, 79070, 180)
    SetChrPos(0x1, 50770, 0, 79870, 180)
    SetChrPos(0x2, 49620, 0, 80520, 180)
    SetChrPos(0x19, 50932, 0, 42709, 270)
    SetChrPos(0x18, 64013, 0, 42894, 270)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #310
        0x19,
        "Girl's Voice",
        (
            "Wait up! You're running like\x01",
            "a crazed lunatic...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #311
        0x18,
        "Man's Voice",
        (
            "Who can just walk...\x01",
            "at a time like this?!\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    TurnDirection(0x19, 0x18, 0)
    OP_6D(51350, 0, 43040, 3000)

    def lambda_626E():

        label("loc_626E")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_626E")

    QueueWorkItem2(0x19, 1, lambda_626E)
    OP_8E(0x18, 0xE25B, 0x0, 0xA926, 0x1388, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xDC36, 0x0, 0xA85E, 0xBB8, 0x0)
    OP_8F(0x18, 0xD89B, 0x0, 0xA98A, 0xBB8, 0x0)
    OP_8F(0x18, 0xD398, 0x0, 0xA7FA, 0xBB8, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xCE24, 0x0, 0xA926, 0xBB8, 0x0)
    OP_8F(0x18, 0xC7B3, 0x0, 0xAAA0, 0x7D0, 0x0)
    OP_44(0x19, 0xFF)

    ChrTalk(    #312
        0x18,
        (
            "#145F#4P*wheeze* *wheeze*\x02\x03",

            "#145FMaybe I should think...about\x01",
            "cutting back...on those blasted\x01",
            "cigarettes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#000FWhat are the two of you up to?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrPos(0x101, 50434, 0, 54609, 270)
    SetChrPos(0x102, 48721, 0, 55602, 270)
    SetChrPos(0x103, 51196, 0, 55910, 270)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0x102, 0x1, 0x0, 0x17)
    OP_43(0x103, 0x1, 0x0, 0x18)
    OP_6D(51050, 0, 45160, 1000)
    TurnDirection(0x18, 0x101, 400)
    TurnDirection(0x19, 0x101, 400)
    Sleep(2000)

    ChrTalk(    #314
        0x18,
        (
            "#140F#4PYou kids again, huh?\x02\x03",

            "#140FActually, we've got to get\x01",
            "to Bose ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x102,
        (
            "#010FBut the airliner's not even\x01",
            "here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x18,
        (
            "#141F#4PI know. That's why we're heading\x01",
            "there on foot.\x02\x03",

            "#141FIt'll take some time, but it's\x01",
            "not a distance that we can't\x01",
            "cover by ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        (
            "#501FWell, don't wear yourselves out\x01",
            "too badly. By the way, are you\x01",
            "after a scoop or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x18,
        (
            "#147F#4PYeah, and the mother of all\x01",
            "scoops, too!\x02\x03",

            "#144FNo time to talk!\x01",
            "We've got to make it there today!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x18, 0x1, 0x0, 0x19)
    TurnDirection(0x19, 0x18, 0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x18, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)

    ChrTalk(    #319
        0x19,
        (
            "#154F#2PI wonder if Nial's going\x01",
            "to be all right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x19, 400)
    TurnDirection(0x103, 0x19, 400)

    ChrTalk(    #320
        0x19,
        "#151FSee you later, Estelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x19)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x19, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x19, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)

    ChrTalk(    #321
        0x103,
        (
            "#020FWell, aren't they a lively pair.\x01",
            "Friends of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x101,
        (
            "#000FThose were the reporters from\x01",
            "one of the jobs Dad asked us to\x01",
            "take over.\x02\x03",

            "#000FI wonder what's going on...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_21_6149 end

    def Function_22_67BA(): pass

    label("Function_22_67BA")

    OP_92(0x101, 0x19, 0x7D0, 0xBB8, 0x0)
    Return()

    # Function_22_67BA end

    def Function_23_67C9(): pass

    label("Function_23_67C9")

    OP_92(0x102, 0x19, 0xBB8, 0xBB8, 0x0)
    Return()

    # Function_23_67C9 end

    def Function_24_67D8(): pass

    label("Function_24_67D8")

    OP_92(0x103, 0x19, 0xDAC, 0xBB8, 0x0)
    Return()

    # Function_24_67D8 end

    def Function_25_67E7(): pass

    label("Function_25_67E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6810")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    OP_48()
    Jump("Function_25_67E7")

    label("loc_6810")

    Return()

    # Function_25_67E7 end

    def Function_26_6811(): pass

    label("Function_26_6811")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x10)
    OP_28(0xA, 0x1, 0x4)

    ChrTalk(    #323
        0x1A,
        (
            "#020FGood work, you two.\x02\x03",

            "#020FAs a rule of training, I'm going\x01",
            "to need to confirm the items\x01",
            "in your possession.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #324
        "\x07\x00Handed over \x07\x02Small Box\x07\x00 x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x373, 2)

    ChrTalk(    #325
        0x1A,
        (
            "#020FYep...\x01",
            "They're the real deal, all right.\x02\x03",

            "I don't see any evidence of\x01",
            "tampering, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x101,
        "#007F(That was a close one...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#015F(I figured she would try and\x01",
            "set us up like that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x1A,
        (
            "#021FCongratulations to the both of you.\x01",
            "You have successfully passed your\x01",
            "qualification test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x101,
        (
            "#502FYou didn't really think something\x01",
            "that simple would be a problem\x01",
            "for us, did you?\x02\x03",

            "#000FSo...uh, Schera.\x01",
            "What's in those boxes you\x01",
            "had us get?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x1A,
        (
            "#020FThat's for me to know and you\x01",
            "to find out...after your training\x01",
            "is finished.\x02\x03",

            "#020FThat's enough chit-chat for now,\x01",
            "so let's get back to work.\x02\x03",

            "#020FYou two still have some things\x01",
            "left to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x101,
        (
            "#004FSeriously?\x02\x03",

            "#004FBut didn't you just say that we\x01",
            "passed the test?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x1A,
        (
            "#020FYou still have to learn about how\x01",
            "to report the results of your work.\x02\x03",

            "#020FI'm aware that you're both tired,\x01",
            "but this is no time to shirk your\x01",
            "duties. Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        (
            "#505FWhen is this day going to be over?\x02\x03",

            "#505FOh well. No sense in giving up\x01",
            "when the finish line is in sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x102,
        (
            "#010FAgreed. It seems like we're within\x01",
            "reaching distance of our goal.\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_26_6811 end

    def Function_27_6DB0(): pass

    label("Function_27_6DB0")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x4)
    OP_28(0xA, 0x4, 0x8)
    OP_28(0xA, 0x1, 0x1)

    ChrTalk(    #335
        0x1A,
        (
            "#020FAll your training has finally come\x01",
            "down to this.\x02\x03",

            "#020FYour qualification test will\x01",
            "begin here.\x02\x03",

            "#020FI expect to see you both use what\x01",
            "you've learned up to this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 315, 400)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #338
        0x102,
        "#010FWhat's wrong, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        "#505FUm...Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x1A,
        "#020FWhat now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#505F...I was kind of wondering but...\x01",
            "is there not going to be a paper\x01",
            "test or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x1A,
        (
            "#023F...\x01",
            "Did Cassius drop you on your\x01",
            "head as a child or something?\x02\x03",

            "You just read what it said on\x01",
            "the bulletin board not that\x01",
            "long ago, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        "#505FYeah, and?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x1A,
        (
            "#020FAnd I even made you jot down what\x01",
            "you read in your Bracer Notebooks...\x01",
            "unless you forgot that, too.\x02\x03",

            "#020FI'm pretty sure the job listing mentioned\x01",
            "searching for and retrieving an item from\x01",
            "the sewers... Ringin' any bells yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        (
            "#004F...\x02\x03",

            "#007FWhat a relief!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x101, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #346
        0x101,
        (
            "#001FOh, Divine Aidios...\x02\x03",

            "I give thanks to thee for thy\x01",
            "infinite grace in bestowing upon\x01",
            "us such wonderful gifts as sewers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x102,
        (
            "#018FSo what you're really saying,\x01",
            "is that you thought it was a\x01",
            "paper test?\x02\x03",

            "No wonder you were acting all\x01",
            "crazy back at the orbal factory...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #348
        0x101,
        (
            "#502FAhhh, I can already feel the nostalgia. All\x01",
            "those horrible days stuck in a classroom are\x01",
            "starting to feel like grand memories indeed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x102,
        (
            "#017FI'm really starting to wonder if we'll\x01",
            "even be able to graduate at all...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #350
        0x101,
        (
            "#509FWhat's wrong with you? Why do you have to\x01",
            "go and say something like that when I'm\x01",
            "trying to reminisce about positive things?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_744A():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_744A)

    def lambda_7458():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7458)

    ChrTalk(    #351
        0x1A,
        (
            "#022FAll right, that's enough jabbering,\x01",
            "you two.\x02\x03",

            "#022FThis is supposed to be a test,\x01",
            "so how about the both of you try\x01",
            "to at least look a little anxious?\x02\x03",

            "#022FJust so you know though, if you do happen to flunk\x01",
            "the test, you don't even want to imagine the kind\x01",
            "of homework I have in store for the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#001FHeh, heh.\x01",
            "We'll be fine!\x02\x03",

            "#001FJust tell us what you want us\x01",
            "to do and let us loose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x1A,
        (
            "#026FWell, if you're so confident then how about\x01",
            "proving that you're not just blowing hot air\x01",
            "with the results of your test?\x02\x03",

            "#020FAnyway, as you both saw on the bulletin\x01",
            "board, this test will be a search\x01",
            "conducted in Rolent's sewers.\x02\x03",

            "#020FYour objective is to retrieve the\x01",
            "contents of a chest which has been\x01",
            "placed somewhere within that area.\x02\x03",

            "#020FThe layout of the sewers is extremely\x01",
            "simple, so you don't need to worry\x01",
            "about getting lost, either.\x02\x03",

            "#020FHowever... There are real, living, breathing\x01",
            "monsters down there, so if you get careless\x01",
            "and let down your guard, you WILL be sorry.\x02\x03",

            "#020FAlso, let me give you this\x01",
            "before I forget.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #354
        "\x07\x00Received \x07\x02Tear Balm\x07\x00 x3.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #355
        "\x07\x00Received \x07\x02Monster Guide\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x1F5, 3)
    OP_3E(0x20F, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #356
        0x101,
        "#505FWhat's this book for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x1A,
        (
            "#020FIt's called a Monster Guide, and it's\x01",
            "used to record information about\x01",
            "monsters and other opponents you meet.\x02\x03",

            "#020FWhenever you figure out an enemy's\x01",
            "attributes, you should make an\x01",
            "immediate note of it in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x102,
        (
            "#010FSounds pretty straightforward\x01",
            "to me.\x02\x03",

            "'He who controls the flow of\x01",
            "information, controls the tide\x01",
            "of battle,' right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x1A,
        (
            "#021FThat's exactly what I'm saying.\x01",
            "You've really got a good head\x01",
            "on your shoulders, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x101,
        (
            "#501FThat's some pretty useful advice.\x02\x03",

            "#001FThanks for the tip, Schera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x102,
        "#010FWe'll put it to good use.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #362
        0x101,
        (
            "#006FAll-righty then! Let's get pumped\x01",
            "and knock out this test!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #363
        0x102,
        (
            "#010FLet's.\x02\x03",

            "#010FDon't forget, though, this IS\x01",
            "an exam. We should make sure\x01",
            "we treat it as such.\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_27_6DB0 end

    def Function_28_7C1D(): pass

    label("Function_28_7C1D")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x17, 0xFF)
    SetChrPos(0x102, 29410, 0, 68310, 0)
    SetChrPos(0x101, 30510, 0, 69400, 0)
    SetChrPos(0x19, 31602, 0, 67448, 0)
    SetChrPos(0x18, 32375, 0, 68461, 0)
    SetChrPos(0x17, 33719, 0, 67665, 0)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_6D(31270, 0, 68330, 0)
    OP_6B(3000, 0)
    OP_6C(270000, 0)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x17, 0x40)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x102, 0x17, 0)
    TurnDirection(0x19, 0x17, 0)
    TurnDirection(0x18, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_A2(0x259)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x1, 0x100)
    OP_28(0x19, 0x1, 0x200)
    OP_28(0x5, 0x4, 0x40)
    OP_28(0x9, 0x4, 0x40)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x17), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D0C")

    label("loc_7D0C")

    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #364
        0x17,
        (
            "#130FThank you so much for escorting\x01",
            "me back here.\x02\x03",

            "#130FThis is the first time I've ever been\x01",
            "able to make it back from some ruins\x01",
            "without being chased or bitten or...\x02\x03",

            "#130FI don't know how to begin to\x01",
            "express my appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x102,
        (
            "#010FYou don't need to thank us.\x01",
            "It's our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#000FI think you'd be better off hiring some\x01",
            "bracers to begin with next time you\x01",
            "go off to investigate some ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x17,
        (
            "#130FMy head says, yes...\x01",
            "but my wallet says, no.\x01",
            "I'll try and save up a bit, though.\x02\x03",

            "#130FWell, have a wonderful day and\x01",
            "I hope we can all meet again.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x17, 0x1, 0x0, 0x1E)
    OP_8C(0x17, 90, 400)
    OP_8E(0x17, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x17, 0xFF)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x18, 400)
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x18, 0x101, 400)

    ChrTalk(    #368
        0x18,
        (
            "#141FI think it's about time we said\x01",
            "goodbye, as well.\x02\x03",

            "#141FI was a bit nervous at first,\x01",
            "but you kids did a fine job.\x02\x03",

            "#147FLet me just say thank you\x01",
            "to the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#502FThat's what I like to call\x01",
            "raw skill. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x18,
        (
            "#142FNow don't get all cocky on me.\x02\x03",

            "#142FThe bracers I know would make\x01",
            "you two look like little fledglings,\x01",
            "not ready to leave the nest.\x02\x03",

            "#142FYou're going to need to\x01",
            "work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        "#007F...I'll try to remember that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x102,
        (
            "#010FSo are the two of you headed\x01",
            "back to the company soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x18,
        (
            "#141FNah, we're going to spend a day\x01",
            "or so relaxing here in Rolent.\x02\x03",

            "#141FI need to write up a rough draft\x01",
            "for some articles and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x19,
        (
            "#151FI'll head over to the orbal factory\x01",
            "and get these photographs\x01",
            "developed.\x02\x03",

            "#151FTake it easy, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x1D)
    OP_43(0x18, 0x1, 0x0, 0x1E)
    OP_8C(0x18, 90, 400)
    OP_8E(0x18, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x18, 0xFF)
    OP_51(0x1B, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x1B, 0x3E8)
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #375
        0x101,
        (
            "#000FI guess this is the last of the\x01",
            "jobs we got from Dad...\x02\x03",

            "#000FThey were much tougher than\x01",
            "I thought they'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x102,
        (
            "#010FI agree with you there.\x02\x03",

            "#010FI feel like I have a greater awareness\x01",
            "now about what it means to be a bracer.\x01",
            "It's not just about fighting for justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#001FThere you go again, saying all\x01",
            "the right things.\x02\x03",

            "#006FBut, yeah...I guess I get where\x01",
            "you're coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x102,
        (
            "#019FIt seems like we've got a long\x01",
            "road ahead of us if we want to\x01",
            "succeed in this profession...\x02\x03",

            "#019FFor the time being, why don't\x01",
            "we report to the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x101,
        (
            "#006FThat sounds like a good idea.\x02\x03",

            "#004FOh, but before we go, how are\x01",
            "you doing? Still not feeling well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x102,
        (
            "#010FThanks for asking.\x02\x03",

            "#010FBut I'm feeling a lot better.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    Return()

    # Function_28_7C1D end

    def Function_29_8623(): pass

    label("Function_29_8623")

    Sleep(500)
    OP_8C(0x19, 90, 400)
    OP_8E(0x19, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    Return()

    # Function_29_8623 end

    def Function_30_8644(): pass

    label("Function_30_8644")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_866D")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    TurnDirection(0x18, 0xFE, 0)
    OP_48()
    Jump("Function_30_8644")

    label("loc_866D")

    Return()

    # Function_30_8644 end

    def Function_31_866E(): pass

    label("Function_31_866E")

    OP_6B(2800, 1300)
    Return()

    # Function_31_866E end

    def Function_32_8678(): pass

    label("Function_32_8678")

    OP_6C(270000, 1300)
    Return()

    # Function_32_8678 end

    def Function_33_8682(): pass

    label("Function_33_8682")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x22)
    OP_43(0x102, 0x0, 0x0, 0x23)
    OP_43(0x0, 0x1, 0x0, 0x24)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x2)
    StopSound(0x9470, 0x30D40, 0x0)
    OP_6D(50063, 0, 24460, 8000)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x2)
    Fade(1000)
    OP_6D(48500, 0, 16400, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    Sleep(1000)

    ChrTalk(    #381
        0x102,
        (
            "#010FIt looks like we made good time.\x02\x03",

            "Not too early or too late, either.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #382
        0x101,
        (
            "#007FWe just barely graduated from Sunday School...\x02\x03",

            "I never dreamed we'd have to study so hard to\x01",
            "become bracers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #383
        0x102,
        (
            "#010FWell, you're in luck. Today is our last day of training.\x02\x03",

            "Truth be told though, you're the one who signed up to be a bracer in\x01",
            "the first place, so I don't know why you'd expect to get away with\x01",
            "any less effort.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #384
        0x101,
        (
            "#505FOh, yeah, I guess I did...\x02\x03",

            "#006FAll right, then!\x02\x03",

            "Let's get to it and make it through this last\x01",
            "hazing from Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x102,
        (
            "#019FYou look ready to me.\x02\x03",

            "Let's go meet with Schera at the Bracer Guild\x01",
            "over there, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_A2(0x203)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_33_8682 end

    def Function_34_89CF(): pass

    label("Function_34_89CF")

    OP_A6(0x0)
    Sleep(5000)
    OP_8E(0xFE, 0xBCAC, 0x0, 0x3C28, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_34_89CF end

    def Function_35_89EF(): pass

    label("Function_35_89EF")

    OP_A6(0x1)
    Sleep(5000)
    OP_8E(0xFE, 0xC15C, 0x0, 0x3B60, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_35_89EF end

    def Function_36_8A0F(): pass

    label("Function_36_8A0F")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_36_8A0F end

    def Function_37_8A16(): pass

    label("Function_37_8A16")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x26)
    OP_43(0x102, 0x0, 0x0, 0x27)
    OP_43(0x9, 0x0, 0x0, 0x28)
    OP_43(0xA, 0x0, 0x0, 0x29)
    OP_43(0x0, 0x1, 0x0, 0x2A)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_A2(0x3)
    OP_A5(0x3)

    ChrTalk(    #386
        0x9,
        "Hurry up and come on!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Sleep(1500)

    ChrTalk(    #387
        0xA,
        "W-Wait for me, Luke!\x02",
    )

    CloseMessageWindow()
    OP_A5(0x4)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x4)
    OP_6D(49690, 0, 23330, 2500)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x4)

    ChrTalk(    #388
        0x101,
        "#501FHuh? Oh, it's you two.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_A5(0x3)
    SetChrName("Luke")

    ChrTalk(    #389
        0x9,
        "Oh, great, it's Estelle...\x02",
    )

    CloseMessageWindow()
    SetChrName("Pat")

    ChrTalk(    #390
        0xA,
        "Hi there, Joshua!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    ChrTalk(    #391
        0x101,
        (
            "#007FOkay, you little twerp, what's\x01",
            "with the 'Oh, great, it's\x01",
            "Estelle...' remark?\x02\x03",

            "#006FAnd what's the big hurry?\x01",
            "How about telling us where\x01",
            "you're headed? \x02\x03",

            "#006FYou're not thinking about wandering\x01",
            "out of town alone, are you? The roads\x01",
            "are full of monsters, I hope you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x9,
        "You're such a pest, Estelle! \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x9,
        (
            "Don't you know there's no room\x01",
            "for GIRLS to be sticking their big\x01",
            "fat noses in BOYS' business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x9,
        (
            "Quit acting like you're a bracer,\x01",
            "you wannabe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        (
            "#006FTsk tsk! How wrong you are,\x01",
            "Luke! How incredibly wrong!\x02\x03",

            "#006FYou're more wrong than a fool who thinks\x01",
            "there's better tasting milk in Liberl than\x01",
            "the milk that comes from the Perzel Farm!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x9,
        "What...? N-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x9,
        "You're full of it, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x101,
        (
            "#502FIn fact, as of just a few minutes\x01",
            "ago we qualified to become real\x01",
            "bracers!\x02\x03",

            "#502FAre you hearing what I'm saying?\x01",
            "REAL BRACERS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x102,
        (
            "#019FMore like bracers-in-training, really. Don't think\x01",
            "you should be getting on your high horse just yet,\x01",
            "Estelle. Now a high 'pony' on the other hand...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #400
        0x101,
        "#509FQuit being a killjoy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xA,
        (
            "Wow! You two are great!\x01",
            "I'm so happy for the both of you!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(    #402
        0x101,
        (
            "#001FOh, Pat! You're such a good\x01",
            "little boy.\x02\x03",

            "Unlike that smart-aleck and\x01",
            "cynical brat you call a friend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x9,
        (
            "Th-This isn't fair! I was supposed\x01",
            "to become a bracer first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x9,
        (
            "I can accept that Joshua became\x01",
            "a bracer before me...but getting\x01",
            "passed by the likes of Estelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(    #405
        0x101,
        (
            "#005FWhat's 'the likes of Estelle'\x01",
            "supposed to mean?!\x02\x03",

            "#005FJust so you know, you can't even be\x01",
            "a bracer until you're 16 years old!\x01",
            "Get it? Only MATURE people allowed.\x02\x03",

            "#005FAnd that means no little kids who are\x01",
            "still going to Sunday School!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x102,
        (
            "#018FI don't know how I should put\x01",
            "this, Estelle, but...Sunday School\x01",
            "is dying to have you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x9,
        "You'd better watch out, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x9,
        (
            "I'm going to go train at my secret\x01",
            "base and before you know it,\x01",
            "I'm gonna be a bracer, too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(    #409
        0x9,
        (
            "Come on, Pat!\x01",
            "Let's go!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(    #410
        0xA,
        "A-All right...I'm coming...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1, 0)

    ChrTalk(    #411
        0xA,
        (
            "See you later, Estelle!\x01",
            "Bye, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_9359():
        OP_6D(49470, 0, 24950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9359)

    def lambda_9371():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9371)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x3)
    OP_A2(0x4)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x3)
    OP_A5(0x4)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)

    ChrTalk(    #412
        0x101,
        (
            "#007FThat boy, Luke...he's always\x01",
            "trying to pick a fight with me.\x02\x03",

            "#007FI wonder if he just plain hates\x01",
            "me or something...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #413
        0x102,
        (
            "#011FRather, I think it's the\x01",
            "exact opposite.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #414
        0x101,
        "#004FWhat do you mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x102,
        (
            "#019FDon't worry about it.\x01",
            "It's just a boy thing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #416
        0x102,
        (
            "#013FAt any rate, what do you think Luke meant\x01",
            "when he said 'secret base'? I don't know why,\x01",
            "but somehow it makes me a bit curious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        (
            "#001FI know exactly what you mean!\x01",
            "A secret base sounds really\x01",
            "intriguing!\x02\x03",

            "#001FThe pure heart of a young child\x01",
            "can be so inspiring at times!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #418
        0x102,
        (
            "#018FThat's not really what I meant\x01",
            "by 'curious'...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x206)
    EventEnd(0x0)
    Return()

    # Function_37_8A16 end

    def Function_38_9684(): pass

    label("Function_38_9684")

    OP_A6(0x0)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC1F2, 0x0, 0x5FDC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_A3(0x0)
    OP_A6(0x0)

    label("loc_96D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_96E5")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_96D3")

    label("loc_96E5")

    Return()

    # Function_38_9684 end

    def Function_39_96E6(): pass

    label("Function_39_96E6")

    OP_A6(0x1)
    Sleep(1000)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC710, 0x0, 0x623E, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_9723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9735")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_9723")

    label("loc_9735")

    Return()

    # Function_39_96E6 end

    def Function_40_9736(): pass

    label("Function_40_9736")

    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xBF2C, 0x0, 0x57A8, 0x1388, 0x0)
    OP_8C(0xFE, 160, 400)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x1F40)
    OP_8C(0xFE, 0, 800)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x3)
    Return()

    # Function_40_9736 end

    def Function_41_981E(): pass

    label("Function_41_981E")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xC2EC, 0x0, 0x4826, 0x1388, 0x0)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6C(12000, 2500)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_8E(0xFE, 0xC288, 0x0, 0x5410, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_A3(0x4)
    OP_A6(0x4)
    Sleep(500)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x4)
    Return()

    # Function_41_981E end

    def Function_42_98D4(): pass

    label("Function_42_98D4")

    OP_A6(0x2)
    OP_6D(49800, 0, 19520, 3000)
    OP_A3(0x2)
    Return()

    # Function_42_98D4 end

    def Function_43_98EC(): pass

    label("Function_43_98EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98FF")
    Call(0, 54)
    Jump("loc_997F")

    label("loc_98FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_9909")
    Jump("loc_997F")

    label("loc_9909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_991C")
    Call(0, 53)
    Jump("loc_997F")

    label("loc_991C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_992F")
    Call(0, 52)
    Jump("loc_997F")

    label("loc_992F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_993D")
    Jump("loc_997F")

    label("loc_993D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_994B")
    Call(0, 51)
    Jump("loc_997F")

    label("loc_994B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_9955")
    Jump("loc_997F")

    label("loc_9955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_9963")
    Call(0, 50)
    Jump("loc_997F")

    label("loc_9963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_9971")
    Call(0, 44)
    Jump("loc_997F")

    label("loc_9971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_997F")
    Call(0, 49)
    Jump("loc_997F")

    label("loc_997F")

    Return()

    # Function_43_98EC end

    def Function_44_9980(): pass

    label("Function_44_9980")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 51370, 0, 29175, 180)
    OP_43(0x101, 0x0, 0x0, 0x2D)
    OP_43(0x102, 0x0, 0x0, 0x2E)
    OP_43(0x8, 0x0, 0x0, 0x2F)
    OP_43(0x0, 0x1, 0x0, 0x30)

    ChrTalk(    #419
        0x8,
        (
            "Estelle! Joshua!\x01",
            "Am I glad I found you two!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 49700, 0, 15020, 315)
    SetChrPos(0x102, 48380, 0, 15120, 0)
    SetChrPos(0x8, 49950, 0, 25270, 180)
    OP_6B(3000, 0)
    OP_6D(50250, 0, 16110, 0)
    OP_6C(156000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_0D()
    OP_8E(0x8, 0xC030, 0x0, 0x4C22, 0x1388, 0x0)

    ChrTalk(    #420
        0x101,
        "#004FOh, hi, Aina!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x102,
        (
            "#014FIs something wrong?\x01",
            "You seem to be in\x01",
            "quite a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        (
            "#742FWe've got a bit of a problem.\x02\x03",

            "Is your father at home today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        (
            "#002FYes, he is. He said something\x01",
            "about having to sort out a bunch\x01",
            "of documents.\x02\x03",

            "#002FBut...what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x8,
        "#742FYou know Luke and Pat, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        (
            "#002FSure we do.\x01",
            "In fact, we saw them\x01",
            "not that long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        (
            "#012FWhat's wrong?\x01",
            "Are they in some sort of trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x8,
        (
            "#742FI don't know how to say this, but...\x02\x03",

            "I just heard from Yuni that Luke and\x01",
            "Pat ran off to the tower that lies on\x01",
            "the northern outskirts of Rolent!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #428
        0x101,
        (
            "#004FYou mean the Tower of Esmelas?!\x02\x03",

            "#004FIsn't that place supposed to be a\x01",
            "breeding ground for monsters?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x8,
        (
            "#742FThat's what they say...\x02\x03",

            "Unfortunately, at the moment, Scherazard is\x01",
            "out on other bracer business, so I want to\x01",
            "ask your father to bring the boys home safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x101,
        (
            "#005FWhat are you talking about?! \x02\x03",

            "#005FThere's no time for that!\x01",
            "Joshua and I will go after them\x01",
            "and bring them back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x8,
        (
            "#745FI don't know if that's such a good idea...\x01",
            "The two of you only just qualified to be\x01",
            "junior bracers today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x102,
        (
            "#012FWith all due respect, I believe\x01",
            "that Estelle's judgment is correct\x01",
            "in this situation. \x02\x03",

            "#012FIf the two of us hurry, we may even\x01",
            "be able to catch up with the boys\x01",
            "before they reach the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x8,
        (
            "#744F...\x02\x03",

            "#742FI understand. I will take responsibility\x01",
            "for whatever happens.\x02\x03",

            "As an emergency request from the Bracer\x01",
            "Guild, I ask that you lose no time in bringing\x01",
            "about the safe return of these children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        "#006FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x102,
        "#012FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x8,
        (
            "#742FThe Esmelas Tower can be reached\x01",
            "by taking the western path at the\x01",
            "junction along the Malga Trail.\x02\x03",

            "You can get onto the Malga Trail\x01",
            "though Rolent's northwest gate.\x02\x03",

            "I'll be on standby at the guild, so\x01",
            "if you run into any trouble, you\x01",
            "know where to find me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_8E(0x8, 0xC31E, 0x0, 0x62B6, 0x1388, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(    #437
        0x101,
        "#002FThis is our first real job...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(    #438
        0x101,
        (
            "#6P#005FCome on, Joshua!\x01",
            "We don't have any time to lose!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #439
        0x102,
        "#012FI'm right behind you!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 48920, 0, 15320, 0)
    SetChrPos(0x102, 48920, 0, 15320, 0)
    OP_6C(0, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x20C)
    OP_28(0x1, 0x1, 0x1)
    OP_28(0x1, 0x1, 0x2)
    OP_28(0x1, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_44_9980 end

    def Function_45_A2DC(): pass

    label("Function_45_A2DC")

    OP_A6(0x0)

    label("loc_A2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2F1")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A2DF")

    label("loc_A2F1")

    OP_A6(0x0)

    label("loc_A2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A306")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A2F4")

    label("loc_A306")

    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_45_A2DC end

    def Function_46_A31B(): pass

    label("Function_46_A31B")

    OP_A6(0x1)

    label("loc_A31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A330")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A31E")

    label("loc_A330")

    OP_A6(0x1)

    label("loc_A333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A345")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_A333")

    label("loc_A345")

    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_46_A31B end

    def Function_47_A35A(): pass

    label("Function_47_A35A")

    OP_A6(0x5)
    OP_8E(0xFE, 0xC2F6, 0x0, 0x4902, 0x1388, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    OP_A6(0x5)
    OP_8E(0xFE, 0xC8AA, 0x0, 0x71F7, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    Return()

    # Function_47_A35A end

    def Function_48_A3A7(): pass

    label("Function_48_A3A7")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_48_A3A7 end

    def Function_49_A3AE(): pass

    label("Function_49_A3AE")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #440
        0x102,
        (
            "#014FEstelle, aren't you forgetting\x01",
            "something?\x02\x03",

            "Dad asked us to pick up a copy\x01",
            "of the Liberl News for him at the\x01",
            "general goods store, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #441
        0x101,
        (
            "#008FOh, right.\x01",
            "Completely slipped my mind...\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_49_A3AE end

    def Function_50_A49F(): pass

    label("Function_50_A49F")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #442
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",

            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #443
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_50_A49F end

    def Function_51_A55B(): pass

    label("Function_51_A55B")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #444
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",

            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #445
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_51_A55B end

    def Function_52_A60F(): pass

    label("Function_52_A60F")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #446
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",

            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #447
        0x101,
        "#000FOh, yeah...that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_52_A60F end

    def Function_53_A6C9(): pass

    label("Function_53_A6C9")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #448
        0x102,
        (
            "#015FIf you want to go to the Esmelas\x01",
            "Tower, you'll need to go out the\x01",
            "northwest gate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #449
        0x101,
        (
            "#000FAh...I knew that.\x02\x03",

            "The small gate to the side of\x01",
            "the landing port, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_A6C9 end

    def Function_54_A7A6(): pass

    label("Function_54_A7A6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_A8C3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A847")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #450
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",

            "Let's get over to the landing port.\x01",
            "We may be able to catch her in time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C0")

    label("loc_A847")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #451
        0x103,
        (
            "#022FThere's no reason for us to head\x01",
            "out on the road now.\x02\x03",

            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C0")

    Jump("loc_A9C3")

    label("loc_A8C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A94D")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #452
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",

            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9C3")

    label("loc_A94D")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #453
        0x103,
        (
            "#022FThere's no reason for us to head\x01",
            "out on the road now.\x02\x03",

            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9C3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_A7A6 end

    def Function_55_A9DF(): pass

    label("Function_55_A9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9F2")
    Call(0, 63)
    Jump("loc_AA7A")

    label("loc_A9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A9FC")
    Jump("loc_AA7A")

    label("loc_A9FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA0F")
    Call(0, 62)
    Jump("loc_AA7A")

    label("loc_AA0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA22")
    Call(0, 61)
    Jump("loc_AA7A")

    label("loc_AA22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA30")
    Jump("loc_AA7A")

    label("loc_AA30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_AA3E")
    Call(0, 56)
    Jump("loc_AA7A")

    label("loc_AA3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_AA4C")
    Call(0, 56)
    Jump("loc_AA7A")

    label("loc_AA4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_AA5A")
    Call(0, 56)
    Jump("loc_AA7A")

    label("loc_AA5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_AA68")
    Call(0, 56)
    Jump("loc_AA7A")

    label("loc_AA68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_AA76")
    Call(0, 56)
    Jump("loc_AA7A")

    label("loc_AA76")

    Call(0, 56)

    label("loc_AA7A")

    Return()

    # Function_55_A9DF end

    def Function_56_AA7B(): pass

    label("Function_56_AA7B")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_AB1D")

    ChrTalk(    #454
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",

            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #455
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD76")

    label("loc_AB1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_ABA1")

    ChrTalk(    #456
        0x102,
        (
            "#010FIt's already evening.\x02\x03",

            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #457
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD76")

    label("loc_ABA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_AC42")

    ChrTalk(    #458
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",

            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #459
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD76")

    label("loc_AC42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_ACDE")

    ChrTalk(    #460
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",

            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #461
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD76")

    label("loc_ACDE")


    ChrTalk(    #462
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",

            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #463
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()

    label("loc_AD76")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_AA7B end

    def Function_57_AD92(): pass

    label("Function_57_AD92")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #464
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",

            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #465
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_57_AD92 end

    def Function_58_AE97(): pass

    label("Function_58_AE97")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #466
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",

            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #467
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_58_AE97 end

    def Function_59_AF96(): pass

    label("Function_59_AF96")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #468
        0x102,
        (
            "#012FThe Malga Trail is through\x01",
            "the northwest gate.\x02\x03",

            "#012F...That's the smaller exit\x01",
            "next to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #469
        0x101,
        "#002FI-I know already.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_59_AF96 end

    def Function_60_B09A(): pass

    label("Function_60_B09A")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #470
        0x102,
        (
            "#010FIt's already evening.\x02\x03",

            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #471
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_60_B09A end

    def Function_61_B181(): pass

    label("Function_61_B181")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #472
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",

            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #473
        0x101,
        "#000FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_61_B181 end

    def Function_62_B23A(): pass

    label("Function_62_B23A")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #474
        0x102,
        (
            "#015FIf you want to go to the Esmelas\x01",
            "Tower, you'll need to go out the\x01",
            "northwest gate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #475
        0x101,
        (
            "#000FOh, right.\x02\x03",

            "The small gate to the side of\x01",
            "the landing port, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_62_B23A end

    def Function_63_B310(): pass

    label("Function_63_B310")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_B42D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B3B1")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #476
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",

            "Let's get over to the landing port.\x01",
            "We may be able to catch her in time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42A")

    label("loc_B3B1")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #477
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",

            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42A")

    Jump("loc_B52D")

    label("loc_B42D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B4B7")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #478
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",

            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B52D")

    label("loc_B4B7")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #479
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",

            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B52D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_63_B310 end

    def Function_64_B549(): pass

    label("Function_64_B549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B55C")
    Call(0, 70)
    Jump("loc_B5CD")

    label("loc_B55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_B566")
    Jump("loc_B5CD")

    label("loc_B566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B579")
    Call(0, 69)
    Jump("loc_B5CD")

    label("loc_B579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B587")
    Jump("loc_B5CD")

    label("loc_B587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_B595")
    Call(0, 65)
    Jump("loc_B5CD")

    label("loc_B595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B5A3")
    Call(0, 65)
    Jump("loc_B5CD")

    label("loc_B5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_B5AD")
    Jump("loc_B5CD")

    label("loc_B5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_B5BB")
    Call(0, 65)
    Jump("loc_B5CD")

    label("loc_B5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_B5C9")
    Call(0, 65)
    Jump("loc_B5CD")

    label("loc_B5C9")

    Call(0, 65)

    label("loc_B5CD")

    Return()

    # Function_64_B549 end

    def Function_65_B5CE(): pass

    label("Function_65_B5CE")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_B670")

    ChrTalk(    #480
        0x102,
        (
            "#010FLet's head over to the guild,\x01",
            "Estelle.\x02\x03",

            "#010FWe'd better ask Aina what jobs\x01",
            "she has lined up for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #481
        0x101,
        "#000FGood thinking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B832")

    label("loc_B670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B6F4")

    ChrTalk(    #482
        0x102,
        (
            "#010FIt's already evening.\x02\x03",

            "#010FI'm sure Dad's waiting for us,\x01",
            "so let's head home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #483
        0x101,
        "#000FYeah, I'm beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B832")

    label("loc_B6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_B6FE")
    Jump("loc_B832")

    label("loc_B6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_B79A")

    ChrTalk(    #484
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",

            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #485
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B832")

    label("loc_B79A")


    ChrTalk(    #486
        0x102,
        (
            "#010FIt's almost time to start our\x01",
            "training, Estelle.\x02\x03",

            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #487
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()

    label("loc_B832")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_65_B5CE end

    def Function_66_B84E(): pass

    label("Function_66_B84E")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #488
        0x102,
        (
            "#010FIt's almost time to start\x01",
            "our training, Estelle.\x02\x03",

            "#010FLet's head over to the guildhouse\x01",
            "on the south avenue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #489
        0x101,
        "#007FOh, all right.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_66_B84E end

    def Function_67_B953(): pass

    label("Function_67_B953")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #490
        0x102,
        (
            "#010FEstelle, let's head home.\x02\x03",

            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #491
        0x101,
        "#000FYeah, I forgot about that.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_67_B953 end

    def Function_68_BA52(): pass

    label("Function_68_BA52")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #492
        0x102,
        (
            "#010FWait, Estelle.\x02\x03",

            "#010FWe haven't bought a copy of the\x01",
            "Liberl News from Mr. Rinon's place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #493
        0x101,
        (
            "#000FWhoops. Totally forgot about that.\x01",
            "We'd better get over to the general\x01",
            "goods store then.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_68_BA52 end

    def Function_69_BB8C(): pass

    label("Function_69_BB8C")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #494
        0x102,
        (
            "#010FShouldn't we stop by the\x01",
            "orbal factory?\x02\x03",

            "We're supposed to meet up with\x01",
            "that camerawoman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        "#000FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_69_BB8C end

    def Function_70_BC3E(): pass

    label("Function_70_BC3E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_BD5B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCDF")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #496
        0x103,
        (
            "#022FAnd where do you think\x01",
            "you're going?\x02\x03",

            "Let's get over to the landing port.\x01",
            "We may be able to catch her in\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD58")

    label("loc_BCDF")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #497
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",

            "Let's hurry up and get over\x01",
            "to the landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD58")

    Jump("loc_BE5B")

    label("loc_BD5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDE5")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #498
        0x103,
        (
            "#022FWhere in the world do you two\x01",
            "think you're going?\x02\x03",

            "Right now, we need to go\x01",
            "and check the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE5B")

    label("loc_BDE5")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #499
        0x103,
        (
            "#022FThere's no reason for us to\x01",
            "head out on the road now.\x02\x03",

            "Let's get over to the hotel\x01",
            "and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE5B")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_70_BC3E end

    def Function_71_BE77(): pass

    label("Function_71_BE77")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x102, 54640, 0, 43670, 0)
    SetChrPos(0x101, 55690, 0, 43940, 0)
    OP_6D(55160, 1000, 47020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(314000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_BF00():
        OP_6D(55160, 9000, 47020, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF00)
    OP_6C(44000, 7000)
    Fade(1000)
    OP_6D(55310, 0, 45740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #500
        (
            "\x07\x05《Septian Calendar 1075》\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #501
        (
            "\x07\x05《Septian Calendar 1192》\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #502
        (
            "\x07\x05《Septian Calendar 1197》\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #503
        0x102,
        (
            "#010F#1PEvery time I see this clock tower,\x01",
            "I always think...\x02\x03",

            "They sure did a superb job restoring\x01",
            "it after the war.\x02\x03",

            "You can sure feel the spirit of\x01",
            "Rolent's people from this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x101,
        "#500F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #505
        0x102,
        "#014F#1PEstelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #506
        0x101,
        (
            "#501F#4PUm, Joshua...\x02\x03",

            "What do you think about going up\x01",
            "with me and waiting until Schera\x01",
            "shows up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0x102,
        (
            "#014F#1PYou mean the clock tower?\x01",
            "Sure, I don't mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0x101,
        "#000F#4POkay, come on.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_71_BE77 end

    def Function_72_C298(): pass

    label("Function_72_C298")

    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    AddParty(0x2, 0xFF)
    OP_A2(0x301)
    EventBegin(0x0)
    SetMapFlags(0x1)
    SetChrPos(0x102, 51920, 0, 49090, 180)
    SetChrPos(0x101, 53010, 0, 50110, 270)
    SetChrPos(0x103, 56060, 0, 43300, 270)
    OP_6C(45000, 0)
    OP_6A(0x102)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4A)
    OP_8E(0x102, 0xCA12, 0x0, 0xAC9E, 0xBB8, 0x0)
    ClearMapFlags(0x1)
    OP_43(0x102, 0x0, 0x0, 0x49)
    OP_6D(55290, 0, 43570, 1500)
    OP_6A(0x0)
    ClearMapFlags(0x1)

    ChrTalk(    #509
        0x103,
        (
            "#021FAwww...\x01",
            "The two of you had such a cute\x01",
            "scene going on up there.\x02\x03",

            "Why, my cheeks even feel a bit\x01",
            "hot just thinking about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #510
        0x102,
        (
            "#014F#4PWhat's that supposed to mean?\x02\x03",

            "#014FYou were spying on us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x103,
        (
            "#027FGive me some credit, will you?\x02\x03",

            "I just happened to see you when\x01",
            "I looked up to check the time.\x02\x03",

            "#021FI sure wish I had an orbal camera\x01",
            "to get a shot of that view...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x102,
        "#018F#4PCome on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        (
            "#001FWhat are you trying to say, Schera?\x01",
            "That's called family bonding, plain\x01",
            "and simple.\x02\x03",

            "It's kind of like your habit of\x01",
            "hugging everyone after your\x01",
            "third bottle of wine.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #514
        0x102,
        "#017F#4P*sigh* Let's not get into that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #515
        0x101,
        "#501FWhat's with the sigh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x103,
        (
            "#025FYou really don't know how\x01",
            "to take a joke, do you?\x02\x03",

            "#020FWell, whatever.\x01",
            "Did you say hi to Lena\x01",
            "while you were up there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #517
        0x101,
        (
            "#000FYeah...\x02\x03",

            "I even asked for her to\x01",
            "watch over Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x103,
        (
            "#021FI see, then I guess it looks\x01",
            "like you're all set.\x02\x03",

            "You know, Lena's protection is\x01",
            "equal to that of the Goddess,\x01",
            "herself.\x02\x03",

            "Your dad's safety is pretty\x01",
            "much guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x101,
        (
            "#008FI think you may be giving her\x01",
            "a little too much credit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x102,
        (
            "#010F#4PNow that you mention it,\x01",
            "you met Estelle's mother\x01",
            "before, right, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x103,
        (
            "#020FYeah...when I was a child.\x02\x03",

            "I was still in a troupe at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x102,
        "#014F#4PA troupe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x101,
        (
            "#000FYeah, a troupe in a traveling\x01",
            "circus. Schera was a dancer.\x02\x03",

            "Although it was a long time ago,\x01",
            "we first met when she came to\x01",
            "Rolent with the circus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x103,
        (
            "#020F12 years ago to be exact.\x01",
            "I was 11 and Estelle was 4.\x02\x03",

            "And because of that chance encounter,\x01",
            "when I became a bracer, I trained\x01",
            "under your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x102,
        "#010F#4PI didn't know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0x103,
        (
            "#020FMaybe I'll tell you about it sometime\x01",
            "when I get a chance.\x02\x03",

            "Are you about ready to head\x01",
            "out for Bose?\x02\x03",

            "With airliner flights canceled, we'll\x01",
            "just have to make our way to Bose\x01",
            "the old-fashioned way: by foot.\x02\x03",

            "First, we'll need to make our way to\x01",
            "the Verte Bridge Checkpoint, which\x01",
            "sits on the border of the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x102,
        (
            "#010F#4PThe Verte Bridge is located at the\x01",
            "west end of the Milch Main Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0x101,
        (
            "#006FIt looks like we're all set,\x01",
            "so let's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x52, 0x4, 0x2)
    OP_28(0x52, 0x4, 0x4)
    OP_28(0x52, 0x1, 0x1)
    OP_3F(0x32A, 1)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x400000)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0xA)
    Return()

    # Function_72_C298 end

    def Function_73_CC1B(): pass

    label("Function_73_CC1B")

    OP_8E(0x102, 0xD50C, 0x0, 0xA690, 0xBB8, 0x0)
    OP_8C(0x102, 45, 400)
    Return()

    # Function_73_CC1B end

    def Function_74_CC37(): pass

    label("Function_74_CC37")

    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0xC9B8, 0x0, 0xC468, 0xBB8, 0x0)
    OP_8E(0x101, 0xCAF8, 0x0, 0xAC94, 0xBB8, 0x0)
    OP_8E(0x101, 0xD41C, 0x0, 0xAB86, 0xBB8, 0x0)
    ClearChrFlags(0x101, 0x4)
    TurnDirection(0x101, 0x103, 400)
    Return()

    # Function_74_CC37 end

    def Function_75_CC85(): pass

    label("Function_75_CC85")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #529
        "\x07\x05West: Malga Trail\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_75_CC85 end

    def Function_76_CCC9(): pass

    label("Function_76_CCC9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #530
        "\x07\x05North: Rolent Landing Port\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_CCC9 end

    def Function_77_CD16(): pass

    label("Function_77_CD16")

    SetPlaceName(0x4)
    Return()

    # Function_77_CD16 end

    def Function_78_CD1A(): pass

    label("Function_78_CD1A")

    SetPlaceName(0x2)
    Return()

    # Function_78_CD1A end

    def Function_79_CD1E(): pass

    label("Function_79_CD1E")

    SetPlaceName(0x6)
    Return()

    # Function_79_CD1E end

    def Function_80_CD22(): pass

    label("Function_80_CD22")

    SetPlaceName(0x5)
    Return()

    # Function_80_CD22 end

    def Function_81_CD26(): pass

    label("Function_81_CD26")

    SetPlaceName(0x7)
    Return()

    # Function_81_CD26 end

    def Function_82_CD2A(): pass

    label("Function_82_CD2A")

    SetPlaceName(0x8)
    Return()

    # Function_82_CD2A end

    def Function_83_CD2E(): pass

    label("Function_83_CD2E")

    SetPlaceName(0x3)
    Return()

    # Function_83_CD2E end

    def Function_84_CD32(): pass

    label("Function_84_CD32")

    SetPlaceName(0xA)
    Return()

    # Function_84_CD32 end

    def Function_85_CD36(): pass

    label("Function_85_CD36")

    SetPlaceName(0xC)
    Return()

    # Function_85_CD36 end

    def Function_86_CD3A(): pass

    label("Function_86_CD3A")

    SetPlaceName(0x9)
    Return()

    # Function_86_CD3A end

    def Function_87_CD3E(): pass

    label("Function_87_CD3E")

    SetPlaceName(0x15)
    Return()

    # Function_87_CD3E end

    def Function_88_CD42(): pass

    label("Function_88_CD42")

    SetPlaceName(0x16)
    Return()

    # Function_88_CD42 end

    def Function_89_CD46(): pass

    label("Function_89_CD46")

    SetPlaceName(0x17)
    Return()

    # Function_89_CD46 end

    SaveToFile()

Try(main)
