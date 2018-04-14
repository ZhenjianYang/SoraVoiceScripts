from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4100_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4100_1 ._SN',
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
    OP_6D(-5500, 0, -40280, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -190, 0, -40890, 180)
    SetChrPos(0x105, -1400, 0, -40150, 180)
    SetChrPos(0x104, 620, 0, -40140, 180)
    SetChrPos(0x108, -570, 0, -39260, 180)
    SetChrPos(0x28, -2070, 0, -5120, 180)
    SetChrPos(0x29, 3520, 0, 10640, 180)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_0D()
    Sleep(2000)

    def lambda_168():
        OP_6D(-1400, 0, -41100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_168)

    def lambda_180():
        OP_67(0, 6940, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_180)

    def lambda_198():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_198)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1015F『留在地上的象征』吗。\x02\x03",

            "这个白隼的雕像\x01",
            "感觉是挺可疑的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        (
            "#070F唔，确实是\x01",
            "作为利贝尔象征的鸟嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        "#040F那就调查看看吧。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFF42, 0x0, 0xFFFF5B82, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        (
            "\x07\x05调查铁栅栏的底部\x01",
            "发现贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05　　第三把钥匙在异国之馆中。　\x01",
            "　看看『苍骑士的决心』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    def lambda_300():

        label("loc_300")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_300")

    QueueWorkItem2(0x105, 2, lambda_300)

    def lambda_311():

        label("loc_311")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_311")

    QueueWorkItem2(0x104, 2, lambda_311)
    OP_8E(0x101, 0xFFFFFF42, 0x0, 0xFFFF5E52, 0x3E8, 0x0)
    OP_44(0x105, 0x2)
    OP_44(0x104, 0x2)

    ChrTalk(    #5
        0x101,
        (
            "#1006F好，找对了。\x02\x03",

            "#1015F不过『苍之骑士』\x01",
            "是指什么呢？\x02\x03",

            "是亲卫队的队员们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#040F啊啊……\x01",
            "确实是青色军服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x104,
        (
            "#030F不，说是『异国之馆』\x01",
            "跟亲卫队不搭边吧。\x02\x03",

            "#035F怎么说都太不够华丽了\x01",
            "应该想想其他可能性吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1019F是，是这样吗。\x02\x03",

            "#1015F（嗯，既然是同类说的话\x01",
            "最好是遵从忠告……）\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x10)
    OP_28(0xC4, 0x1, 0x20)
    OP_64(0x7, 0x1)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
