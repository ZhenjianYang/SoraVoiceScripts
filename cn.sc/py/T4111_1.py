from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4111_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(500)
    OP_6D(1120, 0, 63720, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 1620, 0, 63260, 0)
    SetChrPos(0x105, 3140, 0, 62800, 315)
    SetChrPos(0x104, 2160, 0, 61840, 0)
    SetChrPos(0x108, 700, 0, 61860, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1015F嗯～说到老将\x01",
            "还是指摩尔根将军吧……\x02\x03",

            "也就是说，这个就是\x01",
            "『时间的旁观者』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x105,
        (
            "#042F嗯嗯……\x01",
            "我想这个可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        (
            "#030F呼，看来有必要\x01",
            "调查一下里面呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        (
            "\x07\x05艾丝蒂尔他们和家里的人商量\x01",
            "让他们确认了钟。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_6D(-4940, 0, 64160, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    SetChrPos(0xD, -1600, 0, 64260, 90)
    SetChrPos(0xE, -2180, 0, 63520, 90)
    SetChrPos(0xF, -1600, 0, 64800, 90)
    SetChrPos(0x101, 1660, 0, 62460, 0)
    SetChrPos(0x105, -560, 0, 62280, 45)
    SetChrPos(0x104, -240, 0, 61160, 45)
    SetChrPos(0x108, -1620, 0, 61240, 45)
    FadeToBright(1000, 0)

    def lambda_2F3():
        OP_6D(-940, 0, 64160, 3000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F3)
    Sleep(1200)
    OP_8E(0x101, 0x67C, 0x0, 0xF8AC, 0x3E8, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #4
        (
            "\x07\x05调查钟里面，\x01",
            "发现里盖上贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05　　　第二把钥匙在市内。　　　\x01",
            "寻找『留在地上的象征』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #6
        0x108,
        "#074F唔，和猜想的一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        "啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "没想到家里\x01",
            "竟然被放了这种东西……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #9
        0x101,
        (
            "#1016F不过，应该不是\x01",
            "针对这个家恶意所为\x01",
            "我想不用担心的。\x02\x03",

            "#1000F不过保险起见，晚上\x01",
            "还是请锁好门吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        "是，是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        "嗯嗯，会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#030F唔，那么\x01",
            "去下一处看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x4)
    OP_28(0xC4, 0x1, 0x8)
    OP_64(0x0, 0x1)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_43(0xF, 0x0, 0x6, 0x2)
    SetChrPos(0xF, -1460, 0, 64920, 180)
    OP_A2(0x2)
    EventEnd(0x4)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
