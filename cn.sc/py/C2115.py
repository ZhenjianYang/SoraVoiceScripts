from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2115   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = 3770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B9,
        Unknown_18          = 4953,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8230,
        TriggerZ            = 0,
        TriggerY            = 8330,
        TriggerRange        = 1000,
        ActorX              = -8730,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9350,
        TriggerZ            = 0,
        TriggerY            = 9330,
        TriggerRange        = 1000,
        ActorX              = 8850,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12530,
        TriggerZ            = 0,
        TriggerY            = -660,
        TriggerRange        = 1000,
        ActorX              = 12530,
        ActorZ              = 0,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12430,
        TriggerZ            = 0,
        TriggerY            = -640,
        TriggerRange        = 1000,
        ActorX              = -12400,
        ActorZ              = 0,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 0,
        TriggerY            = 22500,
        TriggerRange        = 1000,
        ActorX              = 4690,
        ActorZ              = 0,
        ActorY              = 23200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3680,
        TriggerZ            = 380,
        TriggerY            = 490,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = 380,
        ActorY              = 180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_1DF",          # 01, 1
        "Function_2_285",          # 02, 2
        "Function_3_39C",          # 03, 3
        "Function_4_4B3",          # 04, 4
        "Function_5_5CA",          # 05, 5
        "Function_6_6E1",          # 06, 6
        "Function_7_84B",          # 07, 7
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Return()

    # Function_0_1DE end

    def Function_1_1DF(): pass

    label("Function_1_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1")
    OP_6F(0x0, 0)
    Jump("loc_1F8")

    label("loc_1F1")

    OP_6F(0x0, 60)

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A")
    OP_6F(0x1, 0)
    Jump("loc_211")

    label("loc_20A")

    OP_6F(0x1, 60)

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223")
    OP_6F(0x2, 0)
    Jump("loc_22A")

    label("loc_223")

    OP_6F(0x2, 60)

    label("loc_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C")
    OP_6F(0x3, 0)
    Jump("loc_243")

    label("loc_23C")

    OP_6F(0x3, 60)

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255")
    OP_6F(0x4, 0)
    Jump("loc_25C")

    label("loc_255")

    OP_6F(0x4, 60)

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26B, 1)), scpexpr(EXPR_END)), "loc_268")
    SetChrFlags(0x8, 0x80)

    label("loc_268")

    SoundDistance(0x1CB, 0xFFFFFFA6, 0x0, 0x96, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_1DF end

    def Function_2_285(): pass

    label("Function_2_285")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x177, 1)"), scpexpr(EXPR_END)), "loc_2F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x77\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1316)
    Jump("loc_35A")

    label("loc_2F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x77\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x77\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_35A")

    Jump("loc_38E")

    label("loc_35D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_38E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_285 end

    def Function_3_39C(): pass

    label("Function_3_39C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x168, 1)"), scpexpr(EXPR_END)), "loc_40B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x68\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1318)
    Jump("loc_471")

    label("loc_40B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x68\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x68\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_471")

    Jump("loc_4A5")

    label("loc_474")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4A5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_39C end

    def Function_4_4B3(): pass

    label("Function_4_4B3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x133, 1)"), scpexpr(EXPR_END)), "loc_522")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x33\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131A)
    Jump("loc_588")

    label("loc_522")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x33\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x33\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_588")

    Jump("loc_5BC")

    label("loc_58B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4B3 end

    def Function_5_5CA(): pass

    label("Function_5_5CA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16, 1)"), scpexpr(EXPR_END)), "loc_639")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x16\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131C)
    Jump("loc_69F")

    label("loc_639")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x16\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x16\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_69F")

    Jump("loc_6D3")

    label("loc_6A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5CA end

    def Function_6_6E1(): pass

    label("Function_6_6E1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x263, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1EC, 1)"), scpexpr(EXPR_END)), "loc_750")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xEC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x131F)
    Jump("loc_7B6")

    label("loc_750")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xEC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xEC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_7B6")

    Jump("loc_7EA")

    label("loc_7B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7EA")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_842")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x28)"), scpexpr(EXPR_END)), "loc_809")
    Jump("loc_842")

    label("loc_809")


    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xEC\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #16
        "\x1F\xEC\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_842")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_6E1 end

    def Function_7_84B(): pass

    label("Function_7_84B")

    EventBegin(0x1)

    ChrTalk(    #17
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_877():
        OP_6D(-1110, 380, 470, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_877)

    def lambda_88F():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_88F)

    def lambda_8A7():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8A7)

    def lambda_8B7():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8B7)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #18
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0B")
    OP_C0(0xE, 0x1D, 0xFFFFF40C, 0x370, 0x1D6, 0x5A, 0xFFFFFC36, 0xFFFFFE0C, 0x262)
    Fade(500)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrChipByIndex(0x0, 65535)
    ClearChrFlags(0x0, 0x2)
    ClearChrFlags(0x0, 0x40)
    ClearChrFlags(0x0, 0x4)
    SetChrPos(0x0, -3760, 380, 160, 90)
    SetChrPos(0x1, -3760, 380, 160, 90)
    SetChrPos(0x2, -3760, 380, 160, 90)
    SetChrPos(0x3, -3760, 380, 160, 90)
    SetChrPos(0x4, -3760, 380, 160, 90)
    SetChrPos(0x5, -3760, 380, 160, 90)
    SetChrPos(0x6, -3760, 380, 160, 90)
    SetChrPos(0x7, -3760, 380, 160, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_A1A")

    label("loc_A0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1A")
    EventEnd(0x1)

    label("loc_A1A")

    Return()

    # Function_7_84B end

    SaveToFile()

Try(main)
