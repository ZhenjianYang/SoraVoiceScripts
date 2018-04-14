from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        'ED6_DT29/CH12590 ._CH',             # 00
        'ED6_DT29/CH12591 ._CH',             # 01
        'ED6_DT29/CH12600 ._CH',             # 02
        'ED6_DT29/CH12601 ._CH',             # 03
        'ED6_DT29/CH12610 ._CH',             # 04
        'ED6_DT29/CH12611 ._CH',             # 05
        'ED6_DT29/CH12620 ._CH',             # 06
        'ED6_DT29/CH12621 ._CH',             # 07
        'ED6_DT29/CH12630 ._CH',             # 08
        'ED6_DT29/CH12631 ._CH',             # 09
        'ED6_DT29/CH12640 ._CH',             # 0A
        'ED6_DT29/CH12641 ._CH',             # 0B
        'ED6_DT29/CH12650 ._CH',             # 0C
        'ED6_DT29/CH12651 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12590P._CP',             # 00
        'ED6_DT29/CH12591P._CP',             # 01
        'ED6_DT29/CH12600P._CP',             # 02
        'ED6_DT29/CH12601P._CP',             # 03
        'ED6_DT29/CH12610P._CP',             # 04
        'ED6_DT29/CH12611P._CP',             # 05
        'ED6_DT29/CH12620P._CP',             # 06
        'ED6_DT29/CH12621P._CP',             # 07
        'ED6_DT29/CH12630P._CP',             # 08
        'ED6_DT29/CH12631P._CP',             # 09
        'ED6_DT29/CH12640P._CP',             # 0A
        'ED6_DT29/CH12641P._CP',             # 0B
        'ED6_DT29/CH12650P._CP',             # 0C
        'ED6_DT29/CH12651P._CP',             # 0D
    )

    DeclMonster(
        X                   = -7290,
        Z                   = -7200,
        Y                   = -490,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8128,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7690,
        Z                   = -7200,
        Y                   = 490,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8129,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -20,
        TriggerZ            = -7650,
        TriggerY            = -650,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -7650,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_176",          # 00, 0
        "Function_1_1A4",          # 01, 1
        "Function_2_1E0",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_83D",          # 04, 4
        "Function_5_8A8",          # 05, 5
        "Function_6_913",          # 06, 6
        "Function_7_97E",          # 07, 7
        "Function_8_9E9",          # 08, 8
        "Function_9_A70",          # 09, 9
        "Function_10_AFF",         # 0A, 10
        "Function_11_CDE",         # 0B, 11
        "Function_12_DCD",         # 0C, 12
        "Function_13_E52",         # 0D, 13
        "Function_14_ED7",         # 0E, 14
        "Function_15_F5C",         # 0F, 15
        "Function_16_FE1",         # 10, 16
        "Function_17_10DC",        # 11, 17
        "Function_18_113A",        # 12, 18
        "Function_19_122D",        # 13, 19
        "Function_20_1320",        # 14, 20
        "Function_21_136E",        # 15, 21
    )


    def Function_0_176(): pass

    label("Function_0_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185")
    Event(0, 3)
    Jump("loc_1A3")

    label("loc_185")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_195"),
        (101, "loc_19C"),
        (SWITCH_DEFAULT, "loc_1A3"),
    )


    label("loc_195")

    Event(0, 10)
    Jump("loc_1A3")

    label("loc_19C")

    Event(0, 16)
    Jump("loc_1A3")

    label("loc_1A3")

    Return()

    # Function_0_176 end

    def Function_1_1A4(): pass

    label("Function_1_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6")
    OP_6F(0x1, 0)
    Jump("loc_1BD")

    label("loc_1B6")

    OP_6F(0x1, 60)

    label("loc_1BD")

    OP_1B(0x0, 0x0, 0xB)
    OP_1B(0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 0)), scpexpr(EXPR_END)), "loc_1D3")
    SetChrFlags(0x8, 0x80)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F8, 1)), scpexpr(EXPR_END)), "loc_1DF")
    SetChrFlags(0x9, 0x80)

    label("loc_1DF")

    Return()

    # Function_1_1A4 end

    def Function_2_1E0(): pass

    label("Function_2_1E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_24F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F00)
    Jump("loc_2B5")

    label("loc_24F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_2B5")

    Jump("loc_2E9")

    label("loc_2B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1E0 end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30E")
    Call(0, 8)
    Call(0, 9)

    label("loc_30E")

    OP_6D(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(800)

    def lambda_408():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_408)
    OP_43(0x102, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    Sleep(600)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#1004F#5P咦……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x0)

    ChrTalk(    #4
        0x102,
        "#1044F#2P这里是……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x1, 0x3E8)
    OP_6D(3520, 11180, 56940, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)

    def lambda_4E6():
        OP_6D(-170, 600, -78050, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E6)

    def lambda_4FE():
        OP_67(0, 7500, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FE)

    def lambda_516():
        OP_6B(3000, 15000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_516)

    def lambda_526():
        OP_6C(315000, 15000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_526)

    def lambda_536():
        OP_6E(262, 15000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_536)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#1020F#5P等、等一下……\x02\x03",

            "我们，确实\x01",
            "应该进入了塔中吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DB")

    ChrTalk(    #6
        0x109,
        (
            "#1065F#6P空间转移……\x02\x03",

            "#1063F看来是被传送到\x01",
            "其它的地方去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719")

    label("loc_5DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B")

    ChrTalk(    #7
        0x107,
        (
            "#065F#6P空、空间转移……\x02\x03",

            "可能是被传送到\x01",
            "其它的地方了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719")

    label("loc_62B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67E")

    ChrTalk(    #8
        0x105,
        (
            "#047F#6P空间转移……\x02\x03",

            "#042F说不定是被传送到\x01",
            "其它的地方去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719")

    label("loc_67E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CD")

    ChrTalk(    #9
        0x108,
        (
            "#074F#6P空间转移……\x02\x03",

            "#072F好像被传送到\x01",
            "其它的地方了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719")

    label("loc_6CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_719")

    ChrTalk(    #10
        0x103,
        (
            "#026F#6P空间转移……\x02\x03",

            "#022F好像被传送到\x01",
            "其它的地方了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_719")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x101, 180, 600)

    ChrTalk(    #11
        0x101,
        (
            "#1019F#2P你、你说什么～！？\x02\x03",

            "#1020F那、那么要爬上塔顶\x01",
            "就不可能了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #12
        0x102,
        (
            "#1035F冷静点，艾丝蒂尔。\x02\x03",

            "#1040F既然会有布卢布兰出现\x01",
            "这就表明必然有路可走。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #13
        0x101,
        (
            "#1007F#4P确、确实……\x02\x03",

            "#1002F……嗯！\x01",
            "总之慎重前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E05)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_2F7 end

    def Function_4_83D(): pass

    label("Function_4_83D")


    def lambda_843():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_843)

    def lambda_85D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85D)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_888():
        OP_8F(0xFE, 0x262, 0x258, 0xFFFECFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_888)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_83D end

    def Function_5_8A8(): pass

    label("Function_5_8A8")


    def lambda_8AE():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AE)

    def lambda_8C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C8)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_8F3():
        OP_8F(0xFE, 0xFFFFFE2A, 0x258, 0xFFFECEF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8F3)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_8A8 end

    def Function_6_913(): pass

    label("Function_6_913")


    def lambda_919():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_919)

    def lambda_933():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_933)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_95E():
        OP_8F(0xFE, 0x276, 0x2EE, 0xFFFECA32, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_95E)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_913 end

    def Function_7_97E(): pass

    label("Function_7_97E")


    def lambda_984():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_984)

    def lambda_99E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99E)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_9C9():
        OP_8F(0xFE, 0xFFFFFDE4, 0x2EE, 0xFFFECA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9C9)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_97E end

    def Function_8_9E9(): pass

    label("Function_8_9E9")

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
        (0, "loc_A63"),
        (1, "loc_A69"),
        (SWITCH_DEFAULT, "loc_A6F"),
    )


    label("loc_A63")

    OP_A2(0x1200)
    Jump("loc_A6F")

    label("loc_A69")

    OP_A2(0x1201)
    Jump("loc_A6F")

    label("loc_A6F")

    Return()

    # Function_8_9E9 end

    def Function_9_A70(): pass

    label("Function_9_A70")

    FadeToDark(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_A70 end

    def Function_10_AFF(): pass

    label("Function_10_AFF")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(800)

    def lambda_C0F():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C0F)
    OP_43(0x102, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 610, 600, -77870, 0)
    SetChrPos(0x1, 610, 600, -77870, 0)
    SetChrPos(0x2, 610, 600, -77870, 0)
    SetChrPos(0x3, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_AFF end

    def Function_11_CDE(): pass

    label("Function_11_CDE")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-600, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(219000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 680, 700, -81310, 180)
    SetChrPos(0x102, -330, 700, -81100, 180)
    SetChrPos(0xF8, 910, 750, -79600, 180)
    SetChrPos(0xF9, -270, 750, -79450, 180)
    OP_43(0x101, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xD)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xE)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R0303   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_11_CDE end

    def Function_12_DCD(): pass

    label("Function_12_DCD")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_E12():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E12)

    def lambda_E2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E2C)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_DCD end

    def Function_13_E52(): pass

    label("Function_13_E52")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_E97():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E97)

    def lambda_EB1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EB1)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_E52 end

    def Function_14_ED7(): pass

    label("Function_14_ED7")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F1C():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F1C)

    def lambda_F36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F36)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_14_ED7 end

    def Function_15_F5C(): pass

    label("Function_15_F5C")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_FA1():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA1)

    def lambda_FBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FBB)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_15_F5C end

    def Function_16_FE1(): pass

    label("Function_16_FE1")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -50, 84460, 0)
    SetChrPos(0x101, 500, -50, 83960, 180)
    SetChrPos(0x102, -500, -50, 83960, 180)
    SetChrPos(0xF8, 500, -50, 84960, 180)
    SetChrPos(0xF9, -500, -50, 84960, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 19)
    Call(0, 20)
    Fade(500)
    OP_6D(80, 260, 81830, 0)
    SetChrPos(0x0, 80, 260, 81830, 180)
    SetChrPos(0x1, 80, 260, 81830, 180)
    SetChrPos(0x2, 80, 260, 81830, 180)
    SetChrPos(0x3, 80, 260, 81830, 180)
    EventEnd(0x0)
    Return()

    # Function_16_FE1 end

    def Function_17_10DC(): pass

    label("Function_17_10DC")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -500, -50, 84960, 0)
    SetChrPos(0x102, 500, -50, 84960, 0)
    SetChrPos(0xF8, -500, -50, 83960, 0)
    SetChrPos(0xF9, 500, -50, 83960, 0)
    OP_0D()
    Call(0, 19)
    Call(0, 21)
    NewScene("ED6_DT21/C0701   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_10DC end

    def Function_18_113A(): pass

    label("Function_18_113A")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_18_113A end

    def Function_19_122D(): pass

    label("Function_19_122D")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_19_122D end

    def Function_20_1320(): pass

    label("Function_20_1320")


    def lambda_1326():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1326)

    def lambda_1338():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1338)

    def lambda_134A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_134A)

    def lambda_135C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_135C)
    Sleep(2500)
    Return()

    # Function_20_1320 end

    def Function_21_136E(): pass

    label("Function_21_136E")


    def lambda_1374():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1374)

    def lambda_1386():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1386)

    def lambda_1398():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1398)

    def lambda_13AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13AA)
    Sleep(2000)
    Return()

    # Function_21_136E end

    SaveToFile()

Try(main)
