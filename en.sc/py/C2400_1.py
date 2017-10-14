from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2400_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'C2400.x',
        MapIndex            = 97,
        MapDefaultBGM       = "ed60125",
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_CFB",          # 01, 1
        "Function_2_D04",          # 02, 2
        "Function_3_34CE",         # 03, 3
        "Function_4_5F28",         # 04, 4
        "Function_5_5FC4",         # 05, 5
        "Function_6_601E",         # 06, 6
        "Function_7_6032",         # 07, 7
        "Function_8_608E",         # 08, 8
        "Function_9_60EA",         # 09, 9
        "Function_10_6146",        # 0A, 10
        "Function_11_61A2",        # 0B, 11
        "Function_12_61F9",        # 0C, 12
        "Function_13_620F",        # 0D, 13
        "Function_14_6225",        # 0E, 14
        "Function_15_62A0",        # 0F, 15
        "Function_16_6336",        # 10, 16
        "Function_17_634B",        # 11, 17
        "Function_18_6360",        # 12, 18
        "Function_19_6375",        # 13, 19
        "Function_20_638A",        # 14, 20
        "Function_21_639F",        # 15, 21
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB")
    Call(1, 21)

    label("loc_BB")

    EventBegin(0x0)
    OP_6D(-170, 0, 490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -10, 0, 5410, 1)
    SetChrPos(0xF7, -10, 0, 5410, 1)
    SetChrPos(0x105, -10, 0, 5410, 1)
    SetChrPos(0x104, -10, 0, 5410, 1)
    SetChrPos(0x127, -10, 0, 5410, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, -320, 0, -8670, 7)
    FadeToDark(0, 0, -1)
    FadeToBright(2000, 0)

    def lambda_183():
        OP_8E(0x101, 0xFFFFFF56, 0x0, 0x1EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_183)
    Sleep(500)

    def lambda_1A3():
        OP_8E(0x105, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A3)
    Sleep(500)

    def lambda_1C3():
        OP_8E(0xF7, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1C3)

    def lambda_1DE():
        OP_8E(0x105, 0x2F8, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DE)
    Sleep(500)

    def lambda_1FE():
        OP_8E(0x104, 0xFFFFFF56, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FE)

    def lambda_219():
        OP_8E(0xF7, 0xFFFFFC2C, 0x0, 0x618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_219)
    Sleep(500)

    def lambda_239():
        OP_8E(0x127, 0xFFFFFF9C, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x127, 0, lambda_239)

    def lambda_254():
        OP_8E(0x104, 0x172, 0x0, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_254)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_295():
        OP_6D(0, 0, -3920, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_295)

    def lambda_2AD():
        OP_67(0, 7000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #0
        0x101,
        "#1020F#4PHuh?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30C")

    ChrTalk(    #1
        0x106,
        "#054F#7PAw, hell... Here we go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_32F")

    label("loc_30C")


    ChrTalk(    #2
        0x103,
        "#523F#7PThe enemy is upon us!\x02",
    )

    CloseMessageWindow()

    label("loc_32F")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_36B")
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Jump("loc_375")

    label("loc_36B")

    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)

    label("loc_375")

    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_0D()
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 30)
    SetChrSubChip(0x11, 0)

    def lambda_3A1():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3A1)
    Sleep(500)

    def lambda_3B6():
        OP_99(0xFE, 0x1, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3B6)

    def lambda_3C6():
        OP_8F(0xFE, 0xA, 0x0, 0xFFFFF7CC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3C6)

    def lambda_3E1():
        OP_6D(100, 0, -930, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E1)

    def lambda_3F9():
        OP_67(0, 6000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F9)
    Sleep(500)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrPos(0x101, -170, 0, 490, 180)
    SetChrPos(0x105, 760, 0, 700, 180)
    SetChrPos(0xF7, -980, 0, 1560, 180)
    SetChrPos(0x127, -100, 0, 3000, 180)
    SetChrPos(0x104, 370, 0, 1800, 180)
    SetChrFlags(0x11, 0x80)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x127, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #3
        0x101,
        (
            "#1007FPhew! That was a COUPLE pieces\x01",
            "of cake, I think...\x02\x03",

            "#1002FSo this place...is some kind of\x01",
            "underground ruin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#042FYes, it seems so... The architecture is similar\x01",
            "to buildings from the Middle Ages.\x02\x03",

            "I had no idea a place like this was\x01",
            "so close to the academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x104,
        (
            "#030F#6PHmm... The monsters in this place are as\x01",
            "thick as Hopper Chiefs in a wine cellar.\x02\x03",

            "#035FThis ruin must be the 'trial' mentioned\x01",
            "in the card, then.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6F2")
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    Jump("loc_6FC")

    label("loc_6F2")

    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)

    label("loc_6FC")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(    #6
        0x106,
        (
            "#053F#6PYeah... No way we can bring any unarmed\x01",
            "civvies with us any farther.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_761():

        label("loc_761")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_761")

    QueueWorkItem2(0xF7, 1, lambda_761)
    Sleep(400)

    ChrTalk(    #7
        0x106,
        "#050F#6PYo, camera girl.\x02",
    )

    CloseMessageWindow()

    def lambda_795():

        label("loc_795")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_795")

    QueueWorkItem2(0x101, 1, lambda_795)
    Sleep(100)

    def lambda_7AB():

        label("loc_7AB")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_7AB")

    QueueWorkItem2(0x105, 1, lambda_7AB)
    Sleep(100)

    def lambda_7C1():

        label("loc_7C1")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_7C1")

    QueueWorkItem2(0x104, 1, lambda_7C1)
    Sleep(100)
    TurnDirection(0x127, 0xF7, 400)

    ChrTalk(    #8
        0x127,
        "#153FHuh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        (
            "#050F#6PYou heard all that. This place is a\x01",
            "deathtrap for someone like you.\x02\x03",

            "Go back to that room we were\x01",
            "just in and wait for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17")

    label("loc_87D")


    ChrTalk(    #10
        0x103,
        (
            "#026F#6PYes... Bringing unarmed civilians in with\x01",
            "us would be exceptionally foolish...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DF():

        label("loc_8DF")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_8DF")

    QueueWorkItem2(0xF7, 1, lambda_8DF)
    Sleep(400)

    ChrTalk(    #11
        0x103,
        "#020F#6PHey, Dorothy?\x02",
    )

    CloseMessageWindow()

    def lambda_910():

        label("loc_910")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_910")

    QueueWorkItem2(0x101, 1, lambda_910)
    Sleep(100)

    def lambda_926():

        label("loc_926")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_926")

    QueueWorkItem2(0x105, 1, lambda_926)
    Sleep(100)

    def lambda_93C():

        label("loc_93C")

        TurnDirection(0xFE, 0x127, 400)
        OP_48()
        Jump("loc_93C")

    QueueWorkItem2(0x104, 1, lambda_93C)
    Sleep(100)
    TurnDirection(0x127, 0xF7, 400)

    ChrTalk(    #12
        0x127,
        "#153FHuh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#020F#6PYou were listening, right?\x01",
            "It'll be very dangerous ahead,\x01",
            "and I'd hate to see you get hurt.\x02\x03",

            "Would you mind waiting for us\x01",
            "in the room we just came through?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A17")


    ChrTalk(    #14
        0x127,
        (
            "#154FAwww, but but but...!\x02\x03",

            "I wanted to get some awesome\x01",
            "ghost pictuuuures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1006FHey, don't worry, Dorothy. We'll come\x01",
            "back if we find anything, okay?\x02\x03",

            "You can get your awesome pictures then.\x01",
            "Right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x127, 0x101, 400)

    ChrTalk(    #16
        0x127,
        (
            "#154FWelllll...if I gotta.\x02\x03",

            "Be careful, okay, guys?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x127, 0, 400)
    OP_8E(0x127, 0x0, 0x0, 0x1522, 0x7D0, 0x0)
    OP_9F(0x127, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x4, 0x8)
    RemoveParty(0x26, 0xFF)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_8C(0xF7, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(    #17
        0x106,
        (
            "#051F#3PAll right, let's move out.\x02\x03",

            "Keep an eye on the monsters.\x01",
            "They're tough mothers, so let's\x01",
            "only fight the ones we need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C87")

    label("loc_C00")


    ChrTalk(    #18
        0x103,
        (
            "#022F#3PWell, then, shall we?\x02\x03",

            "The monsters here are incredibly ferocious.\x01",
            "Let's proceed carefully and fight only when\x01",
            "necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C87")


    def lambda_C8D():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8D)

    def lambda_C9B():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C9B)

    def lambda_CA9():
        TurnDirection(0xFE, 0xF7, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CA9)
    Sleep(500)

    ChrTalk(    #19
        0x101,
        "#1005FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#042FOf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        "#031F#6PNaturally.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x122A)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_CFB(): pass

    label("Function_1_CFB")

    Call(1, 2)
    Call(1, 3)
    Return()

    # Function_1_CFB end

    def Function_2_D04(): pass

    label("Function_2_D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D15")
    Call(1, 21)

    label("loc_D15")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    SetChrPos(0x101, -262000, 0, 74000, 360)
    SetChrPos(0x105, -263500, 0, 73700, 360)
    SetChrPos(0xF7, -262000, 0, 72550, 360)
    SetChrPos(0x104, -264000, 0, 72550, 360)
    SetChrPos(0xF, -263000, 150, 90390, 9)
    OP_6D(-262870, 0, 73230, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    OP_20(0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1004FHey...!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x6F)

    def lambda_E12():
        OP_6D(-262290, 0, 87050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E12)

    def lambda_E2A():
        OP_67(0, 6810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E2A)

    def lambda_E42():
        OP_6B(1810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E42)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0x101, -262000, 0, 75500, 360)
    SetChrPos(0x105, -264000, 0, 75500, 360)
    SetChrPos(0xF7, -262000, 0, 74500, 360)
    SetChrPos(0x104, -264000, 0, 74500, 360)

    def lambda_EA0():
        OP_8E(0xFE, 0xFFFBFE9C, 0x0, 0x14A14, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA0)
    Sleep(300)

    def lambda_EC0():
        OP_8E(0xFE, 0xFFFBF8C0, 0x0, 0x14820, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EC0)
    Sleep(150)

    def lambda_EE0():
        OP_8E(0xFE, 0xFFFC0090, 0x0, 0x14438, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_EE0)
    Sleep(300)

    def lambda_F00():
        OP_8E(0xFE, 0xFFFBF8C0, 0x0, 0x142A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F00)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x104, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_FAA")

    ChrTalk(    #23
        0x106,
        (
            "#057F#2PHuh. Well, you've got a shadow,\x01",
            "so I'm guessing you ain't a ghost...\x02\x03",

            "So just who the hell are you?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103C")

    label("loc_FAA")


    ChrTalk(    #24
        0x103,
        (
            "#022F#2PHm. You have a shadow and are tangible,\x01",
            "so somehow I doubt you're a ghost.\x02\x03",

            "Perhaps you'd be so kind as\x01",
            "to introduce yourself, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103C")


    NpcTalk(    #25
        0xF,
        "Man",
        "#6PHahaha...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 400)

    NpcTalk(    #26
        0xF,
        "Masked Man",
        (
            "#230FWelcome, my guests, to my humble,\x01",
            "transient abode.\x02\x03",

            "I receive you with open arms.\x01",
            "Your host will not disappoint,\x01",
            "I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1020F#2PA...mask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#042F#2PHe's exactly as you and Polly\x01",
            "described him, Estelle.\x02\x03",

            "So, then. You are the 'ghost' who\x01",
            "has been disturbing Ruan?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0xF,
        "Masked Man",
        (
            "#231FIndeed I am...Princess Klaudia.\x02\x03",

            "It is the greatest pleasure to\x01",
            "meet you in person at last.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        "#1005F#2PHow do you know who Kloe is?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0xF,
        "Masked Man",
        (
            "#231FHa ha! My pet, there is nothing,\x01",
            "no item or secret, on this plane\x01",
            "or above...which I cannot take!\x02\x03",

            "Ah, but I am uncouth, and have not introduced\x01",
            "myself to my guests! Allow me, then...\x02",
        )
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS114._CH")
    OP_C6(0x0, 0x0, 100000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Masked Man")

    AnonymousTalk(    #32
        (
            "#230FI am Enforcer No. X... The mysterious,\x01",
            "gentlemanly Phantom Thief, Bleublanc!\x02\x03",

            "Ah... That is to say, the Enforcer No. X...\x01",
            "of the Society of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        "#1020F#2PO-OUROBOROS?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14CF")

    ChrTalk(    #34
        0x106,
        "#057F#2PAw, hell...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_14EA")

    label("loc_14CF")


    ChrTalk(    #35
        0x103,
        "#523F#2PThe society?!\x02",
    )

    CloseMessageWindow()

    label("loc_14EA")


    def lambda_14F0():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14F0)
    Sleep(50)

    def lambda_1510():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1510)
    Sleep(50)

    def lambda_1530():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1530)
    Sleep(50)

    def lambda_1550():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1550)
    WaitChrThread(0x104, 0x1)
    Sleep(500)

    ChrTalk(    #36
        0xF,
        (
            "#231F...Such murderous, withering glares!\x01",
            "I assure you, they are not necessary...today.\x02\x03",

            "I am merely here to perform a\x01",
            "simple, trivial experiment.\x02\x03",

            "Not even the slightest hair on my body\x01",
            "has any intention of conflict with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1002F#2PAn experiment?\x02",
    )

    CloseMessageWindow()

    def lambda_167A():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_167A)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    LoadEffect(0x0, "map\\\\mp044_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -263200, 1250, 92150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_83(0x0, 0x2)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x101,
        "#1020F#2PWait, that's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        (
            "#042F#2PThat's the Black Orbment Colonel Richard had!\x01",
            "The 'Gospel'...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x104,
        (
            "#032F#2PQuite. Except...unless my eyes deceive me,\x01",
            "that one is even larger than the last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "#230FInteresting... It is as he said, then.\x01",
            "You already know of these.\x02\x03",

            "The Gospel I hold is a new model,\x01",
            "developed for the purpose of\x01",
            "experiments such as this.\x02\x03",

            "It has proven quite the aid in my\x01",
            "tests over the past few days!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(    #42
        0x106,
        "#057F#2PTests? What tests?\x02",
    )

    CloseMessageWindow()
    Jump("loc_191B")

    label("loc_18E3")


    ChrTalk(    #43
        0x103,
        "#022F#2PTests... What are you doing here, exactly?\x02",
    )

    CloseMessageWindow()

    label("loc_191B")


    ChrTalk(    #44
        0xF,
        (
            "#231FWhat indeed! As they say...\x01",
            "a picture is worth a thousand words.\x02\x03",

            "Allow me to show you...in person!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)
    OP_8F(0xF, 0xFFFBFF64, 0x96, 0x16616, 0x7D0, 0x0)
    OP_8C(0xF, 264, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp088_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    ClearChrFlags(0x10, 0x1)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xAA, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -263000, 500, 89640, 180)
    OP_43(0x10, 0x1, 0x1, 0xC)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        "#1020F#2PThe ghost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x104,
        (
            "#030FNo, it seems to be a...projection,\x01",
            "of some sort, cast into the air using\x01",
            "that device.\x02\x03",

            "I've never heard of such a device\x01",
            "being invented.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 400)

    ChrTalk(    #47
        0xF,
        (
            "#230FNaturally not. This is a hologram projector\x01",
            "that we developed.\x02\x03",

            "Of course, the projector, on its own, can\x01",
            "cast images little farther than this, but...\x02\x03",

            "With the power of a Gospel, one\x01",
            "can do things such as...this!\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp045_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -263200, 850, 92150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_1C97():
        OP_6D(-262290, 0, 85000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C97)

    def lambda_1CAF():
        OP_67(0, 6280, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CAF)
    Sleep(900)
    Fade(500)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -263000, 500, 80000, 360)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_1D62():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D62)

    def lambda_1D70():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1D70)

    def lambda_1D7E():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D7E)

    def lambda_1D8C():
        TurnDirection(0xFE, 0x10, 600)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D8C)
    Sleep(600)

    ChrTalk(    #48
        0x105,
        "#044F#1PAaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1020F#6PHoly...!\x02",
    )

    CloseMessageWindow()

    def lambda_1DCA():

        label("loc_1DCA")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1DCA")

    QueueWorkItem2(0x101, 1, lambda_1DCA)

    def lambda_1DDB():

        label("loc_1DDB")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1DDB")

    QueueWorkItem2(0xF7, 1, lambda_1DDB)

    def lambda_1DEC():

        label("loc_1DEC")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1DEC")

    QueueWorkItem2(0x105, 1, lambda_1DEC)

    def lambda_1DFD():

        label("loc_1DFD")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1DFD")

    QueueWorkItem2(0x104, 1, lambda_1DFD)
    SetChrChipByIndex(0x10, 22)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x1, 0x1, 0xC)
    OP_97(0x10, 0xFFFBFD20, 0x144B0, 0xFFF6D840, 0x1B58, 0x1)
    OP_97(0x10, 0xFFFBFD20, 0x144B0, 0xFFFC7D90, 0x1388, 0x1)
    TurnDirection(0x10, 0xF, 0)
    OP_8F(0x10, 0xFFFBFCA8, 0x96, 0x15E28, 0x7D0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    SetChrChipByIndex(0x10, 23)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 180, 400)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0x90)
    Sleep(1000)
    Fade(1000)
    SetChrFlags(0x10, 0x80)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    def lambda_1EC3():
        OP_6D(-262290, 0, 87050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EC3)

    def lambda_1EDB():
        OP_67(0, 6810, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EDB)
    OP_8E(0xF, 0xFFFBFCA8, 0x96, 0x16116, 0x7D0, 0x0)
    OP_8C(0xF, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #50
        0xF,
        (
            "#230FWell. The concept is clear enough, I think.\x02\x03",

            "The good citizens of Ruan received\x01",
            "a once-in-a-lifetime performance!\x01",
            "They should be thrilled.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1FFD")

    ChrTalk(    #51
        0x106,
        (
            "#057F#2PTch...\x02\x03",

            "So this was all just a bunch of\x01",
            "bullcrap pranks, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205F")

    label("loc_1FFD")


    ChrTalk(    #52
        0x103,
        (
            "#022F#2PUnbelievable...\x02\x03",

            "This whole thing has been for the\x01",
            "purpose of creating a few pranks?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205F")


    ChrTalk(    #53
        0xF,
        (
            "#231FTut! Pranks! Such an insult to my performances!\x02\x03",

            "Hmph. 'Twas a gift of enjoyment and distraction to\x01",
            "a city suffering the stresses of a heated election!\x02\x03",

            "Can you not see the beauty of such a gift?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1007F#2POkay... I kind of get WHAT you're doing...\x01",
            "I think. But...\x02\x03",

            "#1005FTell me! WHY did you do all this?!\x01",
            "Why did you scare so many people?!\x02\x03",

            "What do you people...\x01",
            "What does Ouroboros have planned?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#230FAh, but it is not my place to speak the mind\x01",
            "and purpose of the Grandmaster. Forgive me.\x02\x03",

            "Why I myself am here, assisting in the\x01",
            "plan, however, is simple.\x02\x03",

            "I have come seeking an audience...\x01",
            "with you, Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        "#044F#2PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "#231FYour beautiful pride, which was on such\x01",
            "magnificent display when you brought\x01",
            "justice upon the old mayor...\x02\x03",

            "I agreed to participate in this plan...\x01",
            "to claim that beauty for my own.\x02\x03",

            "Oh, I have awaited this day on pins and needles\x01",
            "for months! You cannot imagine my joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        "#043F#2PWh-Wha...? I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F#2P'Justice upon'... You mean what\x01",
            "happened with Mayor Dalmore!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        (
            "#1020F#2PWait, how the hell do you know\x01",
            "about that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xF,
        (
            "#230FI was a fly on the wall for that little\x01",
            "event. Or perhaps a 'shadow'?\x02\x03",

            "Like...this, for example.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_253E():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_253E)

    def lambda_2556():
        OP_6B(1700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2556)
    Sleep(500)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xF, 360, 2000)
    SetChrChipByIndex(0xF, 12)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 270, 2000)
    OP_8C(0xF, 180, 2000)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_AD(0x2400C1, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #62
        0x105,
        "#043F#2PYou were in the Dalmore mansion...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E4")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Candelabrum Quest to Not Done\x01",      # 0
            "Set Candelabrum Quest to Done\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26CB"),
        (1, "loc_26D3"),
        (SWITCH_DEFAULT, "loc_26DB"),
    )


    label("loc_26CB")

    OP_28(0x57, 0x3, 0x10)
    Jump("loc_26DB")

    label("loc_26D3")

    OP_28(0x57, 0x4, 0x10)
    Jump("loc_26DB")

    label("loc_26DB")

    FadeToBright(300, 0)

    label("loc_26E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x57, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_281B")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x101,
        (
            "#1005F#2PWait a minute!\x02\x03",

            "That means YOU'RE 'Phantom Thief B,'\x01",
            "the guy who stole the candelabrum from\x01",
            "the mayor's mansion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        "#044F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        (
            "#6PHo ho! Only now do we realize this?\x01",
            "I expected better.\x02\x03",

            "I thought you would have realized\x01",
            "it when I left the first card.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281B")


    def lambda_2821():
        OP_6D(-262290, 0, 87050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2821)

    def lambda_2839():
        OP_6B(1810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2839)
    Sleep(500)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xF, 360, 2000)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 270, 2000)
    OP_8C(0xF, 180, 2000)
    SetChrSubChip(0xF, 0)
    Sleep(500)

    ChrTalk(    #66
        0xF,
        (
            "#230FA phantom thief is, in essence, a worshiper\x01",
            "of beauty. We chase it, we covet it. And that\x01",
            "which is prideful cannot help but captivate us.\x02\x03",

            "Princess, your pride...has stolen my heart.\x02\x03",

            "Indeed, you have stolen the heart of a\x01",
            "phantom thief!\x02\x03",

            "#233FAh, what sweet humiliation this is!\x02\x03",

            "My pet, how do you intend to atone\x01",
            "for such a slight upon me?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x105,
        "#043F#2PU-Umm, I...don't really...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A89")

    ChrTalk(    #68
        0x106,
        (
            "#552F#2PHe's so full of himself he's about to\x01",
            "fall over... Sounds familiar, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADF")

    label("loc_2A89")


    ChrTalk(    #69
        0x103,
        (
            "#027F#2PSuch perfect self-absorption...\x01",
            "Just like a certain someone I know, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADF")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #70
        0x104,
        "#5P#034FOh, I beg you, do not compare me to...that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1002F#2PSo you're an agent of Ouroboros...\x01",
            "You aren't what I was expecting, but...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x101,
        (
            "#1005F#2PIf you're going to try and hurt Kloe,\x01",
            "I'm DEFINITELY gonna stop you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#542F#1PEstelle...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D3D")
    OP_8C(0x106, 360, 400)
    TurnDirection(0x104, 0xF, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    OP_0D()

    ChrTalk(    #74
        0x106,
        (
            "#054F#2PRight. In accordance with the laws of the Bracer\x01",
            "Guild, you are hereby under arrest and charged\x01",
            "with intrusion, theft...and a bunch'a other junk.\x02\x03",

            "We got a whole lotta questions for you--that\x01",
            "Gospel being just the start. So come quietly,\x01",
            "or we break your teeth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E63")

    label("loc_2D3D")

    OP_8C(0x103, 360, 400)
    TurnDirection(0x104, 0xF, 400)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 14)
    SetChrSubChip(0x103, 0)
    OP_0D()

    ChrTalk(    #75
        0x103,
        (
            "#024F#2PWell. In accordance with the laws of the Bracer\x01",
            "Guild, you are hereby under arrest and charged\x01",
            "with intrusion and theft...among other charges.\x02\x03",

            "We have a number of questions for you--\x01",
            "including ones about the 'Gospel.'\x01",
            "Please, surrender quietly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E63")


    ChrTalk(    #76
        0xF,
        (
            "#231FTut. How boorish. Arrest? Me?\x02\x03",

            "While it would be invigorating to have a little\x01",
            "fracas, I did choose this place for a reason...\x02\x03",

            "I shall allow him to be your opponent, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F3B")

    ChrTalk(    #77
        0x106,
        "#052F#2PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F56")

    label("loc_2F3B")


    ChrTalk(    #78
        0x103,
        "#023F#2PWhat do you--\x02",
    )

    CloseMessageWindow()

    label("loc_2F56")

    Fade(250)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 32)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    def lambda_2F76():
        OP_6D(-262290, 0, 88050, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F76)

    def lambda_2F8E():
        OP_6B(1700, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F8E)
    WaitChrThread(0x101, 0x0)
    OP_99(0xF, 0x0, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_20(0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-256350, 0, 81990, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(90000, 0)
    OP_6E(326, 0)
    OP_0D()
    OP_22(0x85, 0x0, 0x64)

    def lambda_3003():

        label("loc_3003")

        OP_7C(0x0, 0x64, 0x12C, 0x64)
        OP_48()
        Jump("loc_3003")

    QueueWorkItem2(0xF, 3, lambda_3003)
    OP_0D()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -235000, 0, 82000, 270)
    OP_A1(0x12, 0x13)
    OP_CA(0x13, 0x2, 0x0)
    SetChrFlags(0x12, 0x1)
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_7E(0xFE0C, 0xF830, 0x0, 0x50, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_30A9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30A9)

    def lambda_30B7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_30B7)

    def lambda_30C5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30C5)

    def lambda_30D3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30D3)
    Sleep(500)

    ChrTalk(    #79
        0x101,
        "#1020F#5PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#032F#2PHmm... I would say I have a bad feeling,\x01",
            "but somehow, I feel it's too obvious...\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_6F(0x14, 0)
    OP_70(0x14, 0xF0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x14)
    OP_72(0x14, 0x8)
    OP_72(0x14, 0x20)
    OP_44(0xF, 0x3)
    OP_23(0x85)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    Sleep(1000)
    OP_1D(0x29)
    Sleep(1000)
    OP_43(0x12, 0x0, 0x1, 0x5)
    Sleep(3000)
    OP_43(0x12, 0x3, 0x1, 0x4)
    Sleep(1200)
    OP_44(0x12, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    OP_B0(0x13, 0x8)
    OP_22(0xEC, 0x0, 0x64)
    OP_6F(0x13, 21)
    OP_70(0x13, 0x28)
    Sleep(1500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_73(0x13)
    Sleep(1000)
    OP_71(0x13, 0x20)
    OP_B0(0x13, 0x8)
    OP_6F(0x13, 1)
    OP_70(0x13, 0x10)
    Fade(500)
    OP_6D(-261589, 0, 84500, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(1860, 0)
    OP_6C(56000, 0)
    OP_6E(513, 0)
    OP_0D()
    OP_DC()

    ChrTalk(    #81
        0x101,
        "#1020F#5PWhat the heck is THAT thing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        "#042F#5PSome kind of...armored...CENTAUR machine?!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #83
        0xF,
        (
            "#231F#6PQuite! It seems he was once the\x01",
            "guardian of this place.\x02\x03",

            "The poor chap was half-broken when I arrived.\x01",
            "I repaired him out of the kindness of my heart,\x01",
            "you see.\x02\x03",

            "Since he's here, I think he could serve\x01",
            "as a worthy opponent, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1005F#5PYou have to be kidding!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3427")

    ChrTalk(    #85
        0x106,
        "#054F#2PHere it comes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3450")

    label("loc_3427")


    ChrTalk(    #86
        0x103,
        "#024F#2PIt's coming! On your guard!\x02",
    )

    CloseMessageWindow()

    label("loc_3450")

    Sleep(500)
    Fade(500)
    OP_44(0x12, 0x0)
    OP_72(0x13, 0x20)
    OP_0D()

    def lambda_346A():
        OP_6D(-258000, 0, 85500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_346A)

    def lambda_3482():
        OP_6B(1960, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3482)
    OP_6F(0x13, 81)
    OP_70(0x13, 0x61)
    OP_22(0xEC, 0x0, 0x64)
    OP_73(0x13)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    Battle(0x44C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_34C8"),
        (SWITCH_DEFAULT, "loc_34CD"),
    )


    label("loc_34C8")

    OP_B4(0x0)
    Jump("loc_34CD")

    label("loc_34CD")

    Return()

    # Function_2_D04 end

    def Function_3_34CE(): pass

    label("Function_3_34CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    ClearMapFlags(0x1)
    OP_6F(0x13, 160)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x12, -256500, 0, 81800, 236)
    OP_A1(0x12, 0x13)
    OP_CA(0x13, 0x2, 0x0)
    OP_6F(0x14, 240)
    SetChrPos(0x101, -263320, 0, 84630, 90)
    SetChrPos(0x105, -264530, 0, 82930, 90)
    SetChrPos(0xF7, -261260, 0, 83690, 90)
    SetChrPos(0x104, -262340, 0, 82220, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -262320, 150, 91670, 180)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    SetChrFlags(0xF, 0x40)
    OP_6D(-259000, 0, 84070, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(1810, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #87
        0x101,
        "#1025F#5PPhew! We won...I think.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_36D5")

    ChrTalk(    #88
        0x106,
        "#053F#5PFeh... What a waste of time...\x02",
    )

    CloseMessageWindow()

    def lambda_3628():
        OP_6D(-261290, 0, 88550, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3628)

    def lambda_3640():
        OP_67(0, 6500, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3640)
    TurnDirection(0x106, 0xF, 400)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #89
        0x106,
        (
            "#054F#2PAll right, clown, your turn!\x01",
            "Hope you don't mind a few missing teeth!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C1")

    label("loc_36D5")


    ChrTalk(    #90
        0x103,
        "#026F#5PYes, that was...a bit of a struggle.\x02",
    )

    CloseMessageWindow()

    def lambda_370D():
        OP_6D(-261290, 0, 88550, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_370D)

    def lambda_3725():
        OP_67(0, 6500, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3725)
    TurnDirection(0x103, 0xF, 400)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #91
        0x103,
        (
            "#022F#2PNow, then.\x02\x03",

            "You are, I hope, prepared for the\x01",
            "consequences of what you've done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C1")


    ChrTalk(    #92
        0xF,
        (
            "#230F#6PReally now. Such a lack of elegance in\x01",
            "your fighting styles! I'd hoped for better.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF, 24)
    SetChrSubChip(0xF, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #93
        0xF,
        (
            "#231F#6PWell, if I must...let me show you\x01",
            "a proper example of elegance.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0xF, 0x0, 0x5, 0x9C4)

    ChrTalk(    #94
        0xF,
        "#234F#6PFLAMME!\x02",
    )

    CloseMessageWindow()

    def lambda_38B1():
        OP_6D(-257000, 0, 86750, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38B1)

    def lambda_38C9():
        OP_67(0, 3910, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38C9)

    def lambda_38E1():
        OP_6B(2410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38E1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_22(0x86, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    LoadEffect(0x1, "map\\\\mpfire5.eff")
    PlayEffect(0x1, 0x1, 0xFF, -256000, 2900, 86750, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, -256000, 2900, 77000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0xFD44, 0xFEE8, 0xFEC0, 0x96, 0x7D0)
    OP_8C(0x101, 71, 400)
    OP_8C(0x105, 71, 400)
    OP_8C(0xF7, 71, 400)
    OP_8C(0x104, 71, 400)

    ChrTalk(    #95
        0x101,
        "#1004F#5PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        "#044F#5PTh-The torches!\x02",
    )

    CloseMessageWindow()

    def lambda_39EE():
        OP_6D(-261290, 0, 88550, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39EE)

    def lambda_3A06():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A06)

    def lambda_3A1E():
        OP_6B(1810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A1E)
    SetChrSubChip(0xF, 0)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x105, 0xF, 400)
    TurnDirection(0xF7, 0xF, 400)
    TurnDirection(0x104, 0xF, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #97
        0xF,
        "#234F#6PAIGUILLE!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 6)
    OP_0D()
    OP_7D(0x0, 0xF, 0x32, 0x1F4)

    def lambda_3A8D():
        OP_6D(-262290, 0, 87550, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A8D)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3AAA():
        OP_96(0xFE, 0xFFFBF046, 0x0, 0x15A72, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3AAA)
    OP_43(0x15, 0x0, 0x1, 0x7)
    Sleep(100)
    OP_43(0x16, 0x0, 0x1, 0x8)
    Sleep(100)
    OP_43(0x17, 0x0, 0x1, 0x9)
    Sleep(100)
    OP_43(0x18, 0x0, 0x1, 0xA)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_7D(0x1, 0xF, 0x0, 0x0)

    def lambda_3B05():

        label("loc_3B05")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3B05")

    QueueWorkItem2(0x101, 1, lambda_3B05)

    def lambda_3B22():

        label("loc_3B22")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3B22")

    QueueWorkItem2(0xF7, 1, lambda_3B22)

    def lambda_3B3F():

        label("loc_3B3F")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3B3F")

    QueueWorkItem2(0x105, 1, lambda_3B3F)

    def lambda_3B5C():

        label("loc_3B5C")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3B5C")

    QueueWorkItem2(0x104, 1, lambda_3B5C)

    ChrTalk(    #98
        0x101,
        "#1020F#2PAgh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        "#043F#2PAuuugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x104,
        "#033F#2PNngh!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3BF7")

    ChrTalk(    #101
        0x106,
        (
            "#055F#2PThe f...\x01",
            "He did...somethin' to our shadows...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C2F")

    label("loc_3BF7")


    ChrTalk(    #102
        0x103,
        (
            "#523F#2PThis is...'shadow sewing'?!\x01",
            "Im-Impossible!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2F")

    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    SetChrSubChip(0xF, 7)
    Sleep(75)
    SetChrSubChip(0xF, 0)
    Sleep(75)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 0)
    Sleep(500)

    ChrTalk(    #103
        0xF,
        (
            "#231F#5PApologies, my guests, but I must ask that\x01",
            "you remain still from this point forward.\x02\x03",

            "You seemed surprised when Dalmore's\x01",
            "'treasure' did this. However...\x02\x03",

            "For we Enforcers, such abilities are\x01",
            "trivial. Even without such crutches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1020F#2PN-No...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3DA2")

    ChrTalk(    #105
        0x106,
        "#057F#2PDamn it... Didn't expect this...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DCA")

    label("loc_3DA2")


    ChrTalk(    #106
        0x103,
        "#522F#2PWe were...too careless...!\x02",
    )

    CloseMessageWindow()

    label("loc_3DCA")

    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    OP_22(0x197, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_3DFB():
        OP_6D(-262370, 0, 81630, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DFB)

    def lambda_3E13():
        OP_67(0, 7590, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E13)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    SetChrPos(0x13, -263400, 4000, 69400, 0)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_3E52():
        OP_6D(-262000, 0, 87800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E52)

    def lambda_3E6A():
        OP_67(0, 7590, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E6A)

    def lambda_3E82():
        OP_8E(0xFE, 0xFFFBF56E, 0x12C, 0x158E2, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3E82)
    Sleep(500)
    Sleep(300)
    OP_8C(0xF, 270, 0)
    SetChrSubChip(0xF, 6)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3EC0():
        OP_96(0xF, 0xFFFBFE92, 0x0, 0x15C0C, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3EC0)
    Sleep(200)
    OP_43(0x19, 0x0, 0x1, 0xB)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_7D(0x1, 0xF, 0x0, 0x0)
    WaitChrThread(0x13, 0x2)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x1)

    def lambda_3F0F():

        label("loc_3F0F")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_3F0F")

    QueueWorkItem2(0x13, 1, lambda_3F0F)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #107
        0x13,
        "#310F#4PScreee!\x02",
    )

    CloseMessageWindow()
    OP_44(0x13, 0x1)

    ChrTalk(    #108
        0x105,
        "#043F#2PSieg!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 7)
    Sleep(75)
    SetChrSubChip(0xF, 0)
    Sleep(75)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 0)

    ChrTalk(    #109
        0xF,
        (
            "#231F#4PAh, there you are, courageous little white knight.\x02\x03",

            "Your chivalrous bravery is admirable, but\x01",
            "I must ask you to remain still for a while.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    OP_0D()
    OP_8C(0xF, 225, 400)

    def lambda_4029():
        OP_8E(0xFE, 0xFFFBF4D8, 0x0, 0x14B90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4029)
    Sleep(300)

    def lambda_4049():
        OP_6D(-262900, 0, 84380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4049)

    def lambda_4061():
        OP_67(0, 6280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4061)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF, 0x1)
    OP_8C(0xF, 180, 400)

    ChrTalk(    #110
        0xF,
        (
            "#230F#3PAh, my Princess Klaudia, you are\x01",
            "now a prisoner...to my desires.\x02\x03",

            "Heh heh... How does it feel, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x105,
        (
            "#047F#2P...Do not think that this will break me.\x02\x03",

            "#042FEven if you bind my body, you\x01",
            "shall never enslave my heart.\x02\x03",

            "So long as I am myself, you\x01",
            "will never take me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xF,
        (
            "#231F#3PYes, YES! Those EYES!\x02\x03",

            "Those eyes that shine with such beautiful\x01",
            "pride, which say 'I will never break!'\x02\x03",

            "That shine is what I desire!\x01",
            "Ah, you are everything I hoped for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1005F#4PHey, cut the crap, okay?!\x02",
    )

    CloseMessageWindow()

    def lambda_428F():

        label("loc_428F")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_428F")

    QueueWorkItem2(0x101, 1, lambda_428F)
    TurnDirection(0x101, 0xF, 100)
    OP_44(0x101, 0x1)

    ChrTalk(    #114
        0x101,
        (
            "#1005F#4PCreepy mask dude!\x01",
            "GET THE HELL AWAY FROM KLOE!\x02",
        )
    )


    def lambda_42F3():

        label("loc_42F3")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_42F3")

    QueueWorkItem2(0xF7, 1, lambda_42F3)
    TurnDirection(0xF7, 0xF, 100)
    OP_44(0xF7, 0x1)

    def lambda_431B():

        label("loc_431B")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_431B")

    QueueWorkItem2(0x104, 1, lambda_431B)
    OP_8C(0x104, 323, 100)
    OP_44(0x104, 0x1)
    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #115
        0xF,
        (
            "#230F#3P'Creepy mask dude'? Really.\x01",
            "To not understand the beauty of this mask...\x02\x03",

            "You have a very dim understanding of\x01",
            "refinement, pet. I ask you, be silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x104,
        "#035F#4PHeh heh...\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 135, 400)

    ChrTalk(    #117
        0xF,
        "#232F#3PHmm?\x02",
    )

    CloseMessageWindow()

    def lambda_443B():
        OP_6D(-262000, 0, 83690, 1500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_443B)

    def lambda_4453():
        OP_67(0, 6280, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4453)

    def lambda_446B():
        OP_6C(92000, 1500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_446B)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)

    ChrTalk(    #118
        0x104,
        (
            "#031F#4PAh, my apologies.\x02\x03",

            "#030FYou've simply made a very crude mistake.\x02\x03",

            "I'm afraid I couldn't help but\x01",
            "give an innocent chuckle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xF,
        (
            "#232F#5POh? This should be amusing, in the way\x01",
            "watching a pig wallow in mud is captivating.\x02\x03",

            "And what, exactly, is my mistake, 'bard'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x104,
        (
            "#030F#4PI certainly wouldn't deny Klaudia's\x01",
            "beauty--not even for a moment.\x02\x03",

            "Her beauty, however, extends far\x01",
            "beyond the estimation your frail,\x01",
            "tasteless aesthetic provides.\x02\x03",

            "#035FYou may approach her again when\x01",
            "you have learned the first thing about\x01",
            "beauty, jester of the 'Grandmaster.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xF,
        (
            "#235F#5PWhat?! Your words are bold in\x01",
            "the face of death, Erebonian!\x02\x03",

            "But what gives vagabond musician\x01",
            "scum such as yourself any right to\x01",
            "insult my sense of beauty?!\x02\x03",

            "Choose your next words carefully,\x01",
            "for they will determine your fate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x104,
        (
            "#035F#4PHm. Then I shall phrase them as a question.\x02\x03",

            "#030FWhat IS beauty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xF,
        (
            "#231F#5PTut, tut. You disappoint. I expected\x01",
            "more than such foolishness.\x02\x03",

            "Beauty is pride!\x01",
            "A distant light gleaming far above mortal cares!\x02\x03",

            "Indeed, can any other answer\x01",
            "even be allowed? I think not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x104,
        "#035F#4PReally. I can't even laugh at such an answer...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #125
        0x104,
        (
            "#530F#4P#3STrue beauty, Bleublanc of Ouroboros...\x01",
            "is love!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #126
        0xF,
        "#233F#5P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x104,
        (
            "#035F#4PBeauty only EXISTS because people\x01",
            "are brave enough to love!\x02\x03",

            "And without love, without the bonds of affection\x01",
            "and camaraderie that bind us together...\x01",
            "beauty is naught but a hollow illusion!\x02\x03",

            "#030FThe prideful and the humble...\x01",
            "both shine as a diamond in love!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xF,
        (
            "#235F#5PBah! How childish!\x02\x03",

            "#234FLOVE is the hollow illusion,\x01",
            "you cloddish jongleur!\x02\x03",

            "Beauty is an absolute! Its existence\x01",
            "does not depend on transient human\x01",
            "emotions!\x02\x03",

            "Yes, just as the flower that blooms on\x01",
            "the highest mountain, unseen by man,\x01",
            "remains beautiful in anonymity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x104,
        "#032F#4P...Hmm.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0x105)

    ChrTalk(    #130
        0x101,
        "#1019F#6PUh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4C9A")

    ChrTalk(    #131
        0x106,
        (
            "#551F#4PI've never been forced to listen to a more\x01",
            "brain-rottingly stupid conversation in my life...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D07")

    label("loc_4C9A")


    ChrTalk(    #132
        0x103,
        (
            "#025F#4P*sigh* 'Cloddish jongleur,' indeed.\x01",
            "Well, so much for the raw terror\x01",
            "and suspense, at any rate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D07")


    ChrTalk(    #133
        0x105,
        (
            "#045F#2PI, uh, um, I'm not quite sure\x01",
            "what to say to all this...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #134
        0xF,
        (
            "#230F#5P...Never would I have expected\x01",
            "to find a proper rival in the ways\x01",
            "of beauty among such ruin.\x02\x03",

            "Musician, give me your name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x104,
        (
            "#031F#4POlivier Lenheim.\x02\x03",

            "A wandering bard and hunter of love,\x01",
            "roaming to and fro in search of its\x01",
            "perfect manifestation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xF,
        (
            "#231F#5POlivier Lenheim... Hmm.\x01",
            "I shall remember that name.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -263660, 0, 73660, 339)
    OP_4A(0xE, 255)
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    NpcTalk(    #137
        0xE,
        "Girl's Voice",
        "#1PAaaah! Heeey, I finally found you guys!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xF, 0xE, 400)

    def lambda_4F94():
        OP_8E(0xFE, 0xFFFBF4BA, 0x0, 0x139C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4F94)

    def lambda_4FAF():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_4FAF)

    def lambda_4FBF():
        OP_6D(-263200, 0, 82600, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4FBF)

    def lambda_4FD7():
        OP_67(0, 6280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4FD7)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xE, 0x3)

    ChrTalk(    #138
        0xE,
        (
            "#150F#2PHeehee! Sorry, I know you said to\x01",
            "wait, but you guys were soooo late,\x01",
            "I couldn't wait anymore! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1020F#6PD-Dorothy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        (
            "#042F#6POh, no! DOROTHY!\x01",
            "RUN AWAY! PLEASE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xE,
        "#154F#2PHuh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0xE,
        (
            "#153F#2PHeeey! A masked man in white clothes!\x02\x03",

            "You're the ghost, aren'cha?!\x01",
            "You are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xF,
        "#233F#6PWhat, ah, well...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xE, 25)
    SetChrSubChip(0xE, 0)
    OP_0D()

    ChrTalk(    #144
        0xE,
        "#151F#2POkay, say cheeeeeeeese! ♪\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xE, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    OP_C4(0x1, 0x2)
    OP_7E(0xFD44, 0xFBB4, 0x64, 0x96, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x13, 0x1)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    FadeToBright(200, 16777215)

    ChrTalk(    #145
        0xF,
        "#235F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 10)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x13, 0x40)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    ChrTalk(    #146
        0x13,
        "#311F#3PScreee!\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x1, 0x1, 0xF)
    OP_8C(0x101, 315, 400)
    Sleep(300)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #147
        0x101,
        "#1004F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x105,
        "#542F#6PI can move again!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0xE, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_52EB")

    ChrTalk(    #149
        0x106,
        "#051F#6PWell, hey. The flash bulb wiped our shadows!\x02",
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_52EB")


    ChrTalk(    #150
        0x103,
        (
            "#021F#6POf course! The flash bulb wiped\x01",
            "our shadows clean!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_532B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_533A")
    SetChrChipByIndex(0x106, 15)
    Jump("loc_533F")

    label("loc_533A")

    SetChrChipByIndex(0x103, 14)

    label("loc_533F")

    SetChrChipByIndex(0x104, 16)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x104, 0xE, 400)

    ChrTalk(    #151
        0x104,
        (
            "#031F#4PAh, what an astounding girl! Photography and\x01",
            "perfectly-timed heroism, all in one package!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 400)

    ChrTalk(    #152
        0xE,
        (
            "#151F#5PHeehee! Leave it to meee! ♪\x02\x03",

            "Even though I dunno what I, uh, did...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #153
        0xF,
        (
            "#231FHa. Haha...\x02\x03",

            "HAAAhahahaha!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5441():
        OP_6D(-262490, 0, 88500, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5441)

    def lambda_5459():
        OP_67(0, 6810, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5459)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xF, 0xFFFBFCA8, 0x96, 0x16120, 0x1F4, 0x1388)
    OP_7D(0x1, 0xF, 0x0, 0x0)

    def lambda_549D():
        TurnDirection(0x101, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_549D)

    def lambda_54AB():
        TurnDirection(0xF7, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_54AB)

    def lambda_54B9():
        TurnDirection(0x104, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54B9)

    def lambda_54C7():
        TurnDirection(0xE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54C7)

    def lambda_54D5():
        TurnDirection(0x105, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54D5)
    WaitChrThread(0x101, 0x2)
    OP_8C(0xF, 225, 400)

    def lambda_54EF():
        OP_8F(0xF, 0xFFFBFEC4, 0x96, 0x16648, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_54EF)
    WaitChrThread(0xF, 0x1)
    OP_8C(0xF, 270, 400)
    OP_22(0x82, 0x0, 0x64)
    OP_71(0x15, 0x4)
    Sleep(500)

    ChrTalk(    #154
        0x101,
        "#1005F#2PCrap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x105,
        "#043F#2PThe Gospel!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x20)
    OP_8C(0xF, 180, 400)

    ChrTalk(    #156
        0xF,
        (
            "#231F#6PAh, it has been an age since\x01",
            "I have been entertained so!\x02\x03",

            "You have my thanks, my guests.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_55FE")

    ChrTalk(    #157
        0x106,
        (
            "#057F#2PYou son of...\x01",
            "What're you gonna do now?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5631")

    label("loc_55FE")


    ChrTalk(    #158
        0x103,
        "#022F#2PYou... What else do you intend to do?\x02",
    )

    CloseMessageWindow()

    label("loc_5631")


    ChrTalk(    #159
        0xF,
        (
            "#230F#6PI am going to end our revelry for tonight.\x01",
            "Forgive me if I seem an ungracious host.\x02\x03",

            "It appears, however, that I must take\x01",
            "stock of my assumptions about you.\x02\x03",

            "I can see now why the Black Fang takes\x01",
            "such an interest in you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x101,
        "#1020F#2PThe Black Fang...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        "#043F#2PYou... You mean Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xF,
        (
            "#231F#6PWe are old acquaintances, in a sense.\x02\x03",

            "The reason you came to my attention at all\x01",
            "was because I noticed that shock of black\x01",
            "hair and those amber eyes with you.\x02\x03",

            "Though his memories have returned to\x01",
            "the stage of his mind. I do wonder where\x01",
            "he's rehearsing...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 24)
    SetChrSubChip(0xF, 0)
    OP_0D()
    OP_99(0xF, 0x0, 0x5, 0x9C4)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    PlayEffect(0x0, 0x0, 0xF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0x101,
        "#1020F#2PAaah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5937")

    ChrTalk(    #164
        0x106,
        "#055F#2PThe hell was...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_594B")

    label("loc_5937")


    ChrTalk(    #165
        0x103,
        "#023F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    label("loc_594B")


    def lambda_5951():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_5951)
    Sleep(1500)
    OP_82(0x0, 0x2)
    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Bleublanc's Voice")

    AnonymousTalk(    #166
        (
            "\x07\x05I must now take my leave, my guests.\x02\x03",

            "The true plan has but started... I would\x01",
            "gird yourselves for long labors and suffering\x01",
            "ahead, if you intend to oppose us further.\x02\x03",

            "And I do intend to keep our little game going\x01",
            "on the side...\x02\x03",

            "Till next we meet!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x80)
    OP_20(0xBB8)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_43(0x13, 0x1, 0x1, 0xD)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_5B31():
        OP_8F(0x13, 0xFFFBF988, 0x708, 0x14370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_5B31)
    OP_0D()
    Sleep(500)
    OP_43(0x101, 0x1, 0x1, 0x10)
    Sleep(200)
    OP_43(0x13, 0x2, 0x1, 0xE)

    def lambda_5B65():
        OP_6D(-262500, 150, 91000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5B65)

    def lambda_5B7D():
        OP_67(0, 6280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5B7D)
    OP_43(0xF7, 0x1, 0x1, 0x11)
    OP_43(0x105, 0x1, 0x1, 0x12)
    Sleep(200)
    OP_43(0x104, 0x1, 0x1, 0x13)
    Sleep(100)
    OP_43(0xE, 0x1, 0x1, 0x14)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xE, 0x3)

    ChrTalk(    #167
        0x101,
        "#1020F#1PHe's gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        "#043F#5PI-I still can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xE,
        "#153FWowee! It's like a magic trick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x104,
        (
            "#031F#5PHaha! Most impressive!\x02\x03",

            "I suppose it behooves me to take him\x01",
            "as my rival.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #171
        0x101,
        (
            "#1005F#1POkay, we are SO beyond worrying\x01",
            "about rivals, here!\x02\x03",

            "He may look like some pervo ballroom freak,\x01",
            "but that power of his is NOT normal!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5DBD")

    ChrTalk(    #172
        0x106,
        "#053F#2PYeah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    OP_8C(0x105, 201, 400)

    ChrTalk(    #173
        0x106,
        (
            "#057F#2POuroboros... Wasn't just that Lorence punk,\x01",
            "then. They're all way stronger than I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4B")

    label("loc_5DBD")


    ChrTalk(    #174
        0x103,
        "#026F#2PIndeed...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    OP_8C(0x105, 201, 400)

    ChrTalk(    #175
        0x103,
        (
            "#022F#2POuroboros... Lorence isn't an exception, then.\x01",
            "All the 'Enforcers' must be that powerful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4B")

    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #176
        (
            "\x07\x05And so, the 'ghost incidents' that had\x01",
            "so stirred Ruan came to an end.\x02\x03",

            "The next morning, Estelle and the gang parted\x01",
            "with Dorothy and returned to the guild.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_3_34CE end

    def Function_4_5F28(): pass

    label("Function_4_5F28")


    def lambda_5F2E():
        OP_96(0xFE, 0xFFFBEE98, 0x0, 0x13EC0, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F2E)
    Sleep(100)

    def lambda_5F51():
        OP_96(0xFE, 0xFFFBF15E, 0x0, 0x14636, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F51)
    Sleep(100)

    def lambda_5F74():
        OP_96(0xFE, 0xFFFBF69A, 0x0, 0x13E2A, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5F74)
    Sleep(100)

    def lambda_5F97():
        OP_96(0xFE, 0xFFFBF744, 0x0, 0x14410, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F97)
    SetChrChipByIndex(0x105, 17)
    SetChrChipByIndex(0x104, 16)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    Return()

    # Function_4_5F28 end

    def Function_5_5FC4(): pass

    label("Function_5_5FC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_601D")
    OP_24(0xEC, 0x32)
    OP_B0(0x13, 0xD)
    OP_6F(0x13, 251)
    OP_70(0x13, 0x10A)

    def lambda_5FE9():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5FE9)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_73(0x13)
    Jump("Function_5_5FC4")

    label("loc_601D")

    Return()

    # Function_5_5FC4 end

    def Function_6_601E(): pass

    label("Function_6_601E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6031")
    OP_6F(0x14, 240)
    Jump("Function_6_601E")

    label("loc_6031")

    Return()

    # Function_6_601E end

    def Function_7_6032(): pass

    label("Function_7_6032")

    SetChrPos(0x15, -264690, 500, 90200, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_605D():
        OP_8F(0x15, 0xFFFBF47E, 0xFFFFFDA8, 0x14802, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_605D)
    WaitChrThread(0x15, 0x1)
    SetChrPos(0x15, -265090, 0, 83870, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_7_6032 end

    def Function_8_608E(): pass

    label("Function_8_608E")

    SetChrPos(0x16, -264690, 500, 90200, 270)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_60B9():
        OP_8F(0x16, 0xFFFBF096, 0xFFFFFDA8, 0x14262, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_60B9)
    WaitChrThread(0x16, 0x1)
    SetChrPos(0x16, -266090, 0, 82430, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_8_608E end

    def Function_9_60EA(): pass

    label("Function_9_60EA")

    SetChrPos(0x17, -264690, 500, 90200, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_6115():
        OP_8F(0x17, 0xFFFBFE9C, 0xFFFFFDA8, 0x145C8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6115)
    WaitChrThread(0x17, 0x1)
    SetChrPos(0x17, -262500, 0, 83300, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_9_60EA end

    def Function_10_6146(): pass

    label("Function_10_6146")

    SetChrPos(0x18, -264690, 500, 90200, 270)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_6171():
        OP_8F(0x18, 0xFFFBF8C0, 0xFFFFFDA8, 0x13F88, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6171)
    WaitChrThread(0x18, 0x1)
    SetChrPos(0x18, -264000, 0, 81700, 270)
    SetChrSubChip(0xFE, 2)
    Return()

    # Function_10_6146 end

    def Function_11_61A2(): pass

    label("Function_11_61A2")

    SetChrPos(0x19, -263960, 500, 87940, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x4)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_61C8():
        OP_8F(0x19, 0xFFFBEBDC, 0xFFFFFDA8, 0x153D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_61C8)
    WaitChrThread(0x19, 0x1)
    SetChrPos(0x19, -267400, 0, 86950, 0)
    SetChrSubChip(0xFE, 1)
    Return()

    # Function_11_61A2 end

    def Function_12_61F9(): pass

    label("Function_12_61F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_620E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_12_61F9")

    label("loc_620E")

    Return()

    # Function_12_61F9 end

    def Function_13_620F(): pass

    label("Function_13_620F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6224")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_13_620F")

    label("loc_6224")

    Return()

    # Function_13_620F end

    def Function_14_6225(): pass

    label("Function_14_6225")

    OP_8C(0x13, 332, 400)
    OP_97(0x13, 0xFFFBF6CC, 0x1575C, 0xFFFE0430, 0x1770, 0x1)
    OP_8F(0x13, 0xFFFC01BC, 0x708, 0x16C74, 0x7D0, 0x0)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 270, 400)
    OP_8F(0x13, 0xFFFC01BC, 0x6C2, 0x16C74, 0x3E8, 0x0)
    OP_44(0x13, 0x1)
    Sleep(250)
    SetChrPos(0x13, -261700, 1780, 93300, 270)
    SetChrChipByIndex(0x13, 29)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Return()

    # Function_14_6225 end

    def Function_15_62A0(): pass

    label("Function_15_62A0")

    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)
    OP_8F(0x13, 0xFFFBFCA8, 0x44C, 0x16120, 0xBB8, 0x0)
    OP_8C(0x13, 263, 400)

    def lambda_62CB():
        OP_97(0x13, 0xFFFBF5E6, 0x151E4, 0xFFFC2F70, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_62CB)
    WaitChrThread(0x13, 0x3)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 20)
    OP_8C(0x13, 0, 400)
    OP_8C(0x105, 90, 400)
    SetChrChipByIndex(0x105, 21)
    SetChrSubChip(0x105, 2)
    OP_8F(0x13, 0xFFFBF9EC, 0x64, 0x14438, 0x7D0, 0x0)
    Fade(500)
    OP_44(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x105, 21)
    SetChrSubChip(0x105, 0)
    OP_0D()
    Return()

    # Function_15_62A0 end

    def Function_16_6336(): pass

    label("Function_16_6336")

    OP_8E(0xFE, 0xFFFBFC62, 0x0, 0x15ED2, 0x7D0, 0x0)
    Return()

    # Function_16_6336 end

    def Function_17_634B(): pass

    label("Function_17_634B")

    OP_8E(0xFE, 0xFFFBFEF6, 0x0, 0x15B9E, 0x7D0, 0x0)
    Return()

    # Function_17_634B end

    def Function_18_6360(): pass

    label("Function_18_6360")

    OP_8E(0xFE, 0xFFFBF62C, 0x0, 0x15D56, 0x7D0, 0x0)
    Return()

    # Function_18_6360 end

    def Function_19_6375(): pass

    label("Function_19_6375")

    OP_8E(0xFE, 0xFFFBF79E, 0x0, 0x1570C, 0x7D0, 0x0)
    Return()

    # Function_19_6375 end

    def Function_20_638A(): pass

    label("Function_20_638A")

    OP_8E(0xFE, 0xFFFBFBB8, 0x0, 0x153CE, 0x7D0, 0x0)
    Return()

    # Function_20_638A end

    def Function_21_639F(): pass

    label("Function_21_639F")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6418"),
        (1, "loc_641E"),
        (SWITCH_DEFAULT, "loc_6424"),
    )


    label("loc_6418")

    OP_A2(0x1200)
    Jump("loc_6424")

    label("loc_641E")

    OP_A2(0x1201)
    Jump("loc_6424")

    label("loc_6424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6432")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_6436")

    label("loc_6432")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_6436")

    Return()

    # Function_21_639F end

    SaveToFile()

Try(main)
