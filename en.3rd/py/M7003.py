from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7003   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
        '',                                     # 14
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
        'ED6_DT29/CH14400 ._CH',             # 00
        'ED6_DT29/CH14401 ._CH',             # 01
        'ED6_DT29/CH14410 ._CH',             # 02
        'ED6_DT29/CH14411 ._CH',             # 03
        'ED6_DT29/CH14780 ._CH',             # 04
        'ED6_DT29/CH14781 ._CH',             # 05
        'ED6_DT29/CH14420 ._CH',             # 06
        'ED6_DT29/CH14421 ._CH',             # 07
        'ED6_DT29/CH14010 ._CH',             # 08
        'ED6_DT29/CH14011 ._CH',             # 09
        'ED6_DT29/CH14020 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT29/CH14400P._CP',             # 00
        'ED6_DT29/CH14401P._CP',             # 01
        'ED6_DT29/CH14410P._CP',             # 02
        'ED6_DT29/CH14411P._CP',             # 03
        'ED6_DT29/CH14780P._CP',             # 04
        'ED6_DT29/CH14781P._CP',             # 05
        'ED6_DT29/CH14420P._CP',             # 06
        'ED6_DT29/CH14421P._CP',             # 07
        'ED6_DT29/CH14010P._CP',             # 08
        'ED6_DT29/CH14011P._CP',             # 09
        'ED6_DT29/CH14020P._CP',             # 0A
    )

    DeclMonster(
        X                   = -34690,
        Z                   = 0,
        Y                   = -48940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40290,
        Z                   = 0,
        Y                   = -54350,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3180,
        Z                   = -20000,
        Y                   = -1170,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1750,
        Z                   = -20000,
        Y                   = 3800,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34950,
        Z                   = -40000,
        Y                   = -48840,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39940,
        Z                   = -40000,
        Y                   = -53730,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -160,
        TriggerZ            = -20000,
        TriggerY            = 5210,
        TriggerRange        = 1000,
        ActorX              = -10,
        ActorZ              = -19000,
        ActorY              = 6110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37980,
        TriggerZ            = -40000,
        TriggerY            = -55600,
        TriggerRange        = 1000,
        ActorX              = -38070,
        ActorZ              = -40000,
        ActorY              = -56300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_21D",          # 01, 1
        "Function_2_278",          # 02, 2
        "Function_3_356",          # 03, 3
        "Function_4_434",          # 04, 4
        "Function_5_4F0",          # 05, 5
        "Function_6_5AC",          # 06, 6
        "Function_7_6C2",          # 07, 7
        "Function_8_710",          # 08, 8
        "Function_9_85B",          # 09, 9
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_20E"),
        (101, "loc_215"),
        (SWITCH_DEFAULT, "loc_21C"),
    )


    label("loc_20E")

    Event(0, 2)
    Jump("loc_21C")

    label("loc_215")

    Event(0, 3)
    Jump("loc_21C")

    label("loc_21C")

    Return()

    # Function_0_1F2 end

    def Function_1_21D(): pass

    label("Function_1_21D")

    OP_16(0x2, 0xFA0, 0xFFFDBBEC, 0xFFFDA576, 0x23007F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245")
    OP_1B(0x0, 0x0, 0x4)
    OP_1B(0x1, 0x0, 0x5)

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_6F(0x0, 0)
    Jump("loc_25E")

    label("loc_257")

    OP_6F(0x0, 60)

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_6F(0x1, 0)
    Jump("loc_277")

    label("loc_270")

    OP_6F(0x1, 60)

    label("loc_277")

    Return()

    # Function_1_21D end

    def Function_2_278(): pass

    label("Function_2_278")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -920, 20000, 1870, 270)
    SetChrPos(0x1, -40, 20000, 2890, 270)
    SetChrPos(0x2, -100, 20000, 1110, 270)
    SetChrPos(0x3, 820, 20000, 2040, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 20000, 2100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_2_278 end

    def Function_3_356(): pass

    label("Function_3_356")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 40, -60000, 1110, 180)
    SetChrPos(0x1, -850, -60000, 1910, 180)
    SetChrPos(0x2, 990, -60000, 2190, 180)
    SetChrPos(0x3, -100, -60000, 3060, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 20, -60000, 2040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_356 end

    def Function_4_434(): pass

    label("Function_4_434")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -920, 20000, 1870, 90)
    SetChrPos(0x2, -40, 20000, 2890, 90)
    SetChrPos(0x1, -100, 20000, 1110, 90)
    SetChrPos(0x0, 820, 20000, 2040, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 20000, 2100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    NewScene("ED6_DT21/M7002   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_4_434 end

    def Function_5_4F0(): pass

    label("Function_5_4F0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 40, -60000, 1110, 0)
    SetChrPos(0x2, -850, -60000, 1910, 0)
    SetChrPos(0x1, 990, -60000, 2190, 0)
    SetChrPos(0x0, -100, -60000, 3060, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 20, -60000, 2040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    NewScene("ED6_DT21/M7004   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_4F0 end

    def Function_6_5AC(): pass

    label("Function_6_5AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D5")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5C9)

    label("loc_5D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FE")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5F2)

    label("loc_5FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_627")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_61B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_61B)

    label("loc_627")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_650")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_644():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_644)

    label("loc_650")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67C")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_67C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_693")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_693")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AA")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C1")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6C1")

    Return()

    # Function_6_5AC end

    def Function_7_6C2(): pass

    label("Function_7_6C2")


    def lambda_6C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6C8)

    def lambda_6DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6DA)

    def lambda_6EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6EC)

    def lambda_6FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6FE)
    Sleep(1000)
    Return()

    # Function_7_6C2 end

    def Function_8_710(): pass

    label("Function_8_710")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19B, 1)"), scpexpr(EXPR_END)), "loc_77E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x9B\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2698)
    Jump("loc_7E6")

    label("loc_77E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x9B\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9B\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_7E6")

    Jump("loc_84D")

    label("loc_7E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Empty chest? Why not fill it up again at Bose Market? --Maybelle\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xAA, 0x0)

    label("loc_84D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_710 end

    def Function_9_85B(): pass

    label("Function_9_85B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_919")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)

    AnonymousTalk(    #3
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2699)
    Jump("loc_96B")

    label("loc_919")


    AnonymousTalk(    #4
        "\x07\x05I hear Olivier makes his pack Mueller carry all of his belongings for him.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_96B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xAB, 0x0)
    Return()

    # Function_9_85B end

    SaveToFile()

Try(main)
