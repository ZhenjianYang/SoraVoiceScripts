from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0102   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0102.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60020",
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
        'Rolent',                               # 9
        'Gurune Gate',                          # 10
        'Mistwald',                             # 11
        '赤茶玉虫',                             # 12
        'マーズスパロー',                       # 13
        'マーズスパロー',                       # 14
        '赤茶玉虫',                             # 15
        'マーズスパロー',                       # 16
        'マーズスパロー',                       # 17
        '赤茶玉虫',                             # 18
        '赤茶玉虫',                             # 19
        'マーズスパロー',                       # 20
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
        Unknown_3A              = 23,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
    )

    DeclNpc(
        X                   = -101100,
        Z                   = 1000,
        Y                   = 83200,
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
        X                   = -205500,
        Z                   = 1000,
        Y                   = -19070,
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
        X                   = -65750,
        Z                   = 1000,
        Y                   = 51180,
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


    DeclMonster(
        X                   = -107000,
        Z                   = 1000,
        Y                   = 43000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x21,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -125000,
        Z                   = 2000,
        Y                   = 34000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -106000,
        Z                   = 1000,
        Y                   = 20000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x24,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91000,
        Z                   = 1000,
        Y                   = 28000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -69000,
        Z                   = 1000,
        Y                   = 23000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -150000,
        Z                   = 1000,
        Y                   = -6000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -160000,
        Z                   = 1000,
        Y                   = -22000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x23,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151000,
        Z                   = 2000,
        Y                   = 8000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -138000,
        Z                   = 2000,
        Y                   = 4000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -115130,
        TriggerZ            = 970,
        TriggerY            = 25940,
        TriggerRange        = 1500,
        ActorX              = -115130,
        ActorZ              = 2700,
        ActorY              = 25940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -163860,
        TriggerZ            = 970,
        TriggerY            = -7310,
        TriggerRange        = 1500,
        ActorX              = -163860,
        ActorZ              = 2500,
        ActorY              = -7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28E",          # 00, 0
        "Function_1_28F",          # 01, 1
        "Function_2_2A2",          # 02, 2
        "Function_3_2F9",          # 03, 3
    )


    def Function_0_28E(): pass

    label("Function_0_28E")

    Return()

    # Function_0_28E end

    def Function_1_28F(): pass

    label("Function_1_28F")

    OP_16(0x2, 0xFA0, 0xFFFC1FD0, 0xFFFE5A20, 0x3000A)
    Return()

    # Function_1_28F end

    def Function_2_2A2(): pass

    label("Function_2_2A2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05East: Mistwald\x01",
            "※Beware of monsters!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_2A2 end

    def Function_3_2F9(): pass

    label("Function_3_2F9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05North: Rolent - 308 selge\x01",
            "West: Grancel - 193 selge\x01",
            "Gurune Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_2F9 end

    SaveToFile()

Try(main)
