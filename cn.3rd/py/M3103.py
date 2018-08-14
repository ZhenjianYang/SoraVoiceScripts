from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3103   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10060 ._CH',             # 00
        'ED6_DT09/CH10061 ._CH',             # 01
        'ED6_DT09/CH11210 ._CH',             # 02
        'ED6_DT09/CH11211 ._CH',             # 03
        'ED6_DT09/CH11030 ._CH',             # 04
        'ED6_DT09/CH11031 ._CH',             # 05
        'ED6_DT09/CH11020 ._CH',             # 06
        'ED6_DT09/CH11021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10060P._CP',             # 00
        'ED6_DT09/CH10061P._CP',             # 01
        'ED6_DT09/CH11210P._CP',             # 02
        'ED6_DT09/CH11211P._CP',             # 03
        'ED6_DT09/CH11030P._CP',             # 04
        'ED6_DT09/CH11031P._CP',             # 05
        'ED6_DT09/CH11020P._CP',             # 06
        'ED6_DT09/CH11021P._CP',             # 07
    )

    DeclMonster(
        X                   = 6190,
        Z                   = 0,
        Y                   = 21540,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x291,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23830,
        Z                   = 0,
        Y                   = 8039,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22280,
        Z                   = 0,
        Y                   = 28450,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x290,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10110,
        Z                   = 0,
        Y                   = 42760,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10870,
        Z                   = 0,
        Y                   = 16730,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 70,
        TriggerZ            = 0,
        TriggerY            = 45460,
        TriggerRange        = 800,
        ActorX              = 70,
        ActorZ              = 1200,
        ActorY              = 45460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_19B",          # 01, 1
        "Function_2_1AE",          # 02, 2
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Return()

    # Function_0_19A end

    def Function_1_19B(): pass

    label("Function_1_19B")

    OP_16(0x2, 0xFA0, 0xFFFE4698, 0xFFFE4698, 0x2300A8)
    Return()

    # Function_1_19B end

    def Function_2_1AE(): pass

    label("Function_2_1AE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05被毛玻璃遮住，无法窥视里面的情况。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_1AE end

    SaveToFile()

Try(main)
