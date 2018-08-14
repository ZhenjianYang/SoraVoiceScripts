from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7306   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7306.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        '女性亡灵',                             # 9
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
        'ED6_DT29/CH15180 ._CH',             # 00
        'ED6_DT29/CH15181 ._CH',             # 01
        'ED6_DT26/CH20724 ._CH',             # 02
        'ED6_DT29/CH14440 ._CH',             # 03
        'ED6_DT29/CH14440 ._CH',             # 04
        'ED6_DT29/CH14140 ._CH',             # 05
        'ED6_DT29/CH14140 ._CH',             # 06
        'ED6_DT29/CH14150 ._CH',             # 07
        'ED6_DT29/CH14150 ._CH',             # 08
        'ED6_DT29/CH14090 ._CH',             # 09
        'ED6_DT29/CH14090 ._CH',             # 0A
        'ED6_DT29/CH14120 ._CH',             # 0B
        'ED6_DT29/CH14120 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT29/CH15180P._CP',             # 00
        'ED6_DT29/CH15181P._CP',             # 01
        'ED6_DT26/CH20724P._CP',             # 02
        'ED6_DT29/CH14440P._CP',             # 03
        'ED6_DT29/CH14440P._CP',             # 04
        'ED6_DT29/CH14140P._CP',             # 05
        'ED6_DT29/CH14140P._CP',             # 06
        'ED6_DT29/CH14150P._CP',             # 07
        'ED6_DT29/CH14150P._CP',             # 08
        'ED6_DT29/CH14090P._CP',             # 09
        'ED6_DT29/CH14090P._CP',             # 0A
        'ED6_DT29/CH14120P._CP',             # 0B
        'ED6_DT29/CH14120P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -21070,
        Z                   = 12430,
        Y                   = 43920,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9540,
        Z                   = 12430,
        Y                   = 56180,
        Unknown_0C          = 180,
        Unknown_0E          = 11,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10440,
        Z                   = 18150,
        Y                   = 78170,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2410,
        Z                   = 21230,
        Y                   = 98750,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18070,
        Z                   = 16030,
        Y                   = 77200,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -4800,
        Y                   = 4000,
        Z                   = 10010,
        Range               = 4820,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x303E,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -19970,
        TriggerZ            = 16050,
        TriggerY            = 76750,
        TriggerRange        = 1000,
        ActorX              = -19970,
        ActorZ              = 17050,
        ActorY              = 76750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_203",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_396",          # 03, 3
        "Function_4_DFB",          # 04, 4
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Return()

    # Function_0_202 end

    def Function_1_203(): pass

    label("Function_1_203")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFEF660, 0x230099)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268")
    OP_6F(0x0, 0)
    Jump("loc_26F")

    label("loc_268")

    OP_6F(0x0, 60)

    label("loc_26F")

    Return()

    # Function_1_203 end

    def Function_2_270(): pass

    label("Function_2_270")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_2E4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_2C9")

    label("loc_2C9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6E)
    Jump("loc_352")

    label("loc_2E4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_333")

    label("loc_333")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_352")

    Jump("loc_388")

    label("loc_355")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_388")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_270 end

    def Function_3_396(): pass

    label("Function_3_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 6)), scpexpr(EXPR_END)), "loc_39E")
    Return()

    label("loc_39E")

    EventBegin(0x0)
    OP_D2(0x270176, 0x270183, 0xD)
    OP_D2(0x270177, 0x270184, 0xE)
    OP_D2(0x270178, 0x270185, 0xF)
    OP_D2(0x27058C, 0x270590, 0x10)
    OP_D2(0x27058D, 0x270591, 0x11)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 10, 7030, 23760, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F9():

        label("loc_3F9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3F9")

    QueueWorkItem2(0x10, 3, lambda_3F9)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x07#80W………对不起啊…………\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4AC():
        OP_6D(-1090, 7030, 24840, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4AC)

    def lambda_4C4():
        OP_67(0, 5210, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4C4)

    def lambda_4DC():
        OP_6B(2560, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4DC)

    def lambda_4EC():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4EC)

    def lambda_4FC():
        OP_6E(335, 3500)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_4FC)

    def lambda_50C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_50C)
    Sleep(100)
    OP_8C(0x1, 0, 400)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x1D9, 0x0, 0x64)
    Fade(1000)

    def lambda_535():
        OP_6B(2300, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_535)

    def lambda_545():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_545)

    def lambda_555():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_555)
    OP_22(0x1E0, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    OP_23(0x1D9)
    Sleep(1000)
    SetChrPos(0x109, 1100, 6430, 12160, 0)
    SetChrPos(0x10F, -670, 6750, 12870, 0)

    def lambda_5A6():
        OP_6D(-1940, 7030, 22150, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5A6)

    def lambda_5BE():
        OP_67(0, 5330, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5BE)

    def lambda_5D6():
        OP_6B(2640, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5D6)

    def lambda_5E6():
        OP_6E(335, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5E6)

    def lambda_5F6():
        OP_8E(0xFE, 0x12C, 0x1B76, 0x42E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5F6)
    Sleep(1000)

    def lambda_616():
        OP_8E(0xFE, 0xFFFFFB6E, 0x1B76, 0x4290, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_616)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x07#80W……对不起……凯文………\x01",
            "#3040W \x01",
            "#80W……但是……妈妈我………#2800W \x01",
            "#80W已经……精疲力尽了………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #5
        0x109,
        "#1847F#6P…………啊…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        "#1949F#6P难、难道是……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x07#80W………所以…………#500W\x01",
            "#80W…………所以…我说……凯文…………\x01",
            "#4158W \x01",
            "#80W……就这样………#1930W \x01",
            "#80W………和妈妈#160W一起…………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 13)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 16)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    def lambda_855():
        OP_6D(-1980, 7030, 19170, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_855)

    def lambda_86D():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_86D)

    def lambda_885():
        OP_6B(2100, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_885)

    def lambda_895():
        OP_6E(300, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_895)
    SetChrChipByIndex(0x10, 1)

    def lambda_8AA():
        OP_8F(0xFE, 0xFFFFFE02, 0x1B76, 0x43EE, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8AA)
    WaitChrThread(0xEE, 0x1)
    Battle(0x2CE, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x109, -40, 7030, 20850, 0)
    SetChrPos(0x10F, 80, 7030, 19060, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-990, 7030, 18930, 0)
    OP_67(0, 6350, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(219000, 0)
    OP_6E(284, 0)
    Sleep(500)

    def lambda_971():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_971)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x3)
    Sleep(500)

    ChrTalk(    #8
        0x109,
        (
            "#1076F#6P#40W……………………………………\x02\x03",

            "#1844F……哈哈………\x01",
            "还是饶了我吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1950F#5P#40W凯文……够了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1071F#6P这个『炼狱』……\x01",
            "假如真的是我所希望的话……\x02\x03",

            "那我就是一个……\x01",
            "十足的自虐狂啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #11
        0x10F,
        (
            "#1954F#5P#3S够了……！\x01",
            "这个时候，什么也不要说就行了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0x109,
        "#1076F#6P#40W…………抱歉…………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_B24():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_B24)
    Fade(250)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_44(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #13
        0x109,
        (
            "#1065F#6P#40W……在某种意义上，\x01",
            "会遇到刚才那幅情景可以说是必然的。\x02\x03",

            "自从那个冬日以来……\x01",
            "我一直在不断\x01",
            "逃避着妈妈的死亡……\x02\x03",

            "这次……\x01",
            "……我终于能够面对这个现实了。\x02",
        )
    )

    Jump("loc_C3B")

    label("loc_C3B")

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        "#1955F#5P#40W………凯文……………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(-1040, 7030, 21200, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(244, 0)
    OP_8C(0x109, 180, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x109,
        (
            "#1063F#11P……莉丝。\x01",
            "现在我们就加快脚步前进吧。\x02\x03",

            "#1065F不管今后多么哀伤、\x01",
            "多么后悔也好。\x02\x03",

            "#1840F一切等到……\x01",
            "我们活着离开这里之后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        "#1950F#6P#40W………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x10F,
        "#1952F#6P#40W……嗯……我明白了……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C0E)
    OP_28(0x3D, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_396 end

    def Function_4_DFB(): pass

    label("Function_4_DFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E37")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_4_DFB")

    label("loc_E37")

    Return()

    # Function_4_DFB end

    SaveToFile()

Try(main)
