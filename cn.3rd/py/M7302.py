from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7302   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7302.x',
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
        '亡者奥恩',                             # 9
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
        'ED6_DT29/CH14430 ._CH',             # 00
        'ED6_DT29/CH14431 ._CH',             # 01
        'ED6_DT29/CH14720 ._CH',             # 02
        'ED6_DT29/CH14721 ._CH',             # 03
        'ED6_DT29/CH14550 ._CH',             # 04
        'ED6_DT29/CH14551 ._CH',             # 05
        'ED6_DT29/CH14440 ._CH',             # 06
        'ED6_DT29/CH14440 ._CH',             # 07
        'ED6_DT29/CH14760 ._CH',             # 08
        'ED6_DT29/CH14761 ._CH',             # 09
        'ED6_DT29/CH14770 ._CH',             # 0A
        'ED6_DT29/CH14771 ._CH',             # 0B
        'ED6_DT29/CH14340 ._CH',             # 0C
        'ED6_DT29/CH14340 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14430P._CP',             # 00
        'ED6_DT29/CH14431P._CP',             # 01
        'ED6_DT29/CH14720P._CP',             # 02
        'ED6_DT29/CH14721P._CP',             # 03
        'ED6_DT29/CH14550P._CP',             # 04
        'ED6_DT29/CH14551P._CP',             # 05
        'ED6_DT29/CH14440P._CP',             # 06
        'ED6_DT29/CH14440P._CP',             # 07
        'ED6_DT29/CH14760P._CP',             # 08
        'ED6_DT29/CH14761P._CP',             # 09
        'ED6_DT29/CH14770P._CP',             # 0A
        'ED6_DT29/CH14771P._CP',             # 0B
        'ED6_DT29/CH14340P._CP',             # 0C
        'ED6_DT29/CH14340P._CP',             # 0D
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
        X                   = 48930,
        Z                   = 24880,
        Y                   = 31960,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83950,
        Z                   = 32280,
        Y                   = 27430,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 71720,
        Z                   = 44750,
        Y                   = 74240,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 107030,
        Z                   = 51110,
        Y                   = 99980,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73680,
        Z                   = 63540,
        Y                   = 75170,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50530,
        Z                   = 69690,
        Y                   = 94080,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -5750,
        Y                   = 9000,
        Z                   = 5930,
        Range               = 5180,
        Unknown_10          = 0x3A98,
        Unknown_14          = 0x2724,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 65980,
        TriggerZ            = 45750,
        TriggerY            = 75530,
        TriggerRange        = 1000,
        ActorX              = 65980,
        ActorZ              = 45750,
        ActorY              = 75530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 134920,
        TriggerZ            = 57350,
        TriggerY            = 103670,
        TriggerRange        = 1000,
        ActorX              = 134920,
        ActorZ              = 57350,
        ActorY              = 103670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_2A5",          # 02, 2
        "Function_3_3CB",          # 03, 3
        "Function_4_4F1",          # 04, 4
        "Function_5_10FB",         # 05, 5
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Return()

    # Function_0_24A end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFF15A0, 0xFFFEBBC8, 0x230095)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284")
    OP_6F(0x0, 0)
    Jump("loc_28B")

    label("loc_284")

    OP_6F(0x0, 60)

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D")
    OP_6F(0x1, 0)
    Jump("loc_2A4")

    label("loc_29D")

    OP_6F(0x1, 60)

    label("loc_2A4")

    Return()

    # Function_1_24B end

    def Function_2_2A5(): pass

    label("Function_2_2A5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17E, 1)"), scpexpr(EXPR_END)), "loc_319")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x7E\x01\x07\x00。\x02",
    )

    Jump("loc_2FE")

    label("loc_2FE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C64)
    Jump("loc_387")

    label("loc_319")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x7E\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7E\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_368")

    label("loc_368")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_387")

    Jump("loc_3BD")

    label("loc_38A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3BD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2A5 end

    def Function_3_3CB(): pass

    label("Function_3_3CB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1C7, 1)"), scpexpr(EXPR_END)), "loc_43F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xC7\x01\x07\x00。\x02",
    )

    Jump("loc_424")

    label("loc_424")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C65)
    Jump("loc_4AD")

    label("loc_43F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xC7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xC7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_48E")

    label("loc_48E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4AD")

    Jump("loc_4E3")

    label("loc_4B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3CB end

    def Function_4_4F1(): pass

    label("Function_4_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 4)), scpexpr(EXPR_END)), "loc_4F9")
    Return()

    label("loc_4F9")

    EventBegin(0x0)
    OP_D2(0x270176, 0x270183, 0xE)
    OP_D2(0x270177, 0x270184, 0xF)
    OP_D2(0x270178, 0x270185, 0x10)
    OP_D2(0x27058C, 0x270590, 0x11)
    OP_D2(0x27058D, 0x270591, 0x12)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -580, 11630, 19530, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_554():

        label("loc_554")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_554")

    QueueWorkItem2(0x10, 3, lambda_554)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x02#80W#3S噢噢噢噢噢噢噢噢噢……！\x07\x00\x02",
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

    def lambda_60C():
        OP_6D(-1690, 11630, 20500, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_60C)

    def lambda_624():
        OP_67(0, 6220, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_624)

    def lambda_63C():
        OP_6B(2560, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_63C)

    def lambda_64C():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_64C)

    def lambda_65C():
        OP_6E(335, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_65C)

    def lambda_66C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_66C)
    Sleep(100)
    OP_8C(0x1, 0, 400)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x1D9, 0x0, 0x64)
    Fade(1000)

    def lambda_695():
        OP_6B(2300, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_695)

    def lambda_6A5():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6A5)

    def lambda_6B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B5)
    OP_22(0x1E0, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    OP_23(0x1D9)
    Sleep(1000)
    SetChrPos(0x109, -20, 11000, 7770, 0)
    SetChrPos(0x10F, -1290, 10700, 7080, 0)

    def lambda_706():
        OP_6D(-2090, 11630, 16880, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_706)

    def lambda_71E():
        OP_67(0, 6000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_71E)

    def lambda_736():
        OP_6B(2660, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_736)

    def lambda_746():
        OP_6E(334, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_746)

    def lambda_756():
        OP_8E(0xFE, 0xFFFFFEFC, 0x2D6E, 0x31CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_756)
    Sleep(400)

    def lambda_776():
        OP_8E(0xFE, 0xFFFFF984, 0x2D6E, 0x30E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_776)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x02#60W凯文……格拉汉姆………\x01",
            "#3745W \x01",
            "#60W……你…竟敢……\x01",
            "竟敢………将我…给………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #8
        0x10F,
        "#1934F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1075F#6P原来如此……\x01",
            "这是曾经被我消灭的『异端』吗。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x02#60W没错……！\x01",
            "我的…名字……叫……奥恩…！\x01",
            "#6744W \x01",
            "#60W我是……被你……这家伙……\x01",
            "…第一个…干掉……的……牺牲品……呀……！ \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #11
        0x10F,
        "#1942F#6P奥、奥恩……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#6P典礼省的前任司教……\x02\x03",

            "#1072F一个因贪污渎职而被教会流放的人。\x01",
            "之后由于怀恨在心，\x01",
            "最后沦落到收买猎兵袭击『紫苑之家』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1931F#6P………啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1075F#6P他是我作为『异端制裁者』\x01",
            "第一个正法的猎物。\x02\x03",

            "#1073F呵呵，不过万没想到，\x01",
            "居然会在这种地方再次和他相遇……\x02\x03",

            "我说，你现在有何感受？\x01",
            "那种不能在灼热之中死去，\x01",
            "只可在『炼狱』里匍匐挣扎的感觉是……？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x02#80W酷热……痛苦……怨恨………\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_43(0x10, 0x1, 0x0, 0x5)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x02#60W……怨恨……酷热……怨恨……\x01",
            "#50W怨恨……痛苦……怨恨……救我……\x01",
            "#40W……酷热……怨恨……痛苦……怨恨……\x01",
            "#30W救我……酷热……怨恨……怨恨……\x01",
            "#20W……怨恨……救我……怨恨……酷热……\x01",
            "#15W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x01",
            "#10W救我……救我……救我……救我……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #17
        0x10F,
        "#1935F#6P………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1075F#6P哈哈，的确让人相当同情。\x02\x03",

            "#1073F也罢……\x01",
            "看你这么痛苦的样子，\x01",
            "就让我再一次为你超度吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 17)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #19
        0x109,
        (
            "#1065F#6P到一个既没有酷热也没有痛苦的世界……\x02\x03",

            "#1072F仅仅作为魂魄之块『格利摩尔』，\x01",
            "得到永远的安逸吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EEC():
        OP_6D(-2340, 11630, 14590, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_EEC)

    def lambda_F04():
        OP_67(0, 6290, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_F04)

    def lambda_F1C():
        OP_6B(2000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_F1C)

    def lambda_F2C():
        OP_6E(290, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_F2C)
    SetChrChipByIndex(0x10, 1)

    def lambda_F41():
        OP_8F(0xFE, 0xFFFFFC40, 0x2D6E, 0x353E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F41)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    Battle(0x2CC, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x109, -800, 11630, 15130, 0)
    SetChrPos(0x10F, -750, 11630, 13340, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-2500, 11630, 16000, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(315000, 0)
    OP_6E(220, 0)

    def lambda_100E():
        OP_6B(3600, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_100E)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #20
        0x109,
        "#1067F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1949F#6P……凯文……………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #22
        0x109,
        (
            "#1075F#11P……好了。\x01",
            "前路还很漫长。\x02\x03",

            "#1840F我们还是加快脚步吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C0C)
    OP_28(0x3D, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_4_4F1 end

    def Function_5_10FB(): pass

    label("Function_5_10FB")

    Sleep(3000)

    def lambda_1106():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1106)
    Return()

    # Function_5_10FB end

    SaveToFile()

Try(main)
