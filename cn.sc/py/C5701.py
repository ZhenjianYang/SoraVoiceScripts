from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5701   ._SN',
        MapName             = 'Other',
        Location            = 'C5701.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '工业区域『法克特里亚』１',             # 9
        '工业区域『法克特里亚』３',             # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12060 ._CH',             # 00
        'ED6_DT29/CH12061 ._CH',             # 01
        'ED6_DT29/CH12190 ._CH',             # 02
        'ED6_DT29/CH12191 ._CH',             # 03
        'ED6_DT29/CH12970 ._CH',             # 04
        'ED6_DT29/CH12971 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12060P._CP',             # 00
        'ED6_DT29/CH12061P._CP',             # 01
        'ED6_DT29/CH12190P._CP',             # 02
        'ED6_DT29/CH12191P._CP',             # 03
        'ED6_DT29/CH12970P._CP',             # 04
        'ED6_DT29/CH12971P._CP',             # 05
    )

    DeclNpc(
        X                   = 8150,
        Z                   = 4000,
        Y                   = -23500,
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
        X                   = 70670,
        Z                   = 4000,
        Y                   = 9930,
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
        X                   = 8000,
        Z                   = 4000,
        Y                   = 17890,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -50130,
        Z                   = 4000,
        Y                   = 8970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x514,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78880,
        Z                   = 4000,
        Y                   = 9720,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x515,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -50000,
        Y                   = 4650,
        Z                   = -30000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -107940,
        TriggerZ            = 4350,
        TriggerY            = 7670,
        TriggerRange        = 1000,
        ActorX              = -107540,
        ActorZ              = 5350,
        ActorY              = 7670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B2",          # 00, 0
        "Function_1_1D7",          # 01, 1
        "Function_2_20C",          # 02, 2
        "Function_3_242",          # 03, 3
        "Function_4_32E",          # 04, 4
        "Function_5_43E",          # 05, 5
    )


    def Function_0_1B2(): pass

    label("Function_0_1B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1C8")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_1D6")

    label("loc_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1D6")
    OP_A3(0x10F1)
    Event(0, 5)

    label("loc_1D6")

    Return()

    # Function_0_1B2 end

    def Function_1_1D7(): pass

    label("Function_1_1D7")

    OP_16(0x2, 0xFA0, 0xFFFDB9F8, 0xFFFE3310, 0x230075)
    OP_22(0x1C7, 0x0, 0x64)
    OP_10(0x3, 0x0)
    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 6)), scpexpr(EXPR_END)), "loc_20B")
    OP_71(0x0, 0x10)
    OP_71(0x2, 0x4)
    OP_64(0x0, 0x1)

    label("loc_20B")

    Return()

    # Function_1_1D7 end

    def Function_2_20C(): pass

    label("Function_2_20C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_20C end

    def Function_3_242(): pass

    label("Function_3_242")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-49940, 6000, -29920, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_2A4():
        OP_6D(-107940, 4350, 6860, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A4)
    OP_6C(315000, 7000)
    Fade(500)
    OP_6D(-109590, 4350, 9620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    OP_71(0x2, 0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_242 end

    def Function_4_32E(): pass

    label("Function_4_32E")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-49850, 6000, -29900, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x101, -50000, 6000, -29000, 0)
    OP_89(0x102, -51000, 6000, -30000, 0)
    OP_89(0xF8, -49000, 6000, -30000, 0)
    OP_89(0xF9, -50000, 6000, -31000, 0)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x258)
    StopSound(0x7530, 0x6DDD0, 0x1F40)

    def lambda_3E7():
        OP_6D(-49850, 55000, -29900, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E7)

    def lambda_3FF():
        OP_67(0, 10590, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FF)

    def lambda_417():
        OP_6C(30000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_417)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_32E end

    def Function_5_43E(): pass

    label("Function_5_43E")

    EventBegin(0x0)
    OP_6D(-49850, 60000, -29900, 0)
    OP_67(0, 10590, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    OP_11(0x92, 0xBE, 0xD2, 0x7530, 0x6DDD0, 0x0)
    OP_6F(0x1, 600)
    OP_48()
    OP_89(0x101, -50000, 80000, -29000, 0)
    OP_89(0x102, -51000, 80000, -30000, 0)
    OP_89(0xF8, -49000, 80000, -30000, 0)
    OP_89(0xF9, -50000, 80000, -31000, 0)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)
    StopSound(0x7530, 0x493E0, 0x2328)

    def lambda_4FA():
        OP_6D(-49850, 6000, -29900, 10500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FA)

    def lambda_512():
        OP_67(0, 6500, -10000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_512)

    def lambda_52A():
        OP_6C(45000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_52A)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(-49850, 6000, -28020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -49850, 6000, -28020, 0)
    SetChrPos(0x1, -49850, 6000, -28020, 0)
    SetChrPos(0x2, -49850, 6000, -28020, 0)
    SetChrPos(0x3, -49850, 6000, -28020, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_5_43E end

    SaveToFile()

Try(main)
