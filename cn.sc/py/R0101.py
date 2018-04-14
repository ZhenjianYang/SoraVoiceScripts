from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0101   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0101.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60029",
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
        '雾调整',                               # 9
        '洛连特方向',                           # 10
        '格鲁纳门方向',                         # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10240 ._CH',             # 00
        'ED6_DT09/CH10241 ._CH',             # 01
        'ED6_DT09/CH10230 ._CH',             # 02
        'ED6_DT09/CH10231 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10240P._CP',             # 00
        'ED6_DT09/CH10241P._CP',             # 01
        'ED6_DT09/CH10230P._CP',             # 02
        'ED6_DT09/CH10231P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35110,
        Z                   = 1000,
        Y                   = 185500,
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
        X                   = -122810,
        Z                   = 1000,
        Y                   = -720,
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
        X                   = -32000,
        Z                   = 1000,
        Y                   = 154000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42000,
        Z                   = 1400,
        Y                   = 142000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28000,
        Z                   = 2000,
        Y                   = 120000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47000,
        Z                   = 1000,
        Y                   = 122000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x14,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -55000,
        Z                   = 1000,
        Y                   = 106000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x15,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33000,
        Z                   = 1000,
        Y                   = 109000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83000,
        Z                   = 2000,
        Y                   = 84900,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94000,
        Z                   = 1000,
        Y                   = 62000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -106000,
        Z                   = 1000,
        Y                   = 42000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x14,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -125000,
        Z                   = 1000,
        Y                   = 34000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x15,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -126160,
        TriggerZ            = 1030,
        TriggerY            = 32310,
        TriggerRange        = 1000,
        ActorX              = -126630,
        ActorZ              = 1030,
        ActorY              = 32530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24690,
        TriggerZ            = 2009,
        TriggerY            = 123260,
        TriggerRange        = 1000,
        ActorX              = -24030,
        ActorZ              = 2000,
        ActorY              = 123440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91280,
        TriggerZ            = 970,
        TriggerY            = 78610,
        TriggerRange        = 1000,
        ActorX              = -96410,
        ActorZ              = -500,
        ActorY              = 77750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_3DC",          # 02, 2
        "Function_3_472",          # 03, 3
        "Function_4_589",          # 04, 4
        "Function_5_6A0",          # 05, 5
        "Function_6_C3E",          # 06, 6
        "Function_7_101A",         # 07, 7
        "Function_8_14A8",         # 08, 8
        "Function_9_162B",         # 09, 9
        "Function_10_16C7",        # 0A, 10
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8")
    Event(0, 7)
    Jump("loc_2DE")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DA")
    Event(0, 6)
    Jump("loc_2DE")

    label("loc_2DA")

    Event(0, 5)

    label("loc_2DE")

    Return()

    # Function_0_2AE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_16(0x2, 0xFA0, 0xFFFD0260, 0xFFFF63C0, 0x230009)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303")
    OP_6F(0x0, 0)
    Jump("loc_30A")

    label("loc_303")

    OP_6F(0x0, 60)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C")
    OP_6F(0x1, 0)
    Jump("loc_323")

    label("loc_31C")

    OP_6F(0x1, 60)

    label("loc_323")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_3DB")

    label("loc_35A")

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3DB")

    Return()

    # Function_1_2DF end

    def Function_2_3DC(): pass

    label("Function_2_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_471")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x28C58), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40F")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_424")

    label("loc_40F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_424")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x28C58), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_454")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_469")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_469")

    Sleep(10)
    Jump("Function_2_3DC")

    label("loc_471")

    Return()

    # Function_2_3DC end

    def Function_3_472(): pass

    label("Function_3_472")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_4E1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1910)
    Jump("loc_547")

    label("loc_4E1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_547")

    Jump("loc_57B")

    label("loc_54A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_57B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_472 end

    def Function_4_589(): pass

    label("Function_4_589")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x322, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x281, 1)"), scpexpr(EXPR_END)), "loc_5F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x81\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1911)
    Jump("loc_65E")

    label("loc_5F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x81\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x81\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_65E")

    Jump("loc_692")

    label("loc_661")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_692")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_589 end

    def Function_5_6A0(): pass

    label("Function_5_6A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_6CA")

    OP_6D(-34830, 1000, 170380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -35500, 1000, 180520, 180)
    SetChrPos(0x103, -34500, 1000, 180520, 180)
    SetChrPos(0xF8, -35750, 1000, 181520, 180)
    SetChrPos(0xF9, -34250, 1000, 181520, 180)

    def lambda_751():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_751)
    Sleep(100)

    def lambda_771():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_771)
    Sleep(200)

    def lambda_791():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFDAE4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_791)
    Sleep(100)

    def lambda_7B1():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFDAE4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7B1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #6
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_7F0():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F0)
    Sleep(100)

    def lambda_810():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_810)
    Sleep(200)

    def lambda_830():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_830)
    Sleep(100)

    def lambda_850():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_850)

    def lambda_86B():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86B)

    def lambda_883():
        OP_6B(3370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_883)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 245, 400)
    Sleep(30)
    OP_8C(0xF8, 155, 400)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(50)
    OP_8C(0x103, 245, 400)
    Sleep(30)
    OP_8C(0xF8, 245, 400)
    Sleep(50)
    OP_8C(0xF9, 155, 400)
    Sleep(300)
    OP_8C(0x101, 245, 400)
    Sleep(50)
    OP_8C(0x103, 180, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 0, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    Sleep(50)
    OP_8C(0x103, 0, 400)
    Sleep(30)
    OP_8C(0xF8, 180, 400)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    Sleep(300)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99F")

    ChrTalk(    #7
        0x107,
        (
            "#560F哇……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A68")

    label("loc_99F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D1")

    ChrTalk(    #8
        0x106,
        (
            "#051F嘿……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A68")

    label("loc_9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A05")

    ChrTalk(    #9
        0x104,
        (
            "#030F嗯……\x01",
            "一下子就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A68")

    label("loc_A05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A39")

    ChrTalk(    #10
        0x105,
        (
            "#048F呵呵……\x01",
            "忽然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A68")

    label("loc_A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")

    ChrTalk(    #11
        0x108,
        (
            "#070F呼……\x01",
            "突然就明朗了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(    #12
        0x107,
        (
            "#061F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE0")

    ChrTalk(    #13
        0x106,
        (
            "#051F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C")

    ChrTalk(    #14
        0x104,
        (
            "#030F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_B1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #15
        0x105,
        (
            "#048F雾的覆盖范围\x01",
            "似乎就到这里为止呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B91")

    label("loc_B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B91")

    ChrTalk(    #16
        0x108,
        (
            "#070F雾的覆盖范围\x01",
            "似乎就到这里为止啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B91")


    ChrTalk(    #17
        0x103,
        (
            "#026F艾利兹街道，距离洛连特\x01",
            "大约６０塞尔矩的地点……\x02\x03",

            "#020F雾的范围内也没有魔兽，\x01",
            "应该可以确保安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "接下来去调查\x01",
            "其他地方吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x180E)
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_6A0 end

    def Function_6_C3E(): pass

    label("Function_6_C3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C68")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_C68")

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -35500, 1000, 172520, 180)
    SetChrPos(0x103, -34500, 1000, 172520, 180)
    SetChrPos(0xF8, -35750, 1000, 173520, 180)
    SetChrPos(0xF9, -34250, 1000, 173520, 180)

    def lambda_CEF():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEF)
    Sleep(100)

    def lambda_D0F():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D0F)
    Sleep(200)

    def lambda_D2F():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D2F)
    Sleep(100)

    def lambda_D4F():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D4F)

    def lambda_D6A():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D6A)
    FadeToBright(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC4")

    ChrTalk(    #19
        0x107,
        "#061F嘿嘿，已经晴了⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEF")

    ChrTalk(    #20
        0x106,
        "#051F嘿，已经晴了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1E")

    ChrTalk(    #21
        0x104,
        "#030F嗯，好像已经晴了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4D")

    ChrTalk(    #22
        0x105,
        "#048F……似乎已经晴了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(    #23
        0x108,
        "#070F嗯……已经没有雾了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_E7B")


    ChrTalk(    #24
        0x103,
        (
            "#026F艾利兹街道，距离洛连特\x01",
            "大约６０塞尔矩的地点吗……\x02\x03",

            "#020F在有雾的范围内没有魔兽，\x01",
            "应该可以确保安全。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇调查过玛鲁加山道】\x01",      # 0
            "【◇调查过米尔西街道】\x01",      # 1
            "【◇不变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F73"),
        (1, "loc_F7C"),
        (SWITCH_DEFAULT, "loc_F85"),
    )


    label("loc_F73")

    OP_A3(0x180F)
    OP_A2(0x1810)
    Jump("loc_F85")

    label("loc_F7C")

    OP_A2(0x180F)
    OP_A3(0x1810)
    Jump("loc_F85")

    label("loc_F85")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(    #25
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "这样的话，\x01",
            "只剩下米尔西街道了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1008")

    label("loc_FCF")


    ChrTalk(    #26
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "这样的话，\x01",
            "只剩下玛鲁加山道了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1008")

    OP_A2(0x180E)
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_6_C3E end

    def Function_7_101A(): pass

    label("Function_7_101A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1044")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_1044")

    OP_6D(-35370, 1000, 172190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -35500, 1000, 172520, 180)
    SetChrPos(0x103, -34500, 1000, 172520, 180)
    SetChrPos(0xF8, -35750, 1000, 173520, 180)
    SetChrPos(0xF9, -34250, 1000, 173520, 180)

    def lambda_10CB():
        OP_8E(0xFE, 0xFFFF741E, 0x3E8, 0x27C9A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CB)
    Sleep(100)

    def lambda_10EB():
        OP_8E(0xFE, 0xFFFF7914, 0x3E8, 0x27C0E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10EB)
    Sleep(200)

    def lambda_110B():
        OP_8E(0xFE, 0xFFFF73F6, 0x3E8, 0x282A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_110B)
    Sleep(100)

    def lambda_112B():
        OP_8E(0xFE, 0xFFFF79B4, 0x3E8, 0x282DA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_112B)

    def lambda_1146():
        OP_6D(-34940, 1000, 163860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1146)
    FadeToBright(1000, 0)
    OP_6B(3370, 3000)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #27
        0x107,
        "#061F嘿嘿，已经晴了⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_1257")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CB")

    ChrTalk(    #28
        0x106,
        "#051F嘿，已经晴了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1257")

    label("loc_11CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(    #29
        0x104,
        "#030F嗯，好像已经晴了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1257")

    label("loc_11FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(    #30
        0x105,
        "#048F……似乎已经晴了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1257")

    label("loc_1229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1257")

    ChrTalk(    #31
        0x108,
        "#070F嗯……已经没有雾了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_1257")


    ChrTalk(    #32
        0x103,
        (
            "#026F艾利兹街道……从洛连特出发\x01",
            "大概６０塞尔矩的地点吗……\x02\x03",

            "#020F雾的范围内也没有魔兽，\x01",
            "应该可以确保安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "这样的话，三个地方\x01",
            "都调查过了…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #34
        0x101,
        (
            "#1006F我们应该回协会\x01",
            "向爱娜姐报告了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C2")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没去过布莱特家】\x01",      # 0
            "【◇去过布莱特家】\x01",        # 1
            "【◇不变更】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13B6"),
        (1, "loc_13BC"),
        (SWITCH_DEFAULT, "loc_13C2"),
    )


    label("loc_13B6")

    OP_A3(0x180D)
    Jump("loc_13C2")

    label("loc_13BC")

    OP_A2(0x180D)
    Jump("loc_13C2")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1466")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #35
        0x103,
        (
            "#023F#2P那样也好……\x02\x03",

            "不过你好像\x01",
            "还没回家看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1004F啊……都给忘了。\x02\x03",

            "#1008F回协会报告之前\x01",
            "先回去看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    Jump("loc_14A2")

    label("loc_1466")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #37
        0x103,
        (
            "#021F#2P嗯。\x01",
            "那样也好。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x4)
    OP_28(0x8F, 0x1, 0x8)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)

    label("loc_14A2")

    OP_A2(0x180E)
    EventEnd(0x0)
    Return()

    # Function_7_101A end

    def Function_8_14A8(): pass

    label("Function_8_14A8")

    EventBegin(0x1)

    ChrTalk(    #38
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_14D4():
        OP_6D(-93210, 980, 76900, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_14D4)

    def lambda_14EC():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_14EC)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161B")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x6, 0xFFFE9B70, 0x3CA, 0x13312, 0xE1, 0xFFFE8BF8, 0x41A, 0x128E0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_1615")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160C")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x10)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05将在艾利兹街道发现钓鱼场的事情\x01",
            "记录在游击士手册上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_160C")

    Jump("loc_1615")

    label("loc_160F")

    OP_28(0x73, 0x1, 0x1000)

    label("loc_1615")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_162A")

    label("loc_161B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_162A")
    EventEnd(0x1)

    label("loc_162A")

    Return()

    # Function_8_14A8 end

    def Function_9_162B(): pass

    label("Function_9_162B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_16A8"),
        (1, "loc_16AE"),
        (SWITCH_DEFAULT, "loc_16B4"),
    )


    label("loc_16A8")

    OP_A2(0x1200)
    Jump("loc_16B4")

    label("loc_16AE")

    OP_A2(0x1201)
    Jump("loc_16B4")

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_16C2")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_16C6")

    label("loc_16C2")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_16C6")

    Return()

    # Function_9_162B end

    def Function_10_16C7(): pass

    label("Function_10_16C7")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_10_16C7 end

    SaveToFile()

Try(main)
