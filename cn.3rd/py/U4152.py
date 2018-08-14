from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4152   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4152.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14451 ._CH',             # 01
        'ED6_DT29/CH14730 ._CH',             # 02
        'ED6_DT29/CH14730 ._CH',             # 03
        'ED6_DT29/CH14790 ._CH',             # 04
        'ED6_DT29/CH14791 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14451P._CP',             # 01
        'ED6_DT29/CH14730P._CP',             # 02
        'ED6_DT29/CH14730P._CP',             # 03
        'ED6_DT29/CH14790P._CP',             # 04
        'ED6_DT29/CH14791P._CP',             # 05
    )

    DeclMonster(
        X                   = -42290,
        Z                   = 0,
        Y                   = -4190,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -38330,
        Z                   = 40,
        Y                   = -37890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -74650,
        Z                   = -3500,
        Y                   = -24560,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -79070,
        Z                   = 0,
        Y                   = -3000,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16E",          # 00, 0
        "Function_1_182",          # 01, 1
        "Function_2_1BF",          # 02, 2
        "Function_3_31B",          # 03, 3
    )


    def Function_0_16E(): pass

    label("Function_0_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_181")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_181")

    Return()

    # Function_0_16E end

    def Function_1_182(): pass

    label("Function_1_182")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2")
    OP_10(0x1, 0x0)
    Jump("loc_1A8")

    label("loc_1A2")

    OP_71(0x426, 0x0)
    ExitThread()

    label("loc_1A8")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_182 end

    def Function_2_1BF(): pass

    label("Function_2_1BF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-68150, 1250, 4980, 0)
    OP_67(0, 11130, -10000, 0)
    OP_6B(4690, 0)
    OP_6C(57000, 0)
    OP_6E(421, 0)
    OP_0D()
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Fade(1000)
    OP_6D(-39910, 0, -570, 0)
    OP_67(0, 10460, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(0, 0)
    OP_6E(376, 0)

    def lambda_272():
        OP_6D(-40060, -3000, 34710, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_272)

    def lambda_28A():
        OP_67(0, 7150, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28A)

    def lambda_2A2():
        OP_6B(3020, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A2)

    def lambda_2B2():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2B2)

    def lambda_2C2():
        OP_6E(376, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2C2)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(1000)

    def lambda_2E1():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E1)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x426, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AE(0x5DC)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4151   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_1BF end

    def Function_3_31B(): pass

    label("Function_3_31B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_31B end

    SaveToFile()

Try(main)
