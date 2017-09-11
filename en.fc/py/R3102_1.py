from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3102_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1CD1",         # 03, 3
        "Function_4_24EF",         # 04, 4
        "Function_5_2504",         # 05, 5
        "Function_6_2519",         # 06, 6
        "Function_7_2561",         # 07, 7
        "Function_8_2576",         # 08, 8
        "Function_9_258B",         # 09, 9
        "Function_10_25A0",        # 0A, 10
        "Function_11_25E8",        # 0B, 11
        "Function_12_2630",        # 0C, 12
        "Function_13_2678",        # 0D, 13
        "Function_14_26BC",        # 0E, 14
        "Function_15_26FA",        # 0F, 15
        "Function_16_273F",        # 10, 16
        "Function_17_27CE",        # 11, 17
        "Function_18_27EA",        # 12, 18
        "Function_19_2810",        # 13, 19
        "Function_20_2836",        # 14, 20
        "Function_21_2852",        # 15, 21
        "Function_22_288F",        # 16, 22
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
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_6D(-19410, 40, -38900, 0)
    SetChrPos(0x101, -18990, 50, -38440, 180)
    SetChrPos(0x102, -20320, 20, -39060, 135)
    SetChrPos(0x107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    OP_6B(3000, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "Ugh... I'm guessing it's broken?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "Yeah, looks like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "This WOULD have to happen in\x01",
            "the middle of nowhere like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#501FHey, what happened?\x02\x03",

            "Looks like you're in a bit\x01",
            "of a pickle here...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_315")

    ChrTalk(    #4
        0x8,
        (
            "Hey, you're...wait...\x01",
            "Estelle and Joshua, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#000FGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#010FIt's good to see you again.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #7
        0x9,
        "You know these two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Yeah, they're fellow bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#010FWell, we're still in training.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jump("loc_499")

    label("loc_315")


    ChrTalk(    #10
        0x9,
        "What's up with you two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "Hmm? That emblem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "Might you two be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#006FYep. We're junior bracers.\x02\x03",

            "I'm Estelle, and he's--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#010FJoshua. It's nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "Hmm... You're awful young\x01",
            "to be bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Oh, I see. I've heard about\x01",
            "you two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "It's a pleasure to make your\x01",
            "acquaintance. I'm Wong, of\x01",
            "the Zeiss guild branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "Kilika told me about you.\x02",
    )

    CloseMessageWindow()

    label("loc_499")


    ChrTalk(    #19
        0x8,
        "So what brings you here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#000FWe're on an escort mission\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        (
            "#060FAh... Hi. I have to go to Elmo...\x02\x03",

            "So I asked Estelle and Joshua\x01",
            "if they'd come with me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(    #22
        0x9,
        (
            "Hey, now that I get a good look\x01",
            "at you... You're Tita, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "You on another errand for the\x01",
            "ol' prof? It must be tough,\x01",
            "being that guy's gopher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        "#067FHee hee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#000FSo...what happened here?\x02\x03",

            "You guys seem to be in\x01",
            "a bit of a jam...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #26
        0x8,
        "I'm afraid so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I was escorting this transport\x01",
            "vehicle to the Wolf Fort...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "...but we only got this\x01",
            "far before it broke down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "I think the problem's in\x01",
            "the orbal engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "It started rattling, and then\x01",
            "before we knew it...well, here\x01",
            "we were!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #31
        0x101,
        "#003FOh, man. That stinks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_93A")
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #32
        0x101,
        (
            "#002F...Wait a second...\x02\x03",

            "There's a request up on the\x01",
            "bulletin board about searching\x01",
            "for a haulage vehicle.\x02\x03",

            "Do you think that might have\x01",
            "been about Wong's transport job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#012FNo doubt about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Well, at least the guild knows\x01",
            "about us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        (
            "#063FHmmm... Yeah, but your\x01",
            "orbal engine's a wreck.\x02\x03",

            "Unless I miss my guess, you're\x01",
            "gonna have to replace all your\x01",
            "internal motivator orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_993")

    label("loc_93A")


    ChrTalk(    #36
        0x107,
        (
            "#063FThe engine's busted?\x02\x03",

            "All the internal motivator\x01",
            "orbments have to be replaced.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993")


    def lambda_999():
        TurnDirection(0x102, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_999)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #37
        0x101,
        "#004F#6PHuh...? You can't fix it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #38
        0x107,
        (
            "#063FThe core of an orbal engine\x01",
            "is a super-delicate machine.\x02\x03",

            "You'd need a professional\x01",
            "technician to give it that\x01",
            "kind of complete overhaul.\x02\x03",

            "It just can't be done\x01",
            "with simple tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#013FI understand.\x02\x03",

            "So, there's no way we'll\x01",
            "get it repaired outdoors.\x02\x03",

            "#012F...?!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 215, 400)
    Sleep(800)
    OP_21()
    OP_1D(0x56)

    def lambda_B1D():
        TurnDirection(0x8, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B1D)

    def lambda_B2B():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B2B)

    def lambda_B39():
        TurnDirection(0x9, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B39)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #40
        0x101,
        "#002FWh-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#012F...See for yourself...\x02",
    )

    CloseMessageWindow()

    def lambda_B8A():
        OP_6D(-27480, -30, -42850, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8A)

    def lambda_BA2():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_BA2)
    Sleep(700)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -26150, -50, -46240, 45)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    SetChrPos(0xB, -27650, 30, -47100, 45)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 8)
    SetChrPos(0xC, -28470, -90, -45180, 45)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)
    SetChrPos(0xD, -30510, -30, -44920, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, -29310, -90, -43270, 45)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 8)
    SetChrPos(0xF, -30380, 0, -46760, 45)
    OP_43(0xA, 0x1, 0x1, 0x4)
    OP_43(0xC, 0x1, 0x1, 0x6)
    OP_43(0xE, 0x1, 0x1, 0x8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C9C():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C9C)

    def lambda_CAA():
        OP_8C(0x101, 215, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CAA)
    Sleep(150)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CEB():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEB)

    def lambda_CF9():
        OP_8C(0x107, 215, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CF9)
    OP_43(0xB, 0x1, 0x1, 0x5)
    OP_43(0xD, 0x1, 0x1, 0x7)
    Sleep(100)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x107, 13)
    OP_43(0xF, 0x1, 0x1, 0x9)
    WaitChrThread(0xF, 0x1)

    def lambda_D3A():
        OP_6D(-21250, -20, -39110, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D3A)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(120)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)
    OP_94(0x1, 0x9, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #42
        0x9,
        "M-Monsters?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 8)
    SetChrPos(0x14, -22130, -40, -48120, 26)
    SetChrFlags(0x14, 0x4)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4A(0x14, 0)
    SetChrSubChip(0x14, 4)
    OP_96(0x14, 0xFFFFAC90, 0x7D0, 0xFFFF4F2A, 0x898, 0x1388)
    SetChrChipByIndex(0x14, 7)
    OP_4B(0x14, 0)

    def lambda_DF5():
        OP_6D(-19870, -30, -41930, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DF5)

    def lambda_E0D():
        OP_6C(180000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_E0D)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x14, 400)
    WaitChrThread(0x11, 0x2)

    ChrTalk(    #43
        0x101,
        "#005FWong! Look up!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x14, 400)
    SetChrChipByIndex(0x14, 8)
    OP_8E(0x14, 0xFFFFB17C, 0x7D0, 0xFFFF572C, 0x1B58, 0x0)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4A(0x14, 0)
    SetChrSubChip(0x14, 4)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_EBB():

        label("loc_EBB")

        TurnDirection(0x9, 0x14, 400)
        OP_48()
        Jump("loc_EBB")

    QueueWorkItem2(0x9, 1, lambda_EBB)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_ED1():
        OP_96(0x14, 0xFFFFB302, 0xFFFFFFD8, 0xFFFF5E52, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ED1)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_43(0x8, 0x1, 0x1, 0xD)
    Sleep(120)
    OP_44(0x14, 0xFF)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    PlayEffect(0x8, 0xFF, 0x14, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x14, 2)
    SetChrSubChip(0x14, 0)
    OP_8F(0x14, 0xFFFFB0F0, 0x320, 0xFFFF5BDC, 0x1F40, 0x0)
    PlayEffect(0x12, 0xFF, 0xFF, -20370, 800, -42730, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x14, -20240, 1000, -42020, 0)
    OP_51(0x14, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF15A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x14, 0x3, 0x1, 0xF)
    OP_43(0x14, 0x2, 0x1, 0x10)
    Sleep(400)
    OP_96(0xB, 0xFFFF98FE, 0xFFFFFFBA, 0xFFFF50D8, 0x1F4, 0xBB8)
    WaitChrThread(0x14, 0x2)
    WaitChrThread(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0x14, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #44
        0x9,
        "#1PWh-Whoa!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x8, 0xB, 400)
    OP_4B(0x8, 0)

    ChrTalk(    #45
        0x8,
        "#1PStay back, Bruno!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#1POkay!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_10A9():
        OP_8E(0x9, 0xFFFFC09A, 0xFFFFFFE2, 0xFFFF6640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10A9)

    def lambda_10C4():
        OP_6D(-15540, -50, -40250, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_10C4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -19100, -30, -50010, 43)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 8)
    SetChrPos(0x12, -19100, -30, -50010, 43)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 8)
    SetChrPos(0x13, -19100, -30, -50010, 43)
    OP_43(0x11, 0x1, 0x1, 0xA)
    Sleep(400)
    OP_43(0x12, 0x1, 0x1, 0xB)
    Sleep(400)
    OP_43(0x13, 0x1, 0x1, 0xC)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x12, 400)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    def lambda_1181():
        OP_6D(-19630, 60, -38120, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1181)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x9, 0xFFFFBBD6, 0x0, 0xFFFF6D66, 0xBB8, 0x0)
    TurnDirection(0x9, 0x12, 400)
    WaitChrThread(0x14, 0x1)

    ChrTalk(    #47
        0x9,
        "Crap! There's more of 'em!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1235():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1235)

    def lambda_1243():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1243)
    TurnDirection(0x8, 0x12, 400)

    ChrTalk(    #48
        0x8,
        "...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#012FWong, you handle the ones\x01",
            "back there.\x02\x03",

            "We'll take care of these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "A-All right!\x02",
    )

    CloseMessageWindow()

    def lambda_12C0():
        OP_8C(0xFE, 215, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12C0)
    OP_8C(0x107, 215, 400)

    ChrTalk(    #51
        0x101,
        (
            "#005FAll right! Let's show these\x01",
            "things who's boss!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0xB, 8)
    SetChrChipByIndex(0xC, 8)
    SetChrChipByIndex(0xD, 8)
    SetChrChipByIndex(0xE, 8)
    SetChrChipByIndex(0xF, 8)

    def lambda_133E():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_133E)

    def lambda_1354():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1354)

    def lambda_136A():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_136A)

    def lambda_1380():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1380)

    def lambda_1396():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1396)

    def lambda_13AC():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13AC)
    SetChrChipByIndex(0x8, 6)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x1000)
    OP_43(0x8, 0x1, 0x1, 0xE)
    WaitChrThread(0x8, 0x1)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x8, 0x1000)
    Battle(0x3F6, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_143B"),
        (SWITCH_DEFAULT, "loc_143E"),
    )


    label("loc_143B")

    OP_B4(0x0)
    Return()

    label("loc_143E")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_6D(-18050, 20, -37820, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x8, -17230, 10, -39580, 104)
    SetChrPos(0x9, -17250, 20, -36060, 199)
    SetChrPos(0x101, -18990, 50, -38440, 225)
    SetChrPos(0x102, -20320, 20, -39060, 225)
    SetChrPos(0x107, -19090, 50, -36910, 225)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x107, 13)
    SetChrChipByIndex(0x8, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(    #52
        0x101,
        "#002F#6PThat should be all of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#012FYeah, we got them.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 65535)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #54
        0x107,
        "#561FWhew... Thank goodness.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #55
        0x8,
        "Indeed. And no casualties.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)

    def lambda_15BF():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15BF)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #56
        0x9,
        (
            "Oh, man... My life flashed\x01",
            "in front of my eyes.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1609():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1609)

    def lambda_1617():
        OP_8C(0x107, 135, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1617)

    def lambda_1625():
        OP_6C(270000, 3500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1625)

    def lambda_1635():
        OP_6D(-18530, 50, -38340, 3500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1635)
    SetChrFlags(0x9, 0x40)
    OP_43(0x102, 0x1, 0x1, 0x11)
    OP_8E(0x9, 0xFFFFBB18, 0xA, 0xFFFF718A, 0x3E8, 0x0)
    OP_8E(0x9, 0xFFFFBE10, 0xFFFFFFF6, 0xFFFF6A32, 0x3E8, 0x0)
    TurnDirection(0x9, 0x102, 400)
    ClearChrFlags(0x9, 0x40)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)

    ChrTalk(    #57
        0x9,
        (
            "#6PNow... We're okay, but what\x01",
            "comes next?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #58
        0x8,
        "Good question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "I think our first priority\x01",
            "should be to get our vehicle\x01",
            "moving again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#003FBut we can't repair it, can we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x107,
        "#063FIt sure won't be easy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#012FWhich means that our only option\x01",
            "is to change out the parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "The manager of the transport\x01",
            "vehicles is Prometheus from\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "He'd probably know where we can\x01",
            "get the replacement parts we need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "But we'd have to go all the\x01",
            "way back to Zeiss for that...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #66
        0x8,
        (
            "Ugh... I just don't know.\x01",
            "What do you think, Bruno?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "Back to Zeiss, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #68
        0x9,
        (
            "It probably won't do any good,\x01",
            "but I want to try getting it\x01",
            "to start for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#6PIf it starts, we're golden.\x01",
            "If not, back to Zeiss we go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "That works...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "Gotta stick with it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        "You know me...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #73
        0x8,
        (
            "So, I guess that means that\x01",
            "we're going to try holding\x01",
            "out here for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#002FThat's fine...\x01",
            "Just be careful, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        "Don't worry about us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "If things start to look too risky,\x01",
            "we're heading straight back to town.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #77
        0x8,
        (
            "And you watch yourself on the\x01",
            "way to Elmo, okay, Tita?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #78
        0x107,
        "#060FI will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "If you get a chance, let Prometheus\x01",
            "know what's up, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "I'm pretty sure he's in the Central\x01",
            "Factory, third floor Design Room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#000FOkay...\x01",
            "We'll see you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#010FTake care.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #83
        "\x07\x00Quest \x07\x02[Haulage Vehicle Search] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x8, 0x1, 0x1, 0x12)
    OP_43(0x9, 0x1, 0x1, 0x13)
    Sleep(100)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x2)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_28(0x28, 0x1, 0x10)
    OP_28(0x28, 0x1, 0x20)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x2)
    EventEnd(0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Return()

    # Function_2_AC end

    def Function_3_1CD1(): pass

    label("Function_3_1CD1")

    EventBegin(0x0)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_6D(-19410, 40, -38900, 0)
    SetChrPos(0x101, -18990, 50, -38440, 180)
    SetChrPos(0x102, -20320, 20, -39060, 135)
    SetChrPos(0x107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    OP_6B(3000, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(    #84
        0x101,
        (
            "#000FHey...\x01",
            "How's it coming?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #85
        0x8,
        "Welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "I don't suppose you found us\x01",
            "a replacement engine, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#001FWe sure did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#010FSorry we took so long.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "Oh, really?\x01",
            "That's a huge relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "I tried everything I could think\x01",
            "of to get this thing started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "But it was all for nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "We were just about ready to\x01",
            "give up and return to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#000FReally? Well, we made it\x01",
            "just in time, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FLet's go ahead and get the\x01",
            "vehicle fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        (
            "#060FYeah.\x02\x03",

            "#061FWe'll have this orbal engine\x01",
            "swapped out in a flash.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #96
        0x8,
        "Go for it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(    #97
        0x9,
        "I'll help.\x02",
    )

    CloseMessageWindow()

    def lambda_1FBB():
        OP_8E(0x9, 0xFFFFB4A6, 0xFFFFFFE2, 0xFFFF5E98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1FBB)
    OP_43(0x8, 0x1, 0x1, 0x14)
    SetChrFlags(0x107, 0x40)
    OP_8E(0x107, 0xFFFFBAD2, 0x14, 0xFFFF6AC8, 0x5DC, 0x0)
    FadeToDark(1000, 0, -1)
    OP_8E(0x107, 0xFFFFB596, 0x1E, 0xFFFF606E, 0x5DC, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_0D()
    OP_6D(-18190, 10, -40240, 0)
    SetChrPos(0x107, -17490, 10, -39610, 182)
    SetChrPos(0x8, -19060, -10, -40450, 145)
    SetChrChipByIndex(0x9, 14)
    OP_6B(3000, 0)
    OP_6C(276000, 0)
    SetChrPos(0x10, -17420, -20, -41550, 51)
    SetChrFlags(0x10, 0x40)
    OP_A1(0x10, 0x0)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    Sleep(1)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrBattleFlags(0x9, 0x20)
    OP_89(0x9, -17120, 440, -41360, 51)
    SetChrFlags(0x9, 0x20)
    LoadEffect(0x0, "map\\\\mp024_00.eff")
    TurnDirection(0x101, 0x9, 0)
    Sleep(400)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #98
        0x107,
        "#060F#4P...And there we go.\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x107, 0xB4, 0x5DC, 0x7D0, 0x0)

    ChrTalk(    #99
        0x9,
        "Let's give her a whirl.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(400)
    OP_22(0xCF, 0x1, 0x55)

    ChrTalk(    #100
        0x107,
        (
            "#062F#4P...\x02\x03",

            "#060F#4P...Yep, she's good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "Nice. Now we can finally\x01",
            "get that cargo moved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "Your grandpa MUST have\x01",
            "trained you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "You're young enough to still\x01",
            "be going to Sunday school, but\x01",
            "you're amazing with machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        "#067F#4PHee hee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "Well, we're gonna get\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        "You guys be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#000F#4PWe will.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #108
        0x8,
        (
            "We'll talk again.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        "#010F#4PTake care.\x02",
    )

    CloseMessageWindow()

    def lambda_2301():

        label("loc_2301")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2301")

    QueueWorkItem2(0x0, 1, lambda_2301)

    def lambda_2312():

        label("loc_2312")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2312")

    QueueWorkItem2(0x1, 1, lambda_2312)

    def lambda_2323():

        label("loc_2323")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_2323")

    QueueWorkItem2(0x2, 1, lambda_2323)
    OP_8C(0x8, 51, 400)
    SetChrFlags(0x8, 0x40)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 40)
    OP_70(0x0, 0xC8)

    def lambda_2353():
        OP_6D(-14070, -40, -37570, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2353)
    OP_24(0xCF, 0x64)

    def lambda_236F():
        OP_94(0x1, 0x10, 0x0, 0x4650, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_236F)
    PlayEffect(0x0, 0x0, 0x10, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x10, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_8E(0x8, 0xFFFFBBAE, 0xA, 0xFFFF6546, 0x6A4, 0x0)
    OP_8C(0x8, 51, 0)

    def lambda_240A():
        OP_94(0x1, 0x8, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_240A)
    WaitChrThread(0x10, 0x3)
    Sleep(1000)

    def lambda_242A():
        OP_69(0x101, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_242A)
    OP_43(0x0, 0x3, 0x1, 0x16)
    WaitChrThread(0x10, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_72(0x0, 0x20)
    OP_3F(0x346, 1)
    OP_28(0x29, 0x1, 0x40)
    OP_28(0x29, 0x4, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_71(0x0, 0x4)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x0, 0x3)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x00Quest \x07\x02[Haulage Vehicle Repair] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_1CD1 end

    def Function_4_24EF(): pass

    label("Function_4_24EF")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_4_24EF end

    def Function_5_2504(): pass

    label("Function_5_2504")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_5_2504 end

    def Function_6_2519(): pass

    label("Function_6_2519")

    OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_4A(0xFE, 0)
    SetChrSubChip(0xFE, 4)
    OP_96(0xFE, 0xFFFF9F3E, 0x3C, 0xFFFF5D80, 0x320, 0x3E8)
    OP_4B(0xFE, 0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_6_2519 end

    def Function_7_2561(): pass

    label("Function_7_2561")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_7_2561 end

    def Function_8_2576(): pass

    label("Function_8_2576")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_8_2576 end

    def Function_9_258B(): pass

    label("Function_9_258B")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_9_258B end

    def Function_10_25A0(): pass

    label("Function_10_25A0")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_25BF():

        label("loc_25BF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_25BF")

    QueueWorkItem2(0xFE, 2, lambda_25BF)
    OP_8F(0xFE, 0xFFFFCA04, 0xFFFFFFD8, 0xFFFF6816, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_10_25A0 end

    def Function_11_25E8(): pass

    label("Function_11_25E8")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_2607():

        label("loc_2607")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2607")

    QueueWorkItem2(0xFE, 2, lambda_2607)
    OP_8F(0xFE, 0xFFFFC932, 0xFFFFFFA6, 0xFFFF5F2E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_11_25E8 end

    def Function_12_2630(): pass

    label("Function_12_2630")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_264F():

        label("loc_264F")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_264F")

    QueueWorkItem2(0xFE, 2, lambda_264F)
    OP_8F(0xFE, 0xFFFFC360, 0xFFFFFFC4, 0xFFFF5A2E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_12_2630 end

    def Function_13_2678(): pass

    label("Function_13_2678")

    OP_8C(0x8, 225, 0)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 11)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x3, 0xBB8)
    Sleep(200)
    OP_99(0x8, 0x4, 0x7, 0xBB8)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Return()

    # Function_13_2678 end

    def Function_14_26BC(): pass

    label("Function_14_26BC")

    OP_8E(0xFE, 0xFFFFBAD2, 0x1E, 0xFFFF65D2, 0x1388, 0x0)

    def lambda_26D6():

        label("loc_26D6")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26D6")

    QueueWorkItem2(0xFE, 2, lambda_26D6)
    OP_8F(0xFE, 0xFFFFC02C, 0xFFFFFFEC, 0xFFFF67DA, 0x1388, 0x0)
    OP_44(0xFE, 0x2)
    Return()

    # Function_14_26BC end

    def Function_15_26FA(): pass

    label("Function_15_26FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_273E")
    OP_8C(0xFE, 45, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 135, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 225, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 315, 1000)
    OP_8C(0xFE, 360, 1000)
    Jump("Function_15_26FA")

    label("loc_273E")

    Return()

    # Function_15_26FA end

    def Function_16_273F(): pass

    label("Function_16_273F")

    OP_8F(0x14, 0xFFFFA358, 0xC8, 0xFFFF5088, 0x1F40, 0x0)
    PlayEffect(0x12, 0xFF, 0xFF, -23720, 30, -44920, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x20B, 0x0, 0x5F)

    def lambda_2793():
        OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2793)
    OP_96(0x14, 0xFFFF9EA8, 0xC8, 0xFFFF5092, 0x1F4, 0xFA0)
    OP_96(0x14, 0xFFFF9AAC, 0xC8, 0xFFFF4D0E, 0x1F4, 0x7D0)
    Return()

    # Function_16_273F end

    def Function_17_27CE(): pass

    label("Function_17_27CE")

    OP_8E(0x102, 0xFFFFB2B2, 0x14, 0xFFFF65FA, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_17_27CE end

    def Function_18_27EA(): pass

    label("Function_18_27EA")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0x8, 0xFFFFB58C, 0xFFFFFFF6, 0xFFFF61FE, 0x7D0, 0x0)
    OP_8C(0x8, 145, 400)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_18_27EA end

    def Function_19_2810(): pass

    label("Function_19_2810")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0x9, 0xFFFFBBAE, 0xA, 0xFFFF6546, 0x7D0, 0x0)
    OP_8C(0x9, 182, 400)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_19_2810 end

    def Function_20_2836(): pass

    label("Function_20_2836")

    OP_8E(0x8, 0xFFFFAE34, 0xFFFFFFCE, 0xFFFF6334, 0xBB8, 0x0)
    OP_8C(0x8, 135, 400)
    Return()

    # Function_20_2836 end

    def Function_21_2852(): pass

    label("Function_21_2852")

    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    Return()

    # Function_21_2852 end

    def Function_22_288F(): pass

    label("Function_22_288F")

    Sleep(4000)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x37)
    Sleep(100)
    OP_23(0xCF)
    Return()

    # Function_22_288F end

    SaveToFile()

Try(main)
