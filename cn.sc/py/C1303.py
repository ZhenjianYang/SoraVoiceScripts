from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1303   ._SN',
        MapName             = 'Bose',
        Location            = 'C1303.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        '守备队长',                             # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
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
        'ED6_DT07/CH01600 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT27/CH04010 ._CH',             # 02
        'ED6_DT27/CH04011 ._CH',             # 03
        'ED6_DT07/CH00291 ._CH',             # 04
        'ED6_DT07/CH00301 ._CH',             # 05
        'ED6_DT07/CH00311 ._CH',             # 06
        'ED6_DT26/CH20335 ._CH',             # 07
        'ED6_DT06/CH20043 ._CH',             # 08
        'ED6_DT27/CH03014 ._CH',             # 09
        'ED6_DT07/CH00330 ._CH',             # 0A
        'ED6_DT07/CH00320 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01600P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT27/CH04010P._CP',             # 02
        'ED6_DT27/CH04011P._CP',             # 03
        'ED6_DT07/CH00291P._CP',             # 04
        'ED6_DT07/CH00301P._CP',             # 05
        'ED6_DT07/CH00311P._CP',             # 06
        'ED6_DT26/CH20335P._CP',             # 07
        'ED6_DT06/CH20043P._CP',             # 08
        'ED6_DT27/CH03014P._CP',             # 09
        'ED6_DT07/CH00330P._CP',             # 0A
        'ED6_DT07/CH00320P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -75460,
        TriggerZ            = 0,
        TriggerY            = -119560,
        TriggerRange        = 1000,
        ActorX              = -75450,
        ActorZ              = 1500,
        ActorY              = -118890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18E",          # 00, 0
        "Function_1_22C",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_363",          # 03, 3
        "Function_4_7A6",          # 04, 4
        "Function_5_F62",          # 05, 5
        "Function_6_FD2",          # 06, 6
        "Function_7_1049",         # 07, 7
        "Function_8_10C0",         # 08, 8
        "Function_9_1137",         # 09, 9
        "Function_10_117F",        # 0A, 10
        "Function_11_11CE",        # 0B, 11
    )


    def Function_0_18E(): pass

    label("Function_0_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 1)), scpexpr(EXPR_END)), "loc_213")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -39500, 0, -87480, 0)
    SetChrPos(0x9, -41000, 0, -87420, 0)
    SetChrPos(0xA, -40800, 0, -89040, 0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0xA, 7)
    SetChrChipByIndex(0xA, 8)

    label("loc_213")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B")
    Event(0, 3)

    label("loc_22B")

    Return()

    # Function_0_18E end

    def Function_1_22C(): pass

    label("Function_1_22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E")
    OP_6F(0x2, 0)
    Jump("loc_245")

    label("loc_23E")

    OP_6F(0x2, 60)

    label("loc_245")

    OP_10(0x3, 0x0)
    OP_10(0x8, 0x1)
    Return()

    # Function_1_22C end

    def Function_2_24C(): pass

    label("Function_2_24C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x260, 1)"), scpexpr(EXPR_END)), "loc_2BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x60\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1900)
    Jump("loc_321")

    label("loc_2BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x60\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x60\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_321")

    Jump("loc_355")

    label("loc_324")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_355")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_24C end

    def Function_3_363(): pass

    label("Function_3_363")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-34720, 0, -86660, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2230, 0)
    OP_6C(45000, 0)
    OP_6E(355, 0)
    OP_0D()
    OP_43(0x129, 0x1, 0x0, 0x5)
    Sleep(700)
    OP_43(0x12A, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x8)

    def lambda_3E8():
        OP_6D(-36060, 0, -82580, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E8)
    WaitChrThread(0x146, 0x1)
    WaitChrThread(0x146, 0x0)

    ChrTalk(    #3
        0x129,
        (
            "#197F#5P这里是……\x01",
            "我们之前用过的房间呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12A, 0, 400)

    ChrTalk(    #4
        0x12A,
        (
            "#200F#2P哦……\x01",
            "装设了通信器啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x146,
        (
            "#210F#6P里面没人……\x01",
            "有点太粗心大意了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1030F看来这里似乎是\x01",
            "守备队长的房间。\x02\x03",

            "只要埋伏在这里的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x102,
        "#1035F……回来了。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 2)
    OP_0D()
    Sleep(300)
    OP_8C(0x102, 180, 600)

    ChrTalk(    #8
        0x102,
        "#1030F#5P趁他们进来时一次解决。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x146,
        "#213F#6P啊啊……\x02",
    )

    CloseMessageWindow()

    def lambda_567():
        OP_8C(0x146, 180, 400)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_567)

    def lambda_575():
        OP_6D(-34550, 0, -85660, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_575)

    def lambda_58D():
        OP_8C(0x129, 180, 400)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_58D)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_5A5():
        OP_8C(0x12A, 180, 400)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_5A5)
    Sleep(100)
    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0xB)
    WaitChrThread(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x8,
        "#5P什…么…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        "#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1031F#5P……太慢了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x146, 0x1000)
    SetChrFlags(0x12A, 0x1000)
    SetChrFlags(0x129, 0x1000)
    SetChrChipByIndex(0x102, 3)

    def lambda_684():
        OP_8F(0xFE, 0xFFFF7694, 0x0, 0xFFFEA728, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_684)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 6)

    def lambda_6B3():
        OP_8F(0xFE, 0xFFFF7310, 0x0, 0xFFFEA9EE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_6B3)
    Sleep(100)
    SetChrSubChip(0x12A, 0)
    SetChrChipByIndex(0x12A, 5)

    def lambda_6DD():
        OP_8F(0xFE, 0xFFFF75F4, 0x0, 0xFFFEAD0E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_6DD)
    Sleep(50)
    SetChrSubChip(0x129, 0)
    SetChrChipByIndex(0x129, 4)

    def lambda_707():
        OP_8F(0xFE, 0xFFFF72FC, 0x0, 0xFFFEAE12, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_707)

    def lambda_722():
        OP_6D(-34680, 0, -87920, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_722)

    def lambda_73A():
        OP_6B(1960, 300)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_73A)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 11)
    Sleep(300)
    OP_44(0x102, 0xFF)
    OP_44(0x146, 0xFF)
    OP_44(0x12A, 0xFF)
    OP_44(0x129, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0xA5, 0x0, 0x2, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_79C"),
        (SWITCH_DEFAULT, "loc_7A1"),
    )


    label("loc_79C")

    OP_B4(0x0)
    Jump("loc_7A1")

    label("loc_7A1")

    Call(0, 4)
    Return()

    # Function_3_363 end

    def Function_4_7A6(): pass

    label("Function_4_7A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x146, 0x1000)
    ClearChrFlags(0x12A, 0x1000)
    ClearChrFlags(0x129, 0x1000)
    OP_44(0x102, 0x1)
    OP_44(0x146, 0x1)
    OP_44(0x12A, 0x1)
    OP_44(0x129, 0x1)
    SetChrPos(0x102, -38290, 0, -86890, 270)
    SetChrPos(0x129, -36820, 0, -86670, 270)
    SetChrPos(0x146, -37870, 0, -85820, 225)
    SetChrPos(0x12A, -37800, 0, -87800, 270)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x129, 0)
    SetChrChipByIndex(0x129, 65535)
    SetChrSubChip(0x12A, 0)
    SetChrChipByIndex(0x12A, 65535)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 65535)
    SetChrPos(0x8, -39500, 0, -87480, 0)
    SetChrPos(0x9, -41000, 0, -87420, 0)
    SetChrPos(0xA, -40800, 0, -89040, 0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0xA, 7)
    SetChrChipByIndex(0xA, 8)
    OP_6D(-37800, 0, -86880, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x102,
        "#1035F#6P有了……就是这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xF6\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F6, 1)
    Fade(500)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()

    def lambda_990():
        OP_6D(-37210, 0, -86660, 1000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_990)
    OP_8C(0x102, 90, 400)
    OP_8C(0x146, 180, 400)
    OP_8C(0x12A, 0, 400)
    WaitChrThread(0x102, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没看见确认空贼艇的事件】\x01",      # 0
            "【◇看见了确认空贼艇的事件】\x01",      # 1
            "【◇不变更】\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A52"),
        (1, "loc_A58"),
        (SWITCH_DEFAULT, "loc_A5E"),
    )


    label("loc_A52")

    OP_A3(0x1804)
    Jump("loc_A5E")

    label("loc_A58")

    OP_A2(0x1804)
    Jump("loc_A5E")

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8F")

    ChrTalk(    #15
        0x129,
        "#191F#2P哦哦，这么快就找到了啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAD")

    label("loc_A8F")


    ChrTalk(    #16
        0x129,
        "#191F#2P好，终于找到了！\x02",
    )

    CloseMessageWindow()

    label("loc_AAD")


    ChrTalk(    #17
        0x12A,
        (
            "#203F真，真是让人\x01",
            "吓出一身冷汗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x146, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x146)

    ChrTalk(    #18
        0x146,
        (
            "#212F#5P……对了，约修亚。\x02\x03",

            "以前和我们对战的时候，\x01",
            "难道你手下留情了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1034F#6P？什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x146,
        (
            "#214F#5P因为你实在\x01",
            "强得一塌糊涂啊。\x02\x03",

            "说实话，那时候\x01",
            "和现在根本不能相提并论啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1031F#6P我并没有手下留情。\x02\x03",

            "只是当时『开关』\x01",
            "还没打开而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x146,
        "#213F#5P开关？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1035F#6P详细说明就免了……\x02\x03",

            "总之这个开关打开的话，\x01",
            "我就能将合理的思考和行动\x01",
            "发挥到极限。\x02\x03",

            "只有这点差别而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x146,
        (
            "#215F#5P嗯、嗯～……\x01",
            "好像听懂了，又好像没懂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12A,
        (
            "#200F力量并没有改变……\x02\x03",

            "只是能将这些力量\x01",
            "更加彻底有效地发挥出来，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1031F#6P这么理解也没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x129,
        (
            "#490F#2P哦，真不得了。\x02\x03",

            "现在的你，应该和那特务兵\x01",
            "队长也不相上下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12A,
        (
            "#206F说是『结社』手下\x01",
            "的那个洛伦斯少尉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1033F#6P不……这点办不到。\x02\x03",

            "我的能力是针对隐密活动和\x01",
            "对集团作战而特别强化过的。\x02\x03",

            "在一对一的战斗中，\x01",
            "是不可能胜过『剑帝』的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x129,
        "#192F#2P『剑帝』……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x146,
        "#213F#5P这是说那个少尉？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1035F#6P啊啊……\x02\x03",

            "#1032F只要有他在，我绝对\x01",
            "不会正面向『结社』挑战。\x02\x03",

            "正如『漆黑之牙』这名号……\x01",
            "只会在黑暗中露出利齿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x146,
        "#216F#5P……啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x129,
        "#199F#2P你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12A,
        (
            "#206F怎么说呢……\x01",
            "好深奥的话啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1033F#6P……尽说了些无聊话。\x02\x03",

            "#1035F没时间了，赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1801)
    EventEnd(0x0)
    Return()

    # Function_4_7A6 end

    def Function_5_F62(): pass

    label("Function_5_F62")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_F89():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F89)
    OP_8E(0xFE, 0xFFFF78B0, 0x0, 0xFFFEAD7C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7216, 0x0, 0xFFFEB48E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7194, 0x0, 0xFFFEBE98, 0xBB8, 0x0)
    Return()

    # Function_5_F62 end

    def Function_6_FD2(): pass

    label("Function_6_FD2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_FF9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF9)
    OP_8E(0xFE, 0xFFFF766C, 0x0, 0xFFFEA9BC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF6DB6, 0x0, 0xFFFEB164, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF6CBC, 0x0, 0xFFFEB9E8, 0xBB8, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_6_FD2 end

    def Function_7_1049(): pass

    label("Function_7_1049")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1070():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1070)
    OP_8E(0xFE, 0xFFFF77D4, 0x0, 0xFFFEAC50, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF74AA, 0x0, 0xFFFEB204, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF74AA, 0x0, 0xFFFEBBC8, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_1049 end

    def Function_8_10C0(): pass

    label("Function_8_10C0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_10E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10E7)
    OP_8E(0xFE, 0xFFFF7798, 0x0, 0xFFFEA8D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7194, 0x0, 0xFFFEB07E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7162, 0x0, 0xFFFEB628, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_10C0 end

    def Function_9_1137(): pass

    label("Function_9_1137")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_115E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_115E)
    OP_8E(0xFE, 0xFFFF77AC, 0x0, 0xFFFEA624, 0xBB8, 0x0)
    Return()

    # Function_9_1137 end

    def Function_10_117F(): pass

    label("Function_10_117F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_11A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11A6)
    OP_8E(0xFE, 0xFFFF7496, 0x0, 0xFFFEA1D8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_117F end

    def Function_11_11CE(): pass

    label("Function_11_11CE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -35000, 0, -90980, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_11F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11F5)
    OP_8E(0xFE, 0xFFFF79BE, 0x0, 0xFFFEA1D8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_11CE end

    SaveToFile()

Try(main)
