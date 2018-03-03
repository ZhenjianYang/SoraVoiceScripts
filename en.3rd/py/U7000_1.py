from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7000_1 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            '',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_A46",          # 03, 3
        "Function_4_B62",          # 04, 4
        "Function_5_DF6",          # 05, 5
        "Function_6_F08",          # 06, 6
        "Function_7_F24",          # 07, 7
        "Function_8_F40",          # 08, 8
        "Function_9_1052",         # 09, 9
        "Function_10_106E",        # 0A, 10
        "Function_11_108A",        # 0B, 11
        "Function_12_119C",        # 0C, 12
        "Function_13_11B8",        # 0D, 13
        "Function_14_11D4",        # 0E, 14
        "Function_15_2106",        # 0F, 15
        "Function_16_2728",        # 10, 16
        "Function_17_284A",        # 11, 17
        "Function_18_2922",        # 12, 18
        "Function_19_29FA",        # 13, 19
        "Function_20_2AD2",        # 14, 20
        "Function_21_2B99",        # 15, 21
        "Function_22_3AA2",        # 16, 22
        "Function_23_3ADF",        # 17, 23
        "Function_24_3B1C",        # 18, 24
        "Function_25_3C0E",        # 19, 25
        "Function_26_3D03",        # 1A, 26
        "Function_27_4662",        # 1B, 27
        "Function_28_475F",        # 1C, 28
        "Function_29_51F3",        # 1D, 29
        "Function_30_6B82",        # 1E, 30
        "Function_31_6BFB",        # 1F, 31
        "Function_32_729C",        # 20, 32
        "Function_33_84D3",        # 21, 33
        "Function_34_A7B8",        # 22, 34
        "Function_35_ACAB",        # 23, 35
        "Function_36_D8B7",        # 24, 36
        "Function_37_D91E",        # 25, 37
        "Function_38_DDC8",        # 26, 38
        "Function_39_F113",        # 27, 39
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270089, 0x27008D, 0x13)
    SetChrPos(0x109, -510, 2070, -19920, 0)
    SetChrPos(0x10F, 1290, 1980, -20110, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-680, 4100, -14130, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(315000, 0)
    OP_6E(490, 0)

    def lambda_13B():
        OP_8E(0xFE, 0xFFFFFDEE, 0x1004, 0xFFFFC586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13B)
    Sleep(500)

    def lambda_15B():
        OP_8E(0xFE, 0x2DA, 0x1004, 0xFFFFC446, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_15B)
    Sleep(300)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1079F#6PHuh? What's that?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-500, 4000, -15000, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(315000, 0)
    OP_6E(516, 0)

    def lambda_212():
        OP_6D(0, 5600, 5620, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_212)

    def lambda_22A():
        OP_67(0, 2350, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22A)

    def lambda_242():
        OP_6B(1900, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_242)

    def lambda_252():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_252)

    def lambda_262():
        OP_6E(493, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_262)
    Sleep(5000)

    def lambda_277():
        OP_8E(0xFE, 0xFFFFFD9E, 0xFA0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_277)
    Sleep(400)

    def lambda_297():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xFFFFFF6A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_297)
    Sleep(600)

    def lambda_2B7():
        OP_6D(0, 5600, 4620, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B7)

    def lambda_2CF():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2CF)

    def lambda_2E7():
        OP_6B(2100, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E7)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(-2029, 4000, 4520, 0)
    OP_67(0, 4610, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(314000, 0)
    OP_6E(492, 0)
    SetChrPos(0x109, -440, 4000, -110, 0)
    SetChrPos(0x10F, 1000, 4000, -190, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x109,
        (
            "#1063F#6PWell, this is foreboding.\x02\x03",

            "Doesn't look to be a relic of the ancient\x01",
            "Zemurian civilization, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        (
            "#1440F#6PI agree. As far as I can tell, it's not any kind\x01",
            "of device. Simply a stone monument.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #3
        0x10F,
        "#1444F#6P...Oh? There's something written near the bottom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        "#1079F#6PHuh. So there is.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_4C1():
        OP_6D(-410, 4200, 6220, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4C1)

    def lambda_4D9():
        OP_67(0, 4720, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4D9)

    def lambda_4F1():
        OP_6B(2000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4F1)

    def lambda_501():
        OP_8F(0xFE, 0x78, 0x1068, 0x1432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_501)
    Sleep(800)

    def lambda_521():
        OP_8F(0xFE, 0x8E8, 0xFA0, 0xFBE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_521)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(250)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)

    def lambda_55B():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_55B)
    Sleep(500)

    ChrTalk(    #5
        0x109,
        "#1067F#5PLet's see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240103, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 230, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00The Hermit's Garden\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #7
        0x109,
        "#1079F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1802F#6PWhat is this supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1060F#5PI'm not sure... It could be a message, or maybe\x01",
            "even...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #10
        0x109,
        (
            "#1060F#5PActually, let me look it over some more before\x01",
            "I say anything.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-450, 4200, 5100, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -330, 4000, 3500, 0)
    SetChrPos(0x10F, 1190, 4000, 3120, 0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x10F,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#6PNope. Can't find any hidden switches or the like\x01",
            "anywhere.\x02\x03",

            "#1067FYou were right. It really is just a stone monument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1445F#6PHmm...\x02\x03",

            "#1440FShall we try destroying it and see if anything\x01",
            "happens, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #14
        0x109,
        (
            "#1061F#5PI get first hit!\x02\x01",

            "#1069F...Wait, no! No way!\x02\x03",

            "#1068FJust because we've established it isn't any kind\x01",
            "of device doesn't mean nothing bad will happen\x01",
            "if we go smashing it to bits!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10F,
        "#1447F#6PDon't worry. I was just joking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1068F#5P(You SO weren't.)\x02\x03",

            "#1060FAnyway, let's save extreme options like that\x01",
            "until after we've explored all of our, uh, more \x01",
            "reasonable ones.\x02\x03",

            "I say we should go and look around somewhere\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        "#1440F#6P...Okay.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2601)
    Sleep(300)
    Fade(1000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_AC end

    def Function_3_A46(): pass

    label("Function_3_A46")

    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xC8, 0xFA0, 0xFAA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97E, 0xFA0, 0xFBE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8C, 0xFA0, 0x1824, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xAF0, 0xFA0, 0x1B94, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8, 0xFA0, 0x2008, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF7E, 0xFA0, 0x222E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFFABA, 0xFA0, 0x20D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF704, 0xFA0, 0x1E32, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFF68C, 0xFA0, 0xF82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x32, 0xFA0, 0xF46, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_A46 end

    def Function_4_B62(): pass

    label("Function_4_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 2)), scpexpr(EXPR_END)), "loc_B6A")
    Return()

    label("loc_B6A")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, 750, 11920, 37190, 0)
    SetChrPos(0x10F, -860, 11920, 36940, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-1060, 11920, 38690, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(315000, 0)
    OP_6E(484, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #18
        0x10F,
        "#1444F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1063F#6PAs far out as the eye can see...\x02",
    )

    CloseMessageWindow()

    def lambda_C33():
        OP_6D(-19030, 23080, 86830, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C33)

    def lambda_C4B():
        OP_67(0, 4890, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C4B)

    def lambda_C63():
        OP_6B(2530, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C63)

    def lambda_C73():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C73)

    def lambda_C83():
        OP_6E(484, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C83)
    WaitChrThread(0x109, 0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #20
        "\x07\x00#1802FJust where...are we...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #21
        (
            "\x07\x00#1067FBeats me.\x02\x03",

            "#1063FStill, wherever we are, it's big.\x02\x03",

            "Judging by how our voices don't\x01",
            "echo, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #22
        "\x07\x00#1445F...Yeah.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2602)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-130, 11920, 40940, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -130, 11920, 40940, 0)
    SetChrPos(0x10F, -130, 11920, 40940, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_B62 end

    def Function_5_DF6(): pass

    label("Function_5_DF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -550, 4100, -14830, 0)
    SetChrPos(0x10F, 800, 4100, -15490, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(470, 4100, -14860, 0)
    OP_67(0, 11440, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(314000, 0)
    OP_6E(565, 0)
    OP_43(0x109, 0x0, 0x1, 0x6)
    Sleep(200)
    OP_43(0x10F, 0x0, 0x1, 0x7)

    def lambda_E8E():
        OP_6D(-150, 4000, -5160, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E8E)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_5_DF6 end

    def Function_6_F08(): pass

    label("Function_6_F08")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_F08 end

    def Function_7_F24(): pass

    label("Function_7_F24")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_F24 end

    def Function_8_F40(): pass

    label("Function_8_F40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -11540, 4100, -9000, 45)
    SetChrPos(0x10F, -11400, 4100, -10550, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-10040, 4000, -7610, 0)
    OP_67(0, 10340, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(282000, 0)
    OP_6E(561, 0)
    OP_43(0x109, 0x0, 0x1, 0x9)
    Sleep(100)
    OP_43(0x10F, 0x0, 0x1, 0xA)

    def lambda_FD8():
        OP_6D(-3940, 4000, -3290, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_FD8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_8_F40 end

    def Function_9_1052(): pass

    label("Function_9_1052")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_1052 end

    def Function_10_106E(): pass

    label("Function_10_106E")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_10_106E end

    def Function_11_108A(): pass

    label("Function_11_108A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 11330, 4100, -9810, 270)
    SetChrPos(0x10F, 12980, 4100, -9720, 270)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(11120, 4100, -10060, 0)
    OP_67(0, 13700, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(359000, 0)
    OP_6E(556, 0)
    OP_43(0x109, 0x0, 0x1, 0xC)
    Sleep(400)
    OP_43(0x10F, 0x0, 0x1, 0xD)

    def lambda_1122():
        OP_6D(1390, 4000, -3380, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1122)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Fade(1000)
    OP_6D(-680, 4000, -2430, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Call(1, 14)
    EventEnd(0x0)
    Return()

    # Function_11_108A end

    def Function_12_119C(): pass

    label("Function_12_119C")

    OP_8E(0xFE, 0xFFFFFBF0, 0xFA0, 0xFFFFF2C2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_119C end

    def Function_13_11B8(): pass

    label("Function_13_11B8")

    OP_8E(0xFE, 0x352, 0xFA0, 0xFFFFF2D6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_13_11B8 end

    def Function_14_11D4(): pass

    label("Function_14_11D4")

    Sleep(300)
    OP_D2(0x260286, 0x26028B, 0x13)
    LoadEffect(0x0, "map\\mp252_01.eff")
    LoadEffect(0x1, "magic\\mg054_3.eff")
    LoadEffect(0x2, "monster\\ms31000.eff")

    ChrTalk(    #23
        0x10F,
        (
            "#1445F#6PWell, we've investigated the whole area now...\x02\x03",

            "...but we didn't find anything that would give us\x01",
            "any idea as to where we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1065F#5PMaybe not specifically.\x02\x03",

            "#1060FI think I may have an idea what kind of place\x01",
            "this is, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x10F,
        "#1444F#6PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1065F#5PIt's a place both within Liberl and not at the\x01",
            "same time.\x02\x03",

            "#1063FLike a separate dimension of sorts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10F,
        (
            "#1803F#6P...\x02\x03",

            "#1443FCan you elaborate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#5PWell, you see, during all the trouble with the\x01",
            "Aureole...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x07\x05Kevin explained about the altered spaces hidden within the Tetracyclic\x01",
            "Towers intended to seal the Aureole away.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #30
        0x10F,
        (
            "#1444F#6PWow...\x02\x03",

            "#1802FSo you think the place we're in may be similar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1060F#5PI can't say for sure, but it's definitely a possibility.\x02\x03",

            "#1065FThere are a few cracks in my theory, unfortunately.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #32
        0x10F,
        (
            "#1443F#6POh, I think I understand what you mean...\x02\x03",

            "The Liberlian Cuisine book we found earlier\x01",
            "is one, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1063F#5PExactly.\x02\x03",

            "#1065FIf we assume this is some kind of enclosed\x01",
            "space sealed away with the Aureole all those\x01",
            "years ago...\x02\x03",

            "...how did a book that was only published this\x01",
            "year get in here?\x02\x03",

            "All the other unusual books are from after the\x01",
            "Great Collapse, too.\x02\x03",

            "#1067FWhich means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#1445F#6P...someone else has been going in and out\x01",
            "of here within the past year?\x02\x03",

            "#1443FCould it be that man in black we met at the\x01",
            "port?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1063F#5PMaybe. Maybe not.\x02\x03",

            "#1068FI wouldn't peg him as the kind of guy who'd\x01",
            "want to read about Liberlian cuisine, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1446F#6PThat's very true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1063F#5PEither way, I think we can say for sure now\x01",
            "that this situation we're in was planned out\x01",
            "by someone.\x02\x03",

            "Possibly before that cube even came into our\x01",
            "possession.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        (
            "#1445F#6PYou really think so...?\x02\x03",

            "#1802FBut if that really is the case...what should we\x01",
            "do now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1068F#5PThere's the million mira question.\x02\x03",

            "#1067FWe don't have much to work with here.\x01",
            "Just a big open area with no way out...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x10F,
        "#1444F#6POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        "#1063F#5PThis again?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-1190, 4000, -2560, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(315000, 0)
    OP_6E(496, 0)
    ClearMapFlags(0x10)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED6")
    PlayEffect(0x1, 0xFF, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1B6D():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1B6D)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BC1():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1BC1)

    ChrTalk(    #42
        0x10F,
        "#1445F#6PAaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        "#1070F#5PUgh!\x02",
    )

    CloseMessageWindow()
    OP_22(0x14B, 0x0, 0x50)
    Sleep(500)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x10F,
        "#1802F#6PTh-That sounded like something broke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1063F#5PYeah. But what...?\x02\x03",

            "#1069F...Crap!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x07\x05Kevin took his battle orbment out of his pocket.\x02\x03",

            "He then noticed all of the quartz in it were shattered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x10F,
        "#1444F#6P...?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05Seeing this, Ries took out her own battle orbment.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x10F)
    Sleep(300)

    ChrTalk(    #49
        0x10F,
        "#1802F#6PMine is the same way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        (
            "#1067F#5PUgh. Even my spare quartz are ruined.\x02\x03",

            "Just what is going on here?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x11D, 0x0, 0x64)
    OP_22(0x217, 0x0, 0x64)
    Fade(500)
    PlayEffect(0x2, 0x2, 0x109, 100, 1000, 400, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x2, 0x2)
    OP_23(0x11D)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #51
        0x109,
        "#1079F#5PWhat?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F72")

    label("loc_1ED6")

    Sleep(400)
    OP_82(0x0, 0x0)
    OP_23(0xC9)
    Sleep(300)
    OP_22(0x11D, 0x0, 0x64)
    OP_22(0x217, 0x0, 0x64)
    Fade(500)
    PlayEffect(0x2, 0x2, 0x109, 100, 1000, 400, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x2, 0x2)
    OP_23(0x11D)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    label("loc_1F72")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_1F86():
        OP_6D(0, 4000, 10440, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F86)

    def lambda_1F9E():
        OP_67(0, 3870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F9E)

    def lambda_1FB6():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FB6)

    def lambda_1FC6():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1FC6)

    def lambda_1FD6():
        OP_6E(507, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1FD6)
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xB8)
    OP_22(0x15F, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0xFF, 0x13, 262144)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_A2(0x2605)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7003   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_11D4 end

    def Function_15_2106(): pass

    label("Function_15_2106")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x260286, 0x26028B, 0x13)
    SetChrPos(0x109, -1040, 4000, -3390, 0)
    SetChrPos(0x10F, 850, 4000, -3370, 0)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)
    OP_82(0x81, 0x0)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_6D(-370, 21220, 40970, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(438, 0)

    def lambda_2199():
        OP_6D(-370, 11800, 40970, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2199)

    def lambda_21B1():
        OP_67(0, 7000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_21B1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_22(0x15F, 0x0, 0x64)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_2222():
        OP_6D(0, 15770, 34670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2222)

    def lambda_223A():
        OP_67(0, 2230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_223A)

    def lambda_2252():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2252)

    def lambda_2262():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2262)

    def lambda_2272():
        OP_6E(458, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2272)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_22(0x117, 0x0, 0x64)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)

    def lambda_22A2():
        OP_6D(-900, 4000, -2500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22A2)

    def lambda_22BA():
        OP_67(0, 5950, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_22BA)

    def lambda_22D2():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22D2)

    def lambda_22E2():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_22E2)

    def lambda_22F2():
        OP_6E(496, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_22F2)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #52
        0x10F,
        "#1444F#6PWh-What just happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1067F#5P...I don't know.\x02\x03",

            "#1063FI'd wager it was this cube's doing.\x02\x03",

            "Guess we can add 'altering this area' to its list\x01",
            "of quirks along with wrecking our quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #55
        0x10F,
        "#1443F#6PAre you sure it's a good idea to keep it on you?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #56
        0x109,
        (
            "#1065F#5PHonestly, I get the feeling we'd be shit outta\x01",
            "luck without it.\x02\x03",

            "#1063FAt least now we've got some new stuff to\x01",
            "investigate that could lead us in the right\x01",
            "direction.\x02\x03",

            "We should go and check all the places that\x01",
            "have changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        "#1440F#6PAll right.\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_254E():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_254E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A1")
    OP_C0(0x26, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_25A1")

    OP_34(0x8, 0xFFFF)
    OP_34(0xE, 0xFFFF)
    OP_3F(0x328, 1)
    OP_3E(0x33E, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269A")
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)

    AnonymousTalk(    #58
        (
            "\x07\x02Salvaged:\x01",
            "#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50\x01",
            "#62ITime Sepith x50\x01",
            "#60ISpace Sepith x50\x01",
            "#61IMirage Sepith x50\x01",
            "from the broken quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_269A")

    OP_6D(240, 4000, -2570, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 240, 4000, -2570, 0)
    SetChrPos(0x10F, 240, 4000, -2570, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    OP_69(0x0, 0x0)
    OP_72(0x400, 0x0)
    ExitThread()
    Sleep(500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_2106 end

    def Function_16_2728(): pass

    label("Function_16_2728")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #59
        0x10F,
        (
            "#1444FShouldn't we investigate that monument\x01",
            "first, Kevin?\x02\x03",

            "That definitely looks to have changed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #60
        0x109,
        "#1063FOh, right. We probably should.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F3")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Jump("loc_2838")

    label("loc_27F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2817")
    OP_90(0x0, 0x5DC, 0x0, 0x5DC, 0xBB8, 0x0)
    Jump("loc_2838")

    label("loc_2817")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2838")
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x5DC, 0xBB8, 0x0)

    label("loc_2838")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_2728 end

    def Function_17_284A(): pass

    label("Function_17_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2856")
    Return()

    label("loc_2856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285F")
    Return()

    label("loc_285F")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #61
        0x10F,
        (
            "#1444FShouldn't we investigate that monument\x01",
            "first, Kevin?\x02\x03",

            "That definitely looks to have changed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #62
        0x109,
        "#1063FOh, right. We probably should.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_284A end

    def Function_18_2922(): pass

    label("Function_18_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_292E")
    Return()

    label("loc_292E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")
    Return()

    label("loc_2937")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #63
        0x10F,
        (
            "#1444FShouldn't we investigate that monument\x01",
            "first, Kevin?\x02\x03",

            "That definitely looks to have changed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #64
        0x109,
        "#1063FOh, right. We probably should.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0x5DC, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_2922 end

    def Function_19_29FA(): pass

    label("Function_19_29FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A06")
    Return()

    label("loc_2A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0F")
    Return()

    label("loc_2A0F")

    EventBegin(0x1)
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #65
        0x10F,
        (
            "#1444FShouldn't we investigate that monument\x01",
            "first, Kevin?\x02\x03",

            "That definitely looks to have changed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #66
        0x109,
        "#1063FOh, right. We probably should.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_19_29FA end

    def Function_20_2AD2(): pass

    label("Function_20_2AD2")

    TalkBegin(0xFF)

    ChrTalk(    #67
        0x10F,
        "#1802FWhat's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1063FIt seems like some kind of barrier, but beyond\x01",
            "that...\x02\x03",

            "That circle on the other side feels like it's\x01",
            "going to be important to us sooner or later,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_20_2AD2 end

    def Function_21_2B99(): pass

    label("Function_21_2B99")

    EventBegin(0x0)
    OP_D2(0x260286, 0x26028B, 0x13)
    LoadEffect(0x0, "map\\mp252_01.eff")
    Fade(500)
    SetChrPos(0x109, 800, 4000, 1030, 0)
    SetChrPos(0x10F, -540, 4000, 810, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-860, 4000, 2380, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(315000, 0)
    OP_6E(411, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #69
        0x10F,
        (
            "#1445F#5PI could understand if it were an artifact or\x01",
            "an orbment, but how did a lump of stone\x01",
            "start glowing like this?\x02\x03",

            "#1443FIt's like magic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1065F#6PNow, there's an apt enough description\x01",
            "if I've ever heard one.\x02\x03",

            "#1063FOnly thing I can add to that is that the laws\x01",
            "of the world as we know them don't seem to\x01",
            "apply to it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #71
        "\x07\x0C\x18#2S#80W...Raise...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x109,
        "#1079F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10F,
        "#1444F#5PThat was a voice, wasn't it?\x02",
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x1, 0x16)
    OP_43(0x10F, 0x0, 0x1, 0x17)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #74
        (
            "\x07\x0C\x18#2S#80W...Raise the cube...\x01",
            "Before...the monument...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_8C(0x109, 0, 400)
    Sleep(100)

    def lambda_2EE9():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2EE9)

    ChrTalk(    #75
        0x109,
        (
            "#1069F#6PWho's there?!\x02\x03",

            "Who are you?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #76
        "\x07\x0C\x18#2S#80W...Please...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #77
        "\x07\x0C\x18#2S#80W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #78
        0x10F,
        "#1443F#5PWhat are we going to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1067F#6PUgh...\x02\x03",

            "#1069FTo hell with it! Not like we got any\x01",
            "better options!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x10F, 0, 400)
    Fade(1000)
    OP_6D(0, 6900, 8770, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(0, 0)
    OP_6E(433, 0)

    def lambda_30B0():
        OP_6D(0, 3950, 8770, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_30B0)

    def lambda_30C8():
        OP_67(0, 3670, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30C8)

    def lambda_30E0():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30E0)

    def lambda_30F0():
        OP_6E(403, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_30F0)
    SetChrPos(0x109, 690, 4000, 1090, 0)
    SetChrPos(0x10F, -480, 4000, 870, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_22(0x15F, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    WaitChrThread(0x109, 0x2)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05#2S#40W...Visitors from afar...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x109,
        "#1063F#6PThis again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10F,
        "#1443F#6PThis voice is different, though...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #83
        (
            "\x07\x05#2S#40W...Welcome...\x01",
            "#800W \x01",
            "#40WIn accordance with my master's wishes, I shall grant you power...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #84
        0x109,
        "#1079F#6PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #85
        (
            "\x07\x05#2S#40WName your currency...\x01",
            "#800W \x01",
            "#40W...so that we may transact within the system that you know...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #86
        0x109,
        (
            "#1069F#6PW-Wait a second!\x02\x03",

            "What do you mean by 'currency'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10F,
        (
            "#1446F#6P...\x02\x03",

            "#1802FMaybe it's going to sell us things in exchange\x01",
            "for mira?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #88
        0x109,
        "#1060F#6POh, I get'cha.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #89
        (
            "\x07\x05#2S#40W...Understood...\x01",
            "#800W \x01",
            "#40WThen I shall grant you power in exchange for that currency...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Fade(1000)
    OP_22(0x161, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    Sleep(1000)
    OP_AA(0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #90
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36DB")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35C7"),
        (1, "loc_3665"),
        (2, "loc_3698"),
        (SWITCH_DEFAULT, "loc_36CB"),
    )


    label("loc_35C7")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_1D(0xD2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_36D8")

    label("loc_3665")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0xA)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_36D8")

    label("loc_3698")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_36D8")

    label("loc_36CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36D8")

    label("loc_36D8")

    Jump("loc_3570")

    label("loc_36DB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #94
        (
            "\x07\x05#2S#40WRelease my brethren...\x01",
            "#800W \x01",
            "#40W...then we shall grant you good fortune...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Fade(500)
    OP_6D(-850, 4000, 1770, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(315000, 0)
    OP_6E(411, 0)
    SetChrPos(0x109, 800, 4000, 1030, 0)
    SetChrPos(0x10F, -540, 4000, 810, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #95
        0x10F,
        "#1443F#5PWhat do you think that was about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        "#1068F#6PHow would I know?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 270, 400)
    Sleep(500)

    ChrTalk(    #97
        0x109,
        (
            "#1840F#6PBizarre as it is to say, we should be able\x01",
            "to buy things for mira and use sepith to\x01",
            "synthesize quartz here.\x02\x03",

            "Pretty useful, if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10F,
        (
            "#1446F#5P...\x02\x03",

            "#1448FWe DO still have the sepith that was left\x01",
            "over when our quartz were shattered...\x02\x03",

            "Perhaps we should use those to synthesize\x01",
            "some new ones?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1060F#6PSounds like a plan to me.\x02\x03",

            "We can stand on our own two feet just fine,\x01",
            "but we're gonna need recovery arts if we\x01",
            "ever find ourselves in a jam.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x2606)
    EventEnd(0x0)
    Return()

    # Function_21_2B99 end

    def Function_22_3AA2(): pass

    label("Function_22_3AA2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ADE")
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    Jump("Function_22_3AA2")

    label("loc_3ADE")

    Return()

    # Function_22_3AA2 end

    def Function_23_3ADF(): pass

    label("Function_23_3ADF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B1B")
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    Jump("Function_23_3ADF")

    label("loc_3B1B")

    Return()

    # Function_23_3ADF end

    def Function_24_3B1C(): pass

    label("Function_24_3B1C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13400, 3000, -12820, 45)
    SetChrPos(0x10F, -15030, 2500, -12140, 45)
    OP_6D(-11560, 4100, -9130, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(359000, 0)
    OP_6E(441, 0)

    def lambda_3B8D():
        OP_8E(0xFE, 0xFFFFD602, 0x1004, 0xFFFFD828, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B8D)

    def lambda_3BA8():
        OP_8E(0xFE, 0xFFFFCF9A, 0x1004, 0xFFFFD9E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3BA8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Call(1, 26)
    Return()

    # Function_24_3B1C end

    def Function_25_3C0E(): pass

    label("Function_25_3C0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 14310, 3000, -11130, 315)
    SetChrPos(0x10F, 13850, 2500, -13140, 315)
    OP_6D(12100, 4100, -8940, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(0, 0)
    OP_6E(439, 0)

    def lambda_3C7F():
        OP_8E(0xFE, 0x2FBC, 0x1004, 0xFFFFDC38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C7F)

    def lambda_3C9A():
        OP_8E(0xFE, 0x2C24, 0x1004, 0xFFFFD620, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3C9A)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x0)
    Call(1, 26)
    Return()

    # Function_25_3C0E end

    def Function_26_3D03(): pass

    label("Function_26_3D03")


    def lambda_3D09():
        OP_6D(0, 15020, 35890, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D09)

    def lambda_3D21():
        OP_67(0, 4640, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D21)

    def lambda_3D39():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3D39)

    def lambda_3D49():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3D49)

    def lambda_3D59():
        OP_6E(446, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3D59)

    def lambda_3D69():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D69)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 750, 9190, 27370, 0)
    SetChrPos(0x10F, -750, 8870, 26740, 0)
    Sleep(500)
    Fade(1000)

    def lambda_3DB4():
        OP_6B(2400, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3DB4)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    Sleep(500)

    ChrTalk(    #100
        0x10F,
        "#1444F#5PYou don't think that could be the exit, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1065F#5PIf anything, I'd say it's more like an entrance.\x02\x03",

            "#1063FA monument that sells us items, a tree that sells\x01",
            "us ingredients, a spring that restores our vitality...\x02\x03",

            "It's like everything in here is designed to help us\x01",
            "prepare for something dangerous. Or am I reading\x01",
            "into it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10F,
        "#1445F#5P...No, I don't think you are.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FCF")
    OP_6D(6920, 4000, 320, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 8130, 4000, -450, 0)
    SetChrPos(0x10F, 6770, 4000, -450, 0)
    Jump("loc_402E")

    label("loc_3FCF")

    OP_6D(-6080, 4000, 80, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(314000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -5140, 4000, -490, 0)
    SetChrPos(0x10F, -6670, 4000, -430, 0)

    label("loc_402E")

    OP_0D()
    OP_8C(0x10F, 90, 400)

    ChrTalk(    #103
        0x10F,
        (
            "#1443F#5PSo what should we do?\x02\x03",

            "Should we try stepping on it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #104
        0x109,
        (
            "#1060F#6PI don't have any better ideas at this point.\x02\x03",

            "#1064FAlthough, it might be better if you stayed\x01",
            "behind he--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10F,
        "#1801F#5P*glare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x109,
        (
            "#1068F#6PNever mind, ma'am. We'll go together.\x02\x03",

            "#1066FIt's not like there's any guarantee you'd\x01",
            "be safe here, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10F,
        (
            "#1446F#5POf course we will.\x02\x03",

            "#1440FBut first, I should give you this.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #108
        "\x07\x05Ries handed Kevin his \x1F\x0A\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20A, 1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x109,
        (
            "#1064F#6P...Huh?\x02\x03",

            "Wh-What are you doing with this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10F,
        (
            "#1448F#5PI was asked to give it to you by Commander \x01",
            "Selnate.\x02\x03",

            "#1447FIn her words: 'Kevin's reports lately have been\x01",
            "far too vague for my liking. I'll bet he's not even\x01",
            "taking notes while he's out on the job.'\x02\x03",

            "'Give him this so he's got no more excuses to\x01",
            "slack off.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x109,
        (
            "#1063F#6PBah... She figured it out, huh?\x02\x03",

            "#1079FHold on! How are you close enough for her\x01",
            "to ask you this kinda favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10F,
        (
            "#1442F#5PShe was the one who taught me how to use\x01",
            "my templar sword.\x02\x03",

            "I respect her deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x109,
        (
            "#1068F#6PN-No joke? I had no idea.\x02\x03",

            "#1067F(I bet she kept that from me on purpose...)\x02\x03",

            "(Can't say I'm surprised... If I'd known,\x01",
            "I sure as hell wouldn't have let Ries...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10F,
        "#1444F#5PKevin...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        (
            "#1065F#6PSorry. Just spacing out.\x02\x03",

            "#1063FOur next destination's that circle,\x01",
            "but if you have anything else you\x01",
            "want to do first, speak up now.\x02\x03",

            "There's no telling what's waiting\x01",
            "for us after we step on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10F,
        "#1448F#5PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x260A)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x8)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_64(0x1, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x3, 0x0, 0x11)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_26_3D03 end

    def Function_27_4662(): pass

    label("Function_27_4662")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, 770, 11920, 40820, 0)
    SetChrPos(0x10F, -500, 11920, 40650, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-530, 11920, 41530, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(314000, 0)
    OP_6E(410, 0)
    OP_0D()
    Sleep(500)

    def lambda_46E8():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_46E8)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -30, 11920, 40820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_27_4662 end

    def Function_28_475F(): pass

    label("Function_28_475F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x260285, 0x26028A, 0x13)
    OP_D2(0x270448, 0x27044C, 0x14)
    LoadEffect(0x0, "map\\mp252_04.eff")
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -160, 4000, -1160, 180)
    SetChrPos(0x10F, 1590, 4000, -1260, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(2330, 12590, 1650, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2250, 0)
    OP_6C(314000, 0)
    OP_6E(461, 0)

    def lambda_487F():
        OP_6D(2330, 6290, 1650, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_487F)

    def lambda_4897():
        OP_67(0, 4880, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4897)

    def lambda_48AF():
        OP_6B(2250, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_48AF)

    def lambda_48BF():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_48BF)

    def lambda_48CF():
        OP_6E(461, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_48CF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(-530, 4000, -50, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(315000, 0)
    OP_6E(399, 0)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x162, 0x0, 0x64)
    Sleep(2000)

    def lambda_49A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_49A5)

    def lambda_49B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_49B7)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    Sleep(500)

    ChrTalk(    #117
        0x10F,
        "#1444F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #118
        0x109,
        (
            "#1060F#5PAll right. That actually worked.\x02\x03",

            "Now we've got a quick way to get back here\x01",
            "to safety if we run into danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #119
        0x10F,
        (
            "#1447F#6PThat does sound useful.\x02\x03",

            "#1448FI still can't bring myself to put much trust\x01",
            "in that cube, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x109,
        (
            "#1075F#5POh, I'm not planning to lower my guard around\x01",
            "the thing, either. I'll keep using it with caution,\x01",
            "so don't worry.\x02\x03",

            "#1060FAnyway...next up's this little guy.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 400, 5330, -1380, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #121
        0x10F,
        (
            "#1443F#6PThat 'sealing stone'?\x02\x03",

            "That voice made it sound like something would be\x01",
            "released from it if we hold it up to the monument.\x02\x03",

            "Any guesses?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #122
        0x109,
        (
            "#1065F#5PNo, but I know how to find out the answer real\x01",
            "quick.\x02\x03",

            "#1063FI'll handle holding it up, but I want you to stand\x01",
            "by prepared for a fight just in case. We've got\x01",
            "no idea what we're dealing with here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10F,
        "#1443F#6PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 20)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)

    def lambda_4E23():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4E23)

    def lambda_4E3B():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4E3B)

    def lambda_4E53():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_4E53)

    def lambda_4E63():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4E63)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x10F,
        "#1444F#6PSomething's happening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1060F#6PAll right... Time for the moment of truth.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_4FE9():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4FE9)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 5000, -500, 0)
    SetChrPos(0x10F, 790, 4000, -2800, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)

    def lambda_508D():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_508D)

    def lambda_50A5():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_50A5)

    def lambda_50BD():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_50BD)

    def lambda_50CD():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_50CD)

    def lambda_50DD():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_50DD)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_5107():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5107)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_28_475F end

    def Function_29_51F3(): pass

    label("Function_29_51F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 0, 4000, -490, 0)
    SetChrPos(0x10F, 1590, 4000, -1260, 0)
    SetChrChipByIndex(0x10F, 20)
    SetChrSubChip(0x10F, 0)
    OP_D2(0x70064, 0x7006C, 0x13)
    OP_D2(0x270448, 0x27044C, 0x14)
    OP_D2(0x26028F, 0x260294, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x11, 0x80)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 390, 8000, 2150, 180)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x4)
    PlayEffect(0x3, 0x0, 0x11, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_532E():
        OP_6D(-600, 4000, 1980, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_532E)

    def lambda_5346():
        OP_67(0, 5590, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5346)

    def lambda_535E():
        OP_6B(2470, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_535E)

    def lambda_536E():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_536E)

    def lambda_537E():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_537E)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x11, 0, 400, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_53E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_53E5)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #126
        0x109,
        "#1069F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10F,
        "#1444F#6PA...girl...?\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x11, 0, 400, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_54AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_54AA)
    WaitChrThread(0x11, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #128
        0x11,
        (
            "#562F#5PH-Huuuh?\x02\x03",

            "Wh-What was that light...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x109,
        "#1064F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #130
        0x10F,
        (
            "#1444F#6PIsn't she the girl from the professor's\x01",
            "photograph?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #131
        0x11,
        "#063F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x11,
        (
            "#064F#11PK-Kevin...?\x02\x03",

            "You ARE Kevin, aren't you? I'm not seeing things?\x02\x03",

            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x109,
        (
            "#1068F#6PWhere do I even start...?\x02\x03",

            "#1066FHaha. But yeah, it's the real deal.\x01",
            "Good to see you again, Tita.\x02\x03",

            "Looks like you've grown a little taller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        (
            "#067F#11PYou noticed? Heehee.\x02\x03",

            "#560FI'm happy to see you again, too! What brings\x01",
            "you back to Liberl?\x02\x03",

            "#064FIs this girl a friend of yours?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_8C(0x11, 270, 400)
    Sleep(500)
    OP_8C(0x11, 90, 400)
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0x11,
        (
            "#064F#5P...Waaait...\x02\x03",

            "I was in the house with Dad getting dinner\x01",
            "ready because Agate was coming over...\x02\x03",

            "...then all of a sudden, everything went white,\x01",
            "and then...\x02\x03",

            "...and then...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x11, 0x0, 0x1, 0x1E)

    ChrTalk(    #136
        0x11,
        (
            "#065F#5PWh-Where am I?! This looks nothing like our house!\x02\x03",

            "Am I d-dreaming?! Is this all a dream?!\x02\x03",

            "Oh, right! I should pinch myself to check!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x109,
        (
            "#1840F#6PHaha... Yep. This is the Tita everyone knows\x01",
            "and loves, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x10F,
        "#1442F#6P(She's adorable...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    OP_D2(0x260286, 0x26028B, 0x13)
    SetChrPos(0x11, 390, 4000, 1500, 180)
    OP_8C(0x109, 0, 0)
    OP_8C(0x10F, 0, 0)
    OP_8C(0x11, 180, 0)
    ClearChrFlags(0x11, 0x4)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)
    OP_6D(-600, 4000, 1800, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #139
        0x11,
        (
            "#063F#11PSo that's what happened...\x02\x03",

            "This is all because of that artifact Mom\x01",
            "pulled out of the lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x109,
        "#1065F#6PHonestly, we can't even be sure right now. \x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(300)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(    #141
        0x109,
        (
            "#1063F#6PEspecially as if we assume that's the case,\x01",
            "how did you end up here when you were all\x01",
            "the way over in Zeiss? It makes no sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        (
            "#065F#11PY-You're right...\x02\x03",

            "It sounds as though you two were fairly close\x01",
            "to one another when you were sent here,\x01",
            "but Grancel and Zeiss are really far apart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10F,
        (
            "#1446F#6PBased on your account, however, we were all\x01",
            "surrounded by that light at roughly the same\x01",
            "time.\x02\x03",

            "#1440FThat's more than a coincidence in my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        (
            "#063F#11PYeah. I think so, too...\x02\x03",

            "#064F...Oh! Whoops. I haven't introduced myself\x01",
            "yet, have I?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #145
        0x11,
        (
            "#560F#11PMy name's Tita Russell! I'm an apprentice at\x01",
            "Zeiss Central Factory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10F,
        (
            "#1448F#6PI'm Ries Argent, a sister of the Septian Church.\x02\x03",

            "I've heard a lot about you from Kevin and your\x01",
            "mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        "#064F#11POh, you've met Mom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x10F,
        (
            "#1447F#6PI have. She showed me a photograph of you,\x01",
            "too.\x02\x03",

            "#1442FAnd now that I've met you in person, I can see\x01",
            "why she boasts about you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x11,
        (
            "#562F#11PWas she doing that? Oh, Mom...\x02\x03",

            "#063FShe... Umm... She didn't say or do anything\x01",
            "inappropriate to you, did she?\x02\x03",

            "She tends to lose control of herself when it\x01",
            "comes to people as cute as you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x10F,
        "#1444F#6P...Lose control, how?\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #151
        0x11,
        (
            "#560F#11PE-Erm, I-I'm sorry! I wasn't trying to be rude\x01",
            "by calling you cute or anything!\x02\x03",

            "#067FIt's just that you're kind of quiet and really\x01",
            "pretty, but you've got this really unique aura\x01",
            "about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x10F,
        "#1802F#6P...Unique?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x109,
        (
            "#1061F#6PHaha. You're every bit as sharp as your mother.\x02\x03",

            "#1062FThe Goddess doesn't make 'em more 'unique' than \x01",
            "Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10F,
        "#1801F#6POh, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x11,
        (
            "#067F#11PUmm... Anyway...\x02\x03",

            "#560FWhat're the two of you planning on doing now?\x02\x03",

            "Are you going to keep looking for a way out of\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x109,
        (
            "#1060F#6PThat's the plan, yeah.\x02\x03",

            "#1068FNot that we've made so much as a dent of\x01",
            "progress on that front so far. We'd barely\x01",
            "started exploring when we found you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x11,
        (
            "#060F#11POh, I see...\x02\x03",

            "#560FIf you don't mind, then, please let me help\x01",
            "you look!\x02\x03",

            "I won't get in the way. I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10F,
        (
            "#1444F#6PGetting in the way wouldn't be the issue,\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x109,
        (
            "#1065F#6PHmm... That's a tough one.\x02\x03",

            "#1840FMy gut tells me you're better off staying here,\x01",
            "to be honest.\x02\x03",

            "You've proven yourself to be made of sturdy\x01",
            "stuff, but like I said before, this place is\x01",
            "just one big and very dangerous mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x11,
        (
            "#062F#11PIf that's true, then who's to say I'd be safe\x01",
            "staying here on my own?\x02\x03",

            "If I'm going to be in danger, I'd rather go\x01",
            "with you and at least try to help out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x109,
        (
            "#1075F#6PFair point, I guess.\x02\x03",

            "#1066FHaha. You're every bit as spunky as Estelle,\x01",
            "too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        "#067F#11PHeehee.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #163
        0x10F,
        "#1443F#6PYou can't be serious, Kevin...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #164
        0x109,
        (
            "#1060F#5PTrust me. She's a lot tougher than she looks.\x02\x03",

            "She went on the Liber Ark and came back down\x01",
            "in one piece, plus she's survived Aidios-knows-\x01",
            "how-many sketchy fights beforehand.\x02\x03",

            "Don't be so quick to judge just because of her\x01",
            "age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10F,
        "#1802F#6PBut still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        (
            "#063F#11PPlease! I really want to help!\x02\x03",

            "I'll do everything I can to make sure I don't\x01",
            "cause you any problems. Really!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1444F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_674D():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_674D)
    Sleep(200)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #168
        0x10F,
        "#1448F#6PAll right. If you're sure.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x11,
        "#064F#11PYou mean it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10F,
        (
            "#1447F#6PYou seem to understand the consequences of your\x01",
            "actions and what it means to worry others.\x02\x03",

            "And as long as that's the case, I've got no reason\x01",
            "to say no.\x02\x03",

            "#1442F...Still, please do be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        "#560F#11PTh-Thank you! I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x109,
        (
            "#1068F#6PYeah. Seriously...\x02\x03",

            "If anything were to happen to you on my watch,\x01",
            "I'm sure my death at Erika's hands would be a\x01",
            "slow and painful one.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #173
        0x11,
        "#065F#11PI swear, I won't let that happen!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #174
        0x109,
        (
            "#1060F#5PDeal. All right, let's get back to work.\x02\x03",

            "Once Tita's equipment is set up, it's back\x01",
            "to exploring we go.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 315, 400)
    Sleep(300)

    ChrTalk(    #175
        0x10F,
        "#1448F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x11,
        "#560F#11PRight!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6A64():
        OP_6B(2770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x260D)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_3F(0x352, 1)
    OP_DB(0x0, 0x6)
    OP_DC(0x1, 0x0, 0x6)
    AddParty(0x6, 0xF0, 0xFF)
    OP_A2(0x25CC)
    Call(6, 16)
    SetChrFlags(0x11, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(630, 4000, -1100, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 630, 4000, -1100, 180)
    SetChrPos(0x10F, 630, 4000, -1100, 180)
    SetChrPos(0x107, 630, 4000, -1100, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_29_51F3 end

    def Function_30_6B82(): pass

    label("Function_30_6B82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BFA")
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 270, 600)
    Sleep(300)
    OP_8C(0x11, 90, 600)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    Sleep(300)
    OP_8C(0x11, 225, 600)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 135, 600)
    Sleep(300)
    OP_8C(0x11, 0, 600)
    Sleep(500)
    Jump("Function_30_6B82")

    label("loc_6BFA")

    Return()

    # Function_30_6B82 end

    def Function_31_6BFB(): pass

    label("Function_31_6BFB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x107, 1110, 4000, -3200, 0)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_6D04():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6D04)

    def lambda_6D1C():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6D1C)

    def lambda_6D34():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6D34)

    def lambda_6D44():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6D44)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6E49():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6E49)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #177
        0x107,
        (
            "#560F#5POooh!\x02\x03",

            "Is this the part where someone comes\x01",
            "out of it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EB2():
        OP_6D(-1040, 4000, -40, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6EB2)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #178
        0x10F,
        (
            "#1448F#5PGiven past precedent, most likely so.\x02\x03",

            "#1447FWhether it's someone completely different or a\x01",
            "second Tita remains to be seen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #179
        0x107,
        "#065F#6PA-A second me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x109,
        (
            "#1068F#5PIf you've jinxed us and we really do get a second\x01",
            "Tita, I hope you're ready to be her new mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10F,
        "#1447F#5PNaturally. I'll love her like my own.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #182
        0x107,
        "#067F#6PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    def lambda_708C():
        OP_8C(0x10F, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_708C)
    Sleep(100)
    OP_8C(0x107, 0, 400)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x107, 900, 4000, -3200, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_7136():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7136)

    def lambda_714E():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_714E)

    def lambda_7166():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7166)

    def lambda_7176():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7176)

    def lambda_7186():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7186)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_71B0():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_71B0)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_31_6BFB end

    def Function_32_729C(): pass

    label("Function_32_729C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    SetChrPos(0x107, 1630, 4000, -3030, 0)
    OP_D2(0x260287, 0x26028C, 0x13)
    OP_D2(0x270021, 0x270024, 0x14)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, 390, 8000, 2150, 180)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x800)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x0, 0x12, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_73E4():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73E4)

    def lambda_73FC():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73FC)

    def lambda_7414():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7414)

    def lambda_7424():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7424)

    def lambda_7434():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7434)
    WaitChrThread(0x12, 0x0)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x12, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_74A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_74A0)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #183
        0x10F,
        "#1444F#6P...A military uniform?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x107,
        "#064F#6PW-Wait. Isn't that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x109,
        (
            "#1065F#5PI knew it.\x02\x03",

            "#1840FThe stone being inside the Arseille did make\x01",
            "me wonder if it'd be someone related to it,\x01",
            "and I was right on the mark.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x12, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_7630():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7630)
    OP_82(0x2, 0x2)
    WaitChrThread(0x12, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #186
        0x12,
        "Captain Schwarz",
        "#175F#5PUgh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 20)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #187
        0x12,
        "Captain Schwarz",
        "#177F#11PWhat happened, Echo?! Report!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x12, 0xFFFFFED4, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)

    NpcTalk(    #188
        0x12,
        "Captain Schwarz",
        "#173F#11P...What? How the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x107,
        "#560F#6PU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x109,
        (
            "#1066F#6PYou're probably feeling kind of confused right\x01",
            "now, but it's good to see you again, Julia.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0x12,
        "Captain Schwarz",
        "#173F#11PFather? Tita?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x800)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x12, 90, 400)
    Sleep(500)
    OP_8C(0x12, 270, 400)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    NpcTalk(    #192
        0x12,
        "Captain Schwarz",
        (
            "#176F#5PBefore greeting all of you, I would simply\x01",
            "like to ask...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(500)

    NpcTalk(    #193
        0x12,
        "Captain Schwarz",
        "#178F#11P...is this a dream or illusion? Or reality?\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -670, 4000, -2950, 0)
    SetChrPos(0x107, 1130, 4000, -3670, 0)
    SetChrPos(0x12, 290, 4000, -190, 180)
    ClearChrFlags(0x12, 0x4)
    OP_6D(-1420, 4000, -120, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #194
        0x12,
        "Captain Schwarz",
        (
            "#176F#11PI see...\x02\x03",

            "#175FTo be honest, all of this is a little hard to swallow,\x01",
            "but it's clear I have no choice but to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x109,
        (
            "#1065F#6PThanks for being quick on the uptake.\x02\x03",

            "#1063FDo you happen to remember what happened\x01",
            "to you before you found yourself here?\x02\x03",

            "Were you also surrounded by a white light\x01",
            "last night?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #196
        0x12,
        "Captain Schwarz",
        (
            "#176F#11PIt feels closer to mere moments ago rather than\x01",
            "last night, but I'd assume so.\x02\x03",

            "#178FI was on my way back to Leiston Fortress after\x01",
            "finishing an airborne training exercise when it\x01",
            "happened.\x02\x03",

            "I was sitting in my usual chair on the bridge\x01",
            "when the white light you speak of appeared,\x01",
            "and then...well...\x02\x03",

            "#175FI have no memories between that and finding\x01",
            "myself here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x109,
        "#1065F#6PThat about matches up with us, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10F,
        (
            "#1445F#6PAll of us were drawn in here in roughly the\x01",
            "same circumstances and at roughly the same\x01",
            "time...\x02\x03",

            "#1443FMight you have any idea what happened to\x01",
            "the rest of the ship's crew?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #199
        0x12,
        "Captain Schwarz",
        (
            "#175F#11PI'm afraid not...\x02\x03",

            "I would be somewhat relieved if I were the only\x01",
            "one drawn into this, but I have my doubts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x107,
        (
            "#063F#6PSeeing as the Arseille itself is here, could the\x01",
            "rest of the crew have ended up here, too?\x02\x03",

            "Or is it possible it was just you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x109,
        (
            "#1063F#5PWe really don't have enough to go on to\x01",
            "be sure either way at this point.\x02\x03",

            "#1065FAll we know is that there was no one else\x01",
            "in the Arseille when we found it.\x02\x03",

            "The only sealing stone there was the one\x01",
            "Julia was inside of, too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #202
        0x12,
        "Captain Schwarz",
        (
            "#175F#11P...\x02\x03",

            "#176FFather Graham.\x02\x03",

            "#178FThe two of you have started to investigate this\x01",
            "peculiar place, have you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x109,
        "#1060F#6PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x10F,
        (
            "#1440F#6PWe haven't been doing it for very long,\x01",
            "so we haven't made much progress yet.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #205
        0x12,
        "Captain Schwarz",
        (
            "#178F#11PThen please allow me to assist you.\x02\x03",

            "I'm concerned about the safety of my subordinates,\x01",
            "and I want to know why the Arseille became non-\x01",
            "functional.\x02\x03",

            "And I think cooperating with the three of you will\x01",
            "be the fastest way for me to answer both of those\x01",
            "questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        "#560F#6PI'd LOVE that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x109,
        (
            "#1078F#6PBelieve me, you won't see us complaining.\x02\x03",

            "We'd have to be nuts to turn down the help\x01",
            "of the Royal Army's finest up-and-coming\x01",
            "swordsman.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #208
        0x12,
        "Captain Schwarz",
        (
            "#179F#11PHaha... I fear you are overestimating my \x01",
            "swordsmanship, but I appreciate you allowing\x01",
            "me to accompany you all the same.\x02\x03",

            "#170FWell, in that case, we should get started as soon\x01",
            "as possible.\x02\x03",

            "It's my pleasure to fight alongside all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10F,
        "#1448F#6PLikewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x107,
        "#560F#6PWe're happy to have you!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_839A():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_839A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x261A)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_3F(0x353, 1)
    OP_DB(0x0, 0xD)
    OP_DC(0x1, 0x0, 0xD)
    AddParty(0xD, 0xF1, 0xFF)
    OP_A2(0x25D4)
    Call(6, 22)
    SetChrFlags(0x12, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 390, 4000, -1290, 180)
    SetChrPos(0x10F, 390, 4000, -1290, 180)
    SetChrPos(0x107, 390, 4000, -1290, 180)
    SetChrPos(0x10E, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x10E, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_32_729C end

    def Function_33_84D3(): pass

    label("Function_33_84D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_1D(0xB2)
    Sleep(1500)
    SetMessageWindowPos(350, 100, -1, -1)
    SetChrName("Younger Girl's Voice")

    AnonymousTalk(    #211
        (
            "\x07\x0C#30WHey...\x02\x03",

            "Come over here for a minute.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 200, -1, -1)
    SetChrName("Elder Girl's Voice")

    AnonymousTalk(    #212
        (
            "\x07\x0C#30WHonestly... How many times do I have to tell you\x01",
            "not to run off without telling me, Ries?\x02\x03",

            "I had the fright of my life when I turned around\x01",
            "after finishing my shopping to find you weren't\x01",
            "there.\x02\x03",

            "Don't do that again, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 100, -1, -1)
    SetChrName("Younger Girl's Voice")

    AnonymousTalk(    #213
        (
            "\x07\x0C#30WI just smelled something nice from the stall\x01",
            "over there...\x02\x03",

            "But hey! I found something weird.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 200, -1, -1)
    SetChrName("Elder Girl's Voice")

    AnonymousTalk(    #214
        "\x07\x0C#30W...Weird?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_AD(0x240106, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #215
        "\x07\x0C#30WOh, goodness...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 260, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #216
        (
            "\x07\x0C#30WDo you think he's dead?\x02\x03",

            "Or maybe he indulged in\x01",
            "excess gormandizing? \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #217
        (
            "\x07\x0C#30WI'm...almost certain it's not the latter...\x02\x03",

            "I swear, what are they teaching children\x01",
            "in school these days...?\x02\x03",

            "...Never mind. I suppose that should wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS407._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS408._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS409._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS410._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS411._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS412._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #218
        (
            "\x07\x0C#30WHey there.\x02\x03",

            "Can you hear us?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #219
        "\x07\x0C#60W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #220
        (
            "\x07\x0C#30WWhew... It looks like he's conscious, at least.\x02\x03",

            "What's the matter? I can't see this being a very\x01",
            "comfortable place to sit.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #221
        "\x07\x0C#60W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #222
        "\x07\x0C#30WUmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #223
        (
            "\x07\x0C#30WMaybe he's just hungry?\x02\x03",

            "When you're really hungry, sometimes you don't\x01",
            "have the energy to talk.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #224
        (
            "\x07\x0C#30WYou might actually be right, there...and you'd\x01",
            "know better than anyone.\x02\x03",

            "Well, then! I think I've got just the thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #225
        (
            "\x07\x0C#30W...!\x02\x03",

            "When did you get Quincy Bell chocolate?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #226
        (
            "\x07\x0C#30WI bought this for you originally, so I'm sorry,\x01",
            "Ries.\x02\x03",

            "Do you mind if he has this?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #227
        "\x07\x0C#30WO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(170, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #228
        "\x07\x0C#30WHeehee. Good girl.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #229
        (
            "\x07\x0C#30WCome on. Why don't you try some?\x02\x03",

            "I think you'll like it. Especially if you like\x01",
            "sweet things.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #230
        "\x07\x0C#60W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #231
        (
            "\x07\x0C#30WQuincy chocolate's the best there is.\x02\x03",

            "There might be a brand that tastes nicer,\x01",
            "but they've got the best balance between\x01",
            "taste and cost.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #232
        (
            "\x07\x0C#30WSee? That's a glowing review coming from\x01",
            "none other than my darling little sister.\x02\x03",

            "The taste should help warm you up a bit, too.\x01",
            "Go on! See what you think.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #233
        "\x07\x0C#80W...Get...st...#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(210, 320, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #234
        "\x07\x0C#30WWhat was that?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(220, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #235
        "\x07\x0C#30WOh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #236
        "\x07\x0C#30W...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #237
        (
            "\x07\x0C#80W...I said...get lost...\x02\x03",

            "Just leave me alone.\x02\x03",

            "Please...#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #238
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #239
        "\x07\x0C#30WWhat should we do?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #240
        (
            "\x07\x0C#30WSo you're not going to take me up on my offer,\x01",
            "huh?\x02\x03",

            "I guess I'm left with no choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 350, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #241
        "\x07\x0C#30WWhy're you eating it...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 330, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #242
        (
            "\x07\x0C#30W*munch*\x02\x03",

            "Mm...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS413._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS414._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS415._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #243
        "\x07\x0C#60WMmmfff?!#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #244
        "\x07\x0C#40W...Mmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #245
        (
            "\x07\x0C#60W！☆▲？◎￥＃＄◆?!\x02\x03",

            "...Ngh...*gulp*...#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 380, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #246
        "\x07\x0C#40WWhoooa...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #247
        (
            "\x07\x0C#30W...Whew.\x02\x03",

            "That should be enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #248
        "\x07\x0C#80W...Gah...*cough*...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(120, 330, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #249
        "\x07\x0C#40WWh-Wh-Wh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(60, 330, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #250
        "\x07\x0C#30W#4SWhat the hell was THAT for?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #251
        (
            "\x07\x0C#30WHaha. Looks like that did the trick.\x02\x03",

            "See? I told you that sweet things are\x01",
            "great for perking you up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #252
        (
            "\x07\x0C#30WThat wasn't the chocolate! That was YOU being a\x01",
            "maniac!\x02\x03",

            "What kinda girl does that to a kid they just found\x01",
            "on the street?! A-Are you some kinda p-pedophile\x01",
            "or something?!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #253
        (
            "\x07\x0C#30WOh, my... The Sunday School curriculum really\x01",
            "seems to have changed since I went there.\x02\x03",

            "But where else could you and Ries be picking up\x01",
            "these fancy words, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 360, -1, -1)
    SetChrName("Younger Girl")

    AnonymousTalk(    #254
        "\x07\x0C#30WI don't think that's really the problem...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 330, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #255
        (
            "\x07\x0C#30WY-Yeah, what she said!\x02\x03",

            "Wait a sec...\x02\x03",

            "Your clothes look familiar...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #256
        (
            "\x07\x0C#30WHeehee. Oh, come to think of it, I haven't\x01",
            "introduced myself yet, have I?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_AD(0x240110, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Elder Girl")

    AnonymousTalk(    #257
        (
            "\x07\x0C#30WMy name's Rufina.\x01",
            "Rufina Argent.\x02\x03",

            "And this is my little sister, Ries.\x02\x03",

            "How about you? What's your name?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(0, 16777215, -1)
    OP_AE(0x64)
    Sleep(3000)
    OP_20(0xBB8)
    OP_21()
    OP_C7(0x1, 0xFF, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    SetChrPos(0x109, 1300, 4000, 320, 180)
    SetChrPos(0x10F, -160, 4000, 160, 90)
    SetChrPos(0x107, 2430, 4000, -1600, 315)
    SetChrPos(0x10E, 670, 4000, -1720, 0)
    OP_6D(0, 4000, 420, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(314000, 0)
    OP_6E(429, 0)
    Sleep(1000)
    SetMessageWindowPos(150, 80, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #258
        (
            "\x07\x00Kevin...\x02\x03",

            "Kevin, are you listening?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 230, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #259
        "\x07\x00#1063F#3S...!!#2S\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    OP_1D(0xD2)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(300)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #260
        0x109,
        (
            "#1079F#6P...Oh.\x02\x03",

            "#1066FSorry about that. Must've spaced out a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x10F,
        "#1802F#5PAre you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x10E,
        (
            "#176F#6PIt's understandable, really.\x02\x03",

            "#178FAfter all that's happened, it's no\x01",
            "surprise you're feeling tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x107,
        (
            "#063F#6PMaybe you should rest up some before\x01",
            "we keep going?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #264
        0x109,
        (
            "#1075F#11PHaha. Nah, don't worry about me.\x02\x03",

            "#1060FAnyway, we were about to start going over all\x01",
            "the information we've gathered so far, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x10F,
        "#1802F#5PYes, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x10E,
        (
            "#176F#6PHe may not be our ally, but our encounter\x01",
            "with that 'Schwarzritter' turned out to be\x01",
            "quite illuminating.\x02\x03",

            "#178FWe finally have the name of this strange\x01",
            "place we've found ourselves in, for one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x107,
        (
            "#062F#6PThat's right.\x02\x03",

            "He called it 'Phantasma,' right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x109,
        (
            "#1065F#11PYep. Interesting name it's got.\x02\x03",

            "#1063FNot sure where it came from, though. As far as\x01",
            "I know, it's nothing from the church's scripts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x10F,
        (
            "#1446F#5PI've never heard it before, either.\x02\x03",

            "#1443FThen there's the existence of his 'lord.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x109,
        (
            "#1063F#11PWell, judging by how that guy spoke of them,\x01",
            "that must be the big boss around here.\x02\x03",

            "They seem to know a whole lot about us, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x10E,
        (
            "#178F#6PIncidentally, there was one thing that knight\x01",
            "mentioned which made me curious.\x02\x03",

            "It mentioned you having a sister, Ries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x10F,
        "#1445F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x109,
        "#1067F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x10E,
        (
            "#173F#6POh, my. I didn't mean to pry into your personal\x01",
            "affairs. Should I not have asked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x109,
        "#1060F#11PNah. I don't blame you for being curious.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(300)

    ChrTalk(    #276
        0x10F,
        (
            "#1446F#5PAs he said, I did indeed have a sister.\x02\x03",

            "#1443FHer name was Rufina.\x02\x03",

            "She was one of the Gralsritter just like I am now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #277
        0x109,
        "#1063F#6PRies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x10E,
        (
            "#178F#6PI take it that your use of the past tense \x01",
            "means...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x10F,
        (
            "#1448F#5PYes. She fell in the line of duty during a mission.\x02\x03",

            "Roughly five years ago, to be precise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x109,
        "#1067F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x10E,
        (
            "#176F#6PI see...\x02\x03",

            "#178FBut in that case, how could that man possibly\x01",
            "know so much about her skills?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x10F,
        (
            "#1445F#5P...I wish I knew.\x02\x03",

            "I don't really know much about the work she did.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #283
        0x10F,
        "#1802F#5PWhat about you, Kevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x109,
        (
            "#1067F#6P...\x02\x03",

            "#1065FSorry. I can't think of how she might have met\x01",
            "him, either.\x02\x03",

            "#1060FStill, she was known for being one skilled knight.\x02\x03",

            "And not just in terms of strength in battle--her\x01",
            "judgment and negotiation abilities were both top\x01",
            "class, too.\x02\x03",

            "The details of her missions are as much a mystery\x01",
            "to me as they are for Ries, but it's not a stretch to\x01",
            "think she could've met him during one of 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x10F,
        "#1440F#5PI suppose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x10E,
        (
            "#178F#6PWe've little more than conjecture to go off\x01",
            "of. I suppose the matter will have to remain\x01",
            "unsolved for now.\x02\x03",

            "#175F...My apologies. I should never have asked.\x01",
            "All I did was bring up painful memories for\x01",
            "the two of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #287
        0x109,
        (
            "#1840F#11PDon't sweat it.\x02\x03",

            "#1065FWe still learned something out of this,\x01",
            "and that's that our enemies are keeping\x01",
            "a pretty close eye on what we do here.\x02\x03",

            "#1063FWe're gonna need to be careful every step\x01",
            "of the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x10E,
        (
            "#179F#6PSo it seems.\x02\x03",

            "#170FShall we get back to our ever-cautious trek,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x107,
        (
            "#560F#6PWe'll have to go back to where we met that guy\x01",
            "and keep going from there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x109,
        (
            "#1060F#11PYeah. I saw another warp at the top of the\x01",
            "stairs.\x02\x03",

            "Thankfully, the cube can get us back there\x01",
            "in no time flat once we're up for it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A671():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A671)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2700)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_28(0x2A, 0x1, 0x10)
    OP_28(0x2A, 0x1, 0x20)
    OP_28(0x2A, 0x1, 0x40)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x4, 0x20)
    OP_28(0x29, 0x4, 0x10)
    OP_28(0x29, 0x4, 0x20)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x4, 0x20)
    OP_28(0x2B, 0x4, 0x4)
    OP_28(0x2B, 0x4, 0x8)
    OP_28(0x2B, 0x1, 0x1)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, 390, 4000, -1290, 180)
    SetChrPos(0x10F, 390, 4000, -1290, 180)
    SetChrPos(0x107, 390, 4000, -1290, 180)
    SetChrPos(0x10E, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrChipByIndex(0x10F, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x10E, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_33_84D3 end

    def Function_34_A7B8(): pass

    label("Function_34_A7B8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x107, 1250, 4000, -3900, 0)
    SetChrPos(0x10E, -200, 4000, -4300, 0)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A8D2():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A8D2)

    def lambda_A8EA():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A8EA)

    def lambda_A902():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_A902)

    def lambda_A912():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_A912)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_A9FB():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A9FB)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #291
        0x107,
        (
            "#067F#5PHeehee... I still can't get over how pretty\x01",
            "they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x10E,
        "#173F#5PSo this is how I was released, too, was it?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x107, 750, 4000, -3900, 0)
    SetChrPos(0x10E, -500, 4000, -4300, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_AB42():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AB42)

    def lambda_AB5A():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB5A)

    def lambda_AB72():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AB72)

    def lambda_AB82():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_AB82)

    def lambda_AB92():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AB92)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_ABBC():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_ABBC)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2721)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_34_A7B8 end

    def Function_35_ACAB(): pass

    label("Function_35_ACAB")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS499._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS446._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS447._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS448._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_D2(0x26029B, 0x2602A0, 0x13)
    OP_D2(0x26029C, 0x2602A1, 0x14)
    OP_D2(0x260286, 0x26028B, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp252_01.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    SetChrPos(0x107, 1630, 4000, -3530, 0)
    SetChrPos(0x10E, 240, 4000, -3980, 0)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 390, 8000, 2150, 180)
    SetChrFlags(0x13, 0x800)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x4)
    PlayEffect(0x3, 0x0, 0x13, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_AEDE():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEDE)

    def lambda_AEF6():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AEF6)

    def lambda_AF0E():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF0E)

    def lambda_AF1E():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AF1E)

    def lambda_AF2E():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_AF2E)
    WaitChrThread(0x13, 0x0)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x13, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_AF9A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_AF9A)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #293
        0x10E,
        "#173FThat looks like#6P...!\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x13, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_B088():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_B088)
    OP_82(0x2, 0x2)
    WaitChrThread(0x13, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #294
        0x13,
        "Major Vander",
        "#272F#5PUgh... What was that? A stun grenade?!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #295
        0x13,
        "Major Vander",
        (
            "#271F#11P#3SFall back, Olivier! \x01",
            "Their target is likely to be--\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x13, 0xFFFFFF38, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #296
        0x13,
        "Major Vander",
        "#273F#11PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x10E,
        "#171F#6PIt really is you.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #298
        0x13,
        "Major Vander",
        (
            "#273F#11PCaptain Schwarz? What are you doing here?\x02\x03",

            "#270F#3S...?!#2S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x13, 0x800)
    SetChrChipByIndex(0x13, 5)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x13, 90, 400)
    Sleep(500)
    OP_8C(0x13, 270, 400)
    Sleep(500)
    OP_63(0x13)
    Sleep(1000)

    NpcTalk(    #299
        0x13,
        "Major Vander",
        (
            "#276F#5PJust where is this?\x02\x03",

            "And what happened to Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x109,
        (
            "#1063F#6PSo you were with the prince when you were\x01",
            "drawn in here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 400)
    Sleep(400)

    ChrTalk(    #301
        0x10E,
        (
            "#179F#6PAllow me to explain what we know of our\x01",
            "current situation.\x02\x03",

            "#170FIf you have any questions, I would be happy\x01",
            "to try and answer them.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -1200, 4000, -2700, 0)
    SetChrPos(0x10F, -260, 4000, -4170, 0)
    SetChrPos(0x107, 1080, 4000, -3810, 0)
    SetChrPos(0x10E, 270, 4000, -2000, 0)
    SetChrPos(0x13, 290, 4000, -190, 180)
    ClearChrFlags(0x13, 0x4)
    OP_6D(-780, 4000, -920, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #302
        0x13,
        "Major Vander",
        (
            "#272F#11PI see...\x02\x03",

            "#270FI must admit, all of this is a little much to take\x01",
            "in at once... I'm more tempted to think I'll wake\x01",
            "up any minute to find I've been dreaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x10E,
        (
            "#170F#6PI felt much the same at first, Major.\x02\x03",

            "I've been in here for a while now, and I still \x01",
            "find myself doubting all of this is even real. \x01",
            "I'm too hardheaded for my own good, I fear.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #304
        0x13,
        "Major Vander",
        (
            "#278F#11PThen we're similar in more ways than\x01",
            "one.\x02\x03",

            "#270FIn any case, we don't have the luxury\x01",
            "of time on our side.\x02\x03",

            "I'm concerned about that fool's safety,\x01",
            "so allow me to assist you with your\x01",
            "search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x109,
        (
            "#1075F#6PWe'd be happy to have you.\x02\x03",

            "#1063FIncidentally, before we get going...\x02\x03",

            "...what kind of situation were you in when\x01",
            "the light started surrounding you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #306
        0x13,
        "Major Vander",
        (
            "#272F#11PWell...the two of us were in Parm conducting an\x01",
            "inspection. Night arrived, and the two of us made\x01",
            "our way back to the hotel where we were staying.\x02\x03",

            "#270FThat was when it happened, and completely\x01",
            "without warning.\x02\x03",

            "I can't say for sure, but given that he was with me,\x01",
            "he may have been caught up in this as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x107,
        (
            "#060F#6PParm?\x02\x03",

            "That's the southernmost town in Erebonia,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #308
        0x13,
        "Major Vander",
        (
            "#277F#11PThat's right. It happens to be the closest\x01",
            "Erebonian town to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x10F,
        (
            "#1802F#6PSorry to interject, but may I ask something?\x02\x03",

            "Who is this 'Olivier' you keep referring to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x109,
        (
            "#1062F#5POh, he was another one of the guys who came\x01",
            "with us to that flying city, Prince Olivert.\x02\x03",

            "#1066FYou wouldn't think he was a prince if you met\x01",
            "him, though. He's real easygoing and fun to be\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #311
        0x13,
        "Major Vander",
        (
            "#274F#11PI'm not sure I could disagree any more with that\x01",
            "last part if I tried.\x02\x03",

            "He delights in living a life of excessive debauchery\x01",
            "and constantly exhausts those unfortunate enough to\x01",
            "be around him at every waking hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x10E,
        (
            "#179F#6PHaha... You know as well as I do that there's\x01",
            "more to him than that, of course.\x02\x03",

            "#171FWord of his exploits since returning to the\x01",
            "Empire has been reaching Liberl, Major.\x02\x03",

            "If they're to be believed, he's become quite\x01",
            "adored at high-class social gatherings.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #313
        0x13,
        "Major Vander",
        (
            "#277F#11PIt's true he's managed to avoid causing too much\x01",
            "of a stir by keeping up his usual act so far...\x02\x03",

            "...but who knows what kinds of rumors will start\x01",
            "spreading when he reveals his true colors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x107,
        "#067F#6PPffft...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x109,
        "#1840F#6PHeh. Well, keep hangin' in there, buddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x10F,
        "#1440F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x109, 135, 400)
    Sleep(300)

    ChrTalk(    #317
        0x109,
        "#1079F#5PSomething wrong, Ries?\x02",
    )

    CloseMessageWindow()

    def lambda_BE05():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BE05)
    Sleep(100)
    OP_8C(0x10E, 180, 400)

    ChrTalk(    #318
        0x10F,
        (
            "#1447F#6P...Nothing at all.\x02\x03",

            "#1443FIt's interesting how the people we've found so far\x01",
            "all seem to know one another.\x02\x03",

            "That can't be a simple coincidence. Perhaps only\x01",
            "people who meet that condition end up getting\x01",
            "surrounded by that white light and coming here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x107,
        "#064F#6PMaybe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x109,
        "#1063F#5PWell, the logic DOES add up.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #321
        0x13,
        "Major Vander",
        (
            "#272F#11PAt the very least, it appears to be linked to becoming\x01",
            "imprisoned in one of those stones you spoke of.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BFE9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BFE9)
    Sleep(100)

    def lambda_BFFC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BFFC)
    Sleep(100)
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    NpcTalk(    #322
        0x13,
        "Major Vander",
        (
            "#270F#11PYou'd mentioned before not finding sealing stones\x01",
            "containing any of the Arseille's crew or Grancelite\x01",
            "residents, correct?\x02\x03",

            "Despite encountering both the ship and the city\x01",
            "itself in an abnormal state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x10E,
        "#178F#6PThat's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x107,
        "#065F#6PI-I hadn't even thought of that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x109,
        (
            "#1065F#6PHmm...\x02\x03",

            "#1063FIt's good food for thought while we keep exploring.\x02\x03",

            "Right now, our focus needs to be finding out what\x01",
            "happened to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x10E,
        "#176F#6PIndeed.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #327
        0x13,
        "Major Vander",
        (
            "#277F#11PI'd like to accompany you, too, if at all possible.\x02\x03",

            "The fastest way for me to accept the situation\x01",
            "I'm in would be to experience it firsthand.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2708)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_3F(0x354, 1)
    OP_DB(0x0, 0xC)
    OP_A2(0x25D2)
    Call(6, 21)
    SetChrFlags(0x13, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x109, 1020, 4000, -2720, 0)
    SetChrPos(0x10F, -450, 4000, -2720, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3A7")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290, 4000, -190, 180)
    SetChrPos(0x10E, 1460, 4000, -4520, 0)
    SetChrPos(0x10D, -320, 4000, -4350, 0)
    Jump("loc_C436")

    label("loc_C3A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3F0")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290, 4000, -190, 180)
    SetChrPos(0x107, 1460, 4000, -4520, 0)
    SetChrPos(0x10D, -320, 4000, -4350, 0)
    Jump("loc_C436")

    label("loc_C3F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C436")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 290, 4000, -190, 180)
    SetChrPos(0x107, 1460, 4000, -4520, 0)
    SetChrPos(0x10E, -320, 4000, -4350, 0)

    label("loc_C436")

    OP_6D(-1420, 4000, -120, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_C4(0x0, 0x200)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #328
        (
            "\x07\x05From this point, it will be possible to switch members in\x01",
            "and out of the party from the garden.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(500)
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x3, 0x0, 16000, 16000, 0)
    OP_C6(0x3, 0x1, 250, 250, 0)
    OP_A3(0x1)
    OP_43(0x0, 0x0, 0x1, 0x24)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #329
        (
            "\x07\x05To do this, select the party icon displayed on the screen.\x01",
            "Members who aren't mandatory at that point in time can\x01",
            "be switched freely.\x02\x03",

            "It's also possible to view and change the equipment and\x01",
            "orbments of reserve members from the Camp Menu while\x01",
            "in the garden as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    OP_A2(0x1)
    Sleep(500)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    FadeToBright(300, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D5")

    ChrTalk(    #330
        0x11,
        "#560F#11PWell, take care, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x109,
        "#1060F#6PYou got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10F,
        (
            "#1447F#6PWe'll leave keeping an eye on things in the\x01",
            "garden to you.\x02\x03",

            "#1448FIf you ever find yourself in danger, don't try\x01",
            "and do anything dangerous, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x11,
        "#060F#11PAll right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5B")

    label("loc_C7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C94B")

    ChrTalk(    #334
        0x12,
        (
            "#178F#11PWell, I leave the exploration of the capital in\x01",
            "your hands.\x02\x03",

            "#176FIt might be best for me to take some time to\x01",
            "cool my head here and regain my composure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x107,
        "#063F#6POkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x109,
        (
            "#1065F#6PIf we find anything noteworthy, we'll let you\x01",
            "know right away.\x02\x03",

            "#1060FIn the meantime, we'll leave guarding this\x01",
            "garden to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x12,
        "#170F#11PUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5B")

    label("loc_C94B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5B")

    ChrTalk(    #338
        0x13,
        (
            "#278F#11PIn that case, I leave everything in your hands.\x02\x03",

            "#277FI'll be here standing by in case you require my\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x109,
        (
            "#1060F#6PThanks.\x02\x03",

            "If we find out anything about where the prince is,\x01",
            "we'll let you know right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x13,
        "#277F#11PThank you.\x02",
    )

    CloseMessageWindow()

    label("loc_CA5B")

    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAC5")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB2C")

    label("loc_CAC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAED")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB2C")

    label("loc_CAED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB15")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB2C")

    label("loc_CB15")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CB2C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB59")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC0")

    label("loc_CB59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB81")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC0")

    label("loc_CB81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBA9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CBC0")

    label("loc_CBA9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CBC0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBED")
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CC3A")

    label("loc_CBED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC15")
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CC3A")

    label("loc_CC15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3A")
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CC3A")

    Sleep(1000)

    def lambda_CC45():
        OP_6D(-700, 4000, -960, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_CC45)
    OP_8C(0x10F, 90, 400)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC90")

    ChrTalk(    #341
        0x10E,
        "#173F#6PWhat was that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCAD")

    label("loc_CC90")


    ChrTalk(    #342
        0x12,
        "#173F#11PWhat was that?\x02",
    )

    CloseMessageWindow()

    label("loc_CCAD")


    ChrTalk(    #343
        0x10F,
        "#1443F#5PKevin, was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x109,
        "#1065F#6PYep. It's our old pal the cube again.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x5, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #345
        "\x07\x0C\x18#2S#80WVisitors from afar...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #346
        "\x07\x0C\x18#2S#80WPossessors of the cube...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE20")

    ChrTalk(    #347
        0x107,
        "#064F#6PA woman's voice?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE3F")

    label("loc_CE20")


    ChrTalk(    #348
        0x11,
        "#064F#11PA woman's voice?\x02",
    )

    CloseMessageWindow()

    label("loc_CE3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE73")

    ChrTalk(    #349
        0x10D,
        "#270F#6PAnd who might she be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE97")

    label("loc_CE73")


    ChrTalk(    #350
        0x13,
        "#270F#11PAnd who might she be?\x02",
    )

    CloseMessageWindow()

    label("loc_CE97")


    ChrTalk(    #351
        0x109,
        (
            "#1841F#6PWish we knew.\x02\x03",

            "#1063FWhoever she is, it doesn't seem like she can\x01",
            "hear us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #352
        "\x07\x0C\x18#2S#80WYou seem to be gathering...strength well...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #353
        "\x07\x0C\x18#2S#80WI will unlock another of the cube's powers...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_22(0x15F, 0x0, 0x64)
    PlayEffect(0x5, 0x1, 0x109, 270, 1250, 100, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0xC9)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    OP_C6(0x3, 0x0, 467000, 305000, 0)
    OP_C6(0x3, 0x1, 1200, 1200, 0)
    Sleep(1500)
    OP_A3(0x1)
    OP_43(0x0, 0x0, 0x1, 0x24)
    Sleep(2000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #354
        "\x07\x05About Remote Abilities\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    AnonymousTalk(    #355
        (
            "\x07\x05In the cube menu, you can select a character not in the\x01",
            "active party to set as a support member.\x02\x03",

            "This support member will confer certain benefits on the\x01",
            "active party.\x02\x03",

            "Each character has a different set of benefits they can\x01",
            "provide, including raising stats, drop rates, and more.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x1)
    Sleep(500)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #356
        (
            "\x07\x0C\x18#2S#80WThe power of the malevolent one is...\x01",
            "much too great...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #357
        (
            "\x07\x0C\x18#2S#80WI pray that your bonds...will become a\x01",
            "great light that will let you prevail...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #358
        "\x07\x0C\x18#2S#80W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D311")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D369")

    label("loc_D311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D334")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D369")

    label("loc_D334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D357")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D369")

    label("loc_D357")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_D369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D38C")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D3E4")

    label("loc_D38C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3AF")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D3E4")

    label("loc_D3AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3D2")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D3E4")

    label("loc_D3D2")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_D3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D407")
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D44A")

    label("loc_D407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D42A")
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_D44A")

    label("loc_D42A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44A")
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_D44A")

    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0xF0)
    OP_63(0xF1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46F")
    OP_63(0x11)
    Jump("loc_D494")

    label("loc_D46F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D483")
    OP_63(0x12)
    Jump("loc_D494")

    label("loc_D483")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D494")
    OP_63(0x13)

    label("loc_D494")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D556")

    ChrTalk(    #359
        0x10D,
        (
            "#272F#6PI fear I may have underestimated just how bizarre\x01",
            "a situation this is.\x02\x03",

            "#277FRegardless, whoever she may be, it doesn't sound\x01",
            "as though she means us any harm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D603")

    label("loc_D556")


    ChrTalk(    #360
        0x13,
        (
            "#272F#11PI fear I may have underestimated just how bizarre\x01",
            "a situation this is.\x02\x03",

            "#277FRegardless, whoever she may be, it doesn't sound\x01",
            "as though she means us any harm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D603")


    ChrTalk(    #361
        0x10F,
        (
            "#1447F#5PIndeed. That Schwarzritter is clearly our enemy,\x01",
            "but the woman doesn't seem to be so far.\x02\x03",

            "#1443FThat said, I wouldn't place too much trust in her\x01",
            "just yet. We still don't know who she is.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0x109,
        (
            "#1075FWell, thanks to her, we've got a few neat\x01",
            "features on the cube to play around with.\x02\x03",

            "#1060FYou guys up for seeing how they work?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D77F():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D77F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D85E")
    SetChrFlags(0x11, 0x80)
    Jump("loc_D887")

    label("loc_D85E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D874")
    SetChrFlags(0x12, 0x80)
    Jump("loc_D887")

    label("loc_D874")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D887")
    SetChrFlags(0x13, 0x80)

    label("loc_D887")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C7(0x1, 0xFF, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_35_ACAB end

    def Function_36_D8B7(): pass

    label("Function_36_D8B7")

    OP_C6(0x3, 0x3, -1, 500, 0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    Sleep(500)

    label("loc_D8DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D91D")
    Sleep(200)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D906")
    Jump("loc_D91D")

    label("loc_D906")

    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    Jump("loc_D8DA")

    label("loc_D91D")

    Return()

    # Function_36_D8B7 end

    def Function_37_D91E(): pass

    label("Function_37_D91E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 1440, 4000, -3840, 0)
    SetChrPos(0x12, 600, 4000, -4670, 0)
    SetChrPos(0x13, -780, 4000, -4310, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_DA62():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_DA62)

    def lambda_DA7A():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DA7A)

    def lambda_DA92():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_DA92)

    def lambda_DAA2():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_DAA2)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_DB8B():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DB8B)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x11, 950, 4000, -3840, 0)
    SetChrPos(0x12, 100, 4000, -4500, 0)
    SetChrPos(0x13, -1280, 4000, -4810, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_DC62():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DC62)

    def lambda_DC7A():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DC7A)

    def lambda_DC92():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DC92)

    def lambda_DCA2():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_DCA2)

    def lambda_DCB2():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DCB2)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_DCDC():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DCDC)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4102   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_37_D91E end

    def Function_38_DDC8(): pass

    label("Function_38_DDC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2700A0, 0x2700A4, 0x13)
    OP_D2(0x27055A, 0x27055E, 0x14)
    OP_D2(0x27055B, 0x27055F, 0x15)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    SetChrPos(0x109, 560, 4000, -1440, 0)
    SetChrPos(0x10F, -120, 4000, -2690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 2000, 4000, -3090, 0)
    SetChrPos(0x12, 1530, 4000, -4170, 0)
    SetChrPos(0x13, 70, 4000, -4130, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 390, 8000, 2150, 180)
    SetChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 20)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x4)
    PlayEffect(0x3, 0x0, 0x14, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_DF4A():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DF4A)

    def lambda_DF62():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF62)

    def lambda_DF7A():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DF7A)

    def lambda_DF8A():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_DF8A)

    def lambda_DF9A():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_DF9A)
    WaitChrThread(0x14, 0x0)
    SetChrSubChip(0x14, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x3, 0x1, 0x14, 0, 600, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_E006():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_E006)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #363
        0x13,
        "#277F#6PHmm... So it's the girl, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x109,
        (
            "#1840F#6PSure looks like it. It was down to either her\x01",
            "or one of her brothers.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x14, 0, 600, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_E170():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_E170)
    OP_82(0x2, 0x2)
    WaitChrThread(0x14, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #365
        0x14,
        (
            "#413F#5PMm... Mm...\x02\x03",

            "#215FKyle? Don? What happened...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x14, 21)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x14, 0xFFFFFF38, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #366
        0x14,
        (
            "#213F#11P...Huh?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x13,
        "#277F#6PIt's been quite some time, young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x109,
        (
            "#1066F#6PHaha. That logo on your visor's your new\x01",
            "courier service, then?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #369
        0x14,
        (
            "#213F#11P...\x02\x03",

            "#413FWhat kinda dream IS this?\x02\x03",

            "#215FThis is so lame! If I have to dream about people\x01",
            "from Liberl, can't Joshua be in it?\x02\x03",

            "What do I care about some phony priest or that\x01",
            "military nut?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x13,
        "#278F#6PHeh. You're still so very charming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x109,
        (
            "#1068F#6PAnd I'll have you know my credentials are\x01",
            "toootally for real, thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x13, -670, 4000, -2950, 0)
    SetChrPos(0x11, 1670, 4000, -3420, 0)
    SetChrPos(0x12, 1140, 4000, -4560, 0)
    SetChrPos(0x10F, -320, 4000, -4620, 0)
    SetChrPos(0x14, 290, 4000, -190, 180)
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_6D(-1180, 4000, -360, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #372
        0x14,
        "#416F#11P#3SStop talking all this crap, already!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #373
        0x14,
        (
            "#214F#11PJust tell me where you've hidden my brothers\x01",
            "so I can go and rescue them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x109,
        (
            "#1068F#6P*sigh* How're we supposed to explain\x01",
            "anything if you won't listen to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x13,
        (
            "#272F#6PAll of us are trapped inside this strange place\x01",
            "just like you.\x02\x03",

            "#270FHow could we know where your brothers are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x14,
        (
            "#216F#11PA-And you expect me to just buy that hook,\x01",
            "line, and sinker?!\x02\x03",

            "#413FI mean, it doesn't take a genius to figure out\x01",
            "there's something weird going on.\x02\x03",

            "#212FBut it wasn't even that long ago that we were all\x01",
            "flying over Crossbell in the Bobcat together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x10F,
        (
            "#1443F#6PSo that was what you were doing when you\x01",
            "were surrounded by that white light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x14,
        (
            "#213F#11PYeah, that's right...\x02\x01",

            "#214F...Wait! How do you know about the light?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x12,
        (
            "#176F#6PSo your situation is nearly the same as my\x01",
            "own, then.\x02\x03",

            "#178FSave for the fact that you were in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x11,
        (
            "#064F#6PStill, Crossbell's not that far from Liberl on\x01",
            "the map, right?\x02\x03",

            "It's the state between Erebonia and Calvard,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x109,
        (
            "#1065F#5PThat's the one. If you took an international liner,\x01",
            "you could be there in about an hour.\x02\x03",

            "#1067FHmm... It's worth noting, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x14,
        (
            "#216F#11PHELLO?! I'm standing right here, guys!\x02\x03",

            "#416FActually, forget it! I'm going back to the Bobcat.\x02\x03",

            "#214FI've got no reason to hang around with you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x11,
        "#065F#6PI-I'm not sure that's a good idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x13,
        (
            "#272F#6PJust so you're aware, Grancel is no longer the\x01",
            "city you once knew.\x02\x03",

            "#270FThere's no telling when your ship will be overrun\x01",
            "by fiends.\x02\x03",

            "Are you still sure you want to try acting alone?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #385
        0x14,
        "#215F#11PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x109,
        (
            "#1065F#6PIf we can't change your mind, we'll at least escort\x01",
            "you back, but I wouldn't recommend it.\x02\x03",

            "#1060FNot until we've got a better idea what kind of\x01",
            "situation we're even in here.\x02\x03",

            "It's not like we've never worked together before,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x14,
        (
            "#215F#11P...\x02\x03",

            "#416FOkay. I get it.\x02\x03",

            "#212FMy head's practically spinning with all that's\x01",
            "going on, so I'm not so sure WHAT I should be\x01",
            "doing right now...\x02\x03",

            "...but I guess it wouldn't hurt to stick with you\x01",
            "until we find Kyle and Don.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x109,
        "#1840F#6PGood. We'd feel better if you did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x14,
        (
            "#214F#11PBut if you guys think I'm gonna owe you one,\x01",
            "you've got another thing coming!\x02\x03",

            "If I'm gonna stick around, I'm gonna be doing\x01",
            "my part. So any time you need something, I'm\x01",
            "your girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x13,
        (
            "#277F#6PA noble enough sentiment.\x02\x03",

            "Just make sure you don't end up holding us\x01",
            "back in your attempts to be of assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x14,
        "#216F#11PY-You mind your own business!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x11,
        "#067F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x10F,
        (
            "#1448F#5P(She seems to be more dutiful\x01",
            "than I was expecting.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x12,
        "#170F#6P(She's a good person at heart, really.)\x02",
    )

    CloseMessageWindow()

    def lambda_EF8A():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EF8A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x270F)
    OP_28(0x2C, 0x1, 0x40)
    OP_28(0x2C, 0x1, 0x80)
    OP_3F(0x355, 1)
    OP_DB(0x0, 0xA)
    OP_A2(0x25D0)
    Call(6, 19)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_38_DDC8 end

    def Function_39_F113(): pass

    label("Function_39_F113")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x260285, 0x26028A, 0x13)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 1910, 4000, -3310, 0)
    SetChrPos(0x12, 1190, 4000, -4940, 0)
    SetChrPos(0x13, -240, 4000, -4660, 0)
    SetChrPos(0x14, 1030, 4000, -3700, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_F26D():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_F26D)

    def lambda_F285():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_F285)

    def lambda_F29D():
        OP_6B(2210, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_F29D)

    def lambda_F2AD():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_F2AD)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 200, 5300, 0, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_F396():
        OP_8F(0xFE, 0xC8, 0x1770, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F396)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrPos(0x11, 1250, 4000, -3240, 0)
    SetChrPos(0x12, -100, 4000, -4900, 0)
    SetChrPos(0x13, -1280, 4000, -5010, 0)
    SetChrPos(0x14, 300, 4000, -3790, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10, 0, 6000, 1000, 0)

    def lambda_F47E():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F47E)

    def lambda_F496():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F496)

    def lambda_F4AE():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F4AE)

    def lambda_F4BE():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_F4BE)

    def lambda_F4CE():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F4CE)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_F4F8():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F4F8)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_39_F113 end

    SaveToFile()

Try(main)
