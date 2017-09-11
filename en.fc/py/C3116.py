from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Major Cid',                            # 9
        "Soldier's Voice",                      # 10
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
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
        X                   = -1100,
        Z                   = 0,
        Y                   = -3000,
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


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_11D",          # 01, 1
        "Function_2_12A",          # 02, 2
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_106"),
        (SWITCH_DEFAULT, "loc_11C"),
    )


    label("loc_106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119")
    OP_A2(0x570)
    Event(0, 2)

    label("loc_119")

    Jump("loc_11C")

    label("loc_11C")

    Return()

    # Function_0_FA end

    def Function_1_11D(): pass

    label("Function_1_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_129")
    OP_22(0xAC, 0x1, 0x3C)

    label("loc_129")

    Return()

    # Function_1_11D end

    def Function_2_12A(): pass

    label("Function_2_12A")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -820, 0, 4400, 180)
    SetChrPos(0x102, -1790, 0, -440, 0)
    SetChrPos(0x101, -1250, 0, 1250, 0)
    SetChrPos(0x106, -180, 0, 650, 0)
    SetChrPos(0x107, -170, 0, -450, 0)
    SetChrPos(0x10B, -2090, 0, 580, 0)
    OP_6D(-590, 0, 2080, 0)
    OP_67(0, 7290, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "#701FThat was spectacularly close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#501FI knew it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#700FLock it, just to be on\x01",
            "the safe side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#012FGot it.\x02",
    )

    CloseMessageWindow()

    def lambda_266():

        label("loc_266")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_266")

    QueueWorkItem2(0x101, 1, lambda_266)

    def lambda_277():

        label("loc_277")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_277")

    QueueWorkItem2(0x106, 1, lambda_277)

    def lambda_288():

        label("loc_288")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_288")

    QueueWorkItem2(0x107, 1, lambda_288)

    def lambda_299():

        label("loc_299")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_299")

    QueueWorkItem2(0x10B, 1, lambda_299)
    OP_8E(0x102, 0xFFFFFBD2, 0x0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0x102, 180, 400)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x102, 0x8, 400)
    Sleep(100)

    def lambda_2E0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E0)

    def lambda_2EE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2EE)

    def lambda_2FC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2FC)

    def lambda_30A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_30A)

    def lambda_318():
        OP_6D(-740, 0, 3380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_318)

    def lambda_330():

        label("loc_330")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_330")

    QueueWorkItem2(0x101, 2, lambda_330)

    def lambda_341():
        OP_8E(0xFE, 0xFFFFFC22, 0x0, 0xADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_341)
    Sleep(200)

    def lambda_361():

        label("loc_361")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_361")

    QueueWorkItem2(0x106, 2, lambda_361)

    def lambda_372():
        OP_8E(0xFE, 0x1E0, 0x0, 0xD02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_372)
    Sleep(100)

    def lambda_392():

        label("loc_392")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_392")

    QueueWorkItem2(0x10B, 2, lambda_392)

    def lambda_3A3():
        OP_8E(0xFE, 0xFFFFF844, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A3)
    Sleep(100)

    def lambda_3C3():

        label("loc_3C3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3C3")

    QueueWorkItem2(0x107, 2, lambda_3C3)

    def lambda_3D4():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x820, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3D4)
    Sleep(200)

    def lambda_3F4():
        OP_8E(0xFE, 0xFFFFF858, 0x0, 0x866, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F4)
    Sleep(2500)

    ChrTalk(    #4
        0x10B,
        (
            "#102FHmph... What are you planning?\x01",
            "You're the C.O. of Leiston Fortress.\x02\x03",

            "Didn't Colonel Richard order\x01",
            "you to keep me locked up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#703F...I'm very sorry about that.\x02\x03",

            "#700FHe's already seized control of the\x01",
            "Royal Armed Forces by using his\x01",
            "position in the Intelligence Division.\x02\x03",

            "And the main generals were given the\x01",
            "choice of obeying him, or being imprisoned.\x02\x03",

            "General Morgan refused to obey him, and as\x01",
            "such is currently imprisoned at the Haken\x01",
            "Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#4P#580FThat stubborn old man?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#2P#012FThis is getting serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#055FWhat the hell? I figured things were bad,\x01",
            "but not THAT bad...\x02\x03",

            "When did the military's structure get\x01",
            "that fragile?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#703FUnfortunately, observance of military\x01",
            "regs has been breaking down,\x01",
            "ever since the end of the war.\x02\x03",

            "Particularly since the top brass\x01",
            "haven't stopped embezzling and\x01",
            "accepting bribes.\x02\x03",

            "Colonel Richard just took\x01",
            "advantage of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10B,
        (
            "#102FI see... So he was able to make use\x01",
            "of the military's existing corruption\x01",
            "and weakness to seize control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#700FPrecisely.\x02\x03",

            "With General Morgan in custody, that\x01",
            "leaves Colonel Richard as the man in\x01",
            "charge of the entire Royal Armed Forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#4P#007FTh-That's horrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x106,
        (
            "#050FWhat about Queen Alicia?\x02\x03",

            "Doesn't supreme command of the army rest\x01",
            "with the queen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#703FMysteriously enough...Queen Alicia\x01",
            "has kept silent on the matter.\x02\x03",

            "The Royal Guardsmen are actually\x01",
            "being sought for questioning, on\x01",
            "suspicion of treason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#4P#580FTr-treason?!\x02\x03",

            "Lieutenant Schwarz, too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#702FThe attack on the central factory has been\x01",
            "pinned on the Royal Guardsmen.\x02\x03",

            "There's even photographic evidence,\x01",
            "as I understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#2P#013FDorothy's pictures...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#065FThat... That just doesn't\x01",
            "sound right!\x02\x03",

            "#561FThe factory was all messed up,\x01",
            "and Grandpa was kidnapped...\x02\x03",

            "Agate was almost killed...\x02\x03",

            "#062FYou can't just go around blaming\x01",
            "people for something like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#703F...I really don't know what to tell you.\x02\x03",

            "You never disobey a direct order from a \x01",
            "superior officer...but since I never voiced\x01",
            "my objections, the fault still lies with me.\x02\x03",

            "#701FI know this will not make up for all I have\x01",
            "done, but I was hoping it would go some way to\x01",
            "atoning for my actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        (
            "#051FYou've had a tough time\x01",
            "of it, ain'tcha?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10B,
        (
            "#104FHmph... Well, if all that you've\x01",
            "said is true, then I suppose I\x01",
            "can forgive and forget.\x02\x03",

            "I had been prepared to brain\x01",
            "you with a wrench and soften\x01",
            "up that hard head. Pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#702FI-I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#065FGrandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10B,
        "#100FIt was a joke, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#4P#002FOkay, I've got everything...but what are you\x01",
            "planning to do now?\x02\x03",

            "Are you planning on hiding us until the heat\x01",
            "dies down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#700FNo, I have a much better solution.\x02\x03",

            "There's a way for you to escape the fortress\x01",
            "through this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#4P#004FThrough this room? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#2P#010FAh, I get it! There's a secret passageway\x01",
            "or something, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#701FHa ha...\x01",
            "Very astute, boy.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_F71():

        label("loc_F71")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F71")

    QueueWorkItem2(0x101, 1, lambda_F71)

    def lambda_F82():

        label("loc_F82")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F82")

    QueueWorkItem2(0x106, 1, lambda_F82)

    def lambda_F93():

        label("loc_F93")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F93")

    QueueWorkItem2(0x107, 1, lambda_F93)

    def lambda_FA4():

        label("loc_FA4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FA4")

    QueueWorkItem2(0x10B, 1, lambda_FA4)

    def lambda_FB5():
        OP_6D(3440, 0, 9720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FB5)

    def lambda_FCD():
        OP_8E(0xFE, 0xD02, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FCD)

    def lambda_FE8():

        label("loc_FE8")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_FE8")

    QueueWorkItem2(0x8, 1, lambda_FE8)
    Sleep(800)

    def lambda_FFE():

        label("loc_FFE")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_FFE")

    QueueWorkItem2(0x106, 1, lambda_FFE)

    def lambda_100F():
        OP_8E(0xFE, 0x9D8, 0x0, 0x1DBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_100F)
    Sleep(50)

    def lambda_102F():

        label("loc_102F")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_102F")

    QueueWorkItem2(0x107, 1, lambda_102F)

    def lambda_1040():
        OP_8E(0xFE, 0x794, 0x0, 0x1A86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1040)
    Sleep(100)

    def lambda_1060():

        label("loc_1060")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_1060")

    QueueWorkItem2(0x101, 1, lambda_1060)

    def lambda_1071():
        OP_8E(0xFE, 0x726, 0x0, 0x208A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1071)
    Sleep(350)

    def lambda_1091():

        label("loc_1091")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_1091")

    QueueWorkItem2(0x10B, 1, lambda_1091)

    def lambda_10A2():
        OP_8E(0xFE, 0xAF0, 0x0, 0x1A86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_10A2)
    Sleep(50)

    def lambda_10C2():

        label("loc_10C2")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_10C2")

    QueueWorkItem2(0x102, 1, lambda_10C2)

    def lambda_10D3():
        OP_8E(0xFE, 0x3E8, 0x0, 0x1B6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D3)
    WaitChrThread(0x8, 0x2)
    Sleep(100)
    OP_70(0x0, 0xF0)
    Sleep(1200)

    ChrTalk(    #30
        0x101,
        "#004FWhoa...\x02",
    )

    CloseMessageWindow()
    OP_73(0x0)
    OP_44(0x8, 0xFF)
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0xA46, 0x0, 0x27EC, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #31
        0x106,
        (
            "#051FMakes sense, for a military\x01",
            "control room. Not bad. Not\x01",
            "bad at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#703FThis emergency escape hatch leads\x01",
            "to an underground aqueduct.\x02\x03",

            "There's a boat set up there,\x01",
            "so you should be able to use\x01",
            "it and escape.\x02\x03",

            "#701FLegally, even my telling civilians\x01",
            "about it would net me ten years\x01",
            "in prison.\x02\x03",

            "But even if military regulations\x01",
            "won't forgive me, I think Aidios\x01",
            "probably will.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12D4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D4)

    def lambda_12E2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12E2)

    def lambda_12F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_12F0)

    def lambda_12FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12FE)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #33
        0x107,
        "#063FMajor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x106,
        "#051FAll right, we'll use it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(400)

    ChrTalk(    #35
        0x106,
        (
            "#050F#2PI'll go down first. Then\x01",
            "the old man and Tita.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #36
        0x106,
        (
            "#054F#2PEstelle and Joshua? I want\x01",
            "you to watch our backs.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13D8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13D8)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #37
        0x101,
        "#006FGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#010FRoger that.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x10B, 0x4)
    SetChrFlags(0x107, 0x4)
    OP_8E(0x106, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x106, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    ChrTalk(    #39
        0x10B,
        "#100FFarewell, Major.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10B, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x10B, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    ChrTalk(    #40
        0x107,
        (
            "#560FUmm...well...\x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x107, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x107, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    def lambda_14EE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14EE)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #41
        0x101,
        (
            "#006FWell, then...\x01",
            "That just leaves us.\x02\x03",

            "Thank you for everything, Major.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xAA0, 0x0, 0x1DE2, 0xBB8, 0x0)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #42
        0x102,
        "#010FWe're in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#703FYou don't need to thank me.\x02\x03",

            "To be honest, I was expecting\x01",
            "this since the moment I first\x01",
            "saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#505FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#010FYou mean when we met\x01",
            "at the front gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#701FYes... As soon as I heard\x01",
            "your last name.\x02\x03",

            "After all, you are the children\x01",
            "of Colonel Cassius, are you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#505FColonel Cassius...\x02\x03",

            "#004FYou mean my dad really\x01",
            "had a rank that high?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#703FRichard may be a colonel now, but he served\x01",
            "under your father back in those days.\x02\x03",

            "Your dad was a real hero. It was thanks to his\x01",
            "efforts that we were able to defeat Erebonia in\x01",
            "the war ten years ago.\x02\x03",

            "#701FBeing as you're his children, I'm not \x01",
            "surprised that you found out the truth \x01",
            "and came to help the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#004FI... Really...?\x02\x03",

            "But he never said anything about\x01",
            "being any kind of military hero...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_18FE():
        OP_6D(1910, 0, 8160, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18FE)

    def lambda_1916():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1916)

    def lambda_1924():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1924)
    TurnDirection(0x101, 0x9, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #50
        0x9,
        "Are you okay, Major?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "The intruders have been spotted\x01",
            "in the dungeon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "The last likely place for\x01",
            "them to be is in central\x01",
            "HQ, sir! Your orders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#580FCrap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#704F#3SAcknowledged! I'll be right\x01",
            "there, so put the facility\x01",
            "on high alert!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A40():
        OP_6D(3440, 0, 9720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A40)

    def lambda_1A58():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A58)

    def lambda_1A66():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A66)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #55
        0x8,
        "#702FCome on, you need to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#002FO-Okay...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#012FExcuse us, then...\x02",
    )

    CloseMessageWindow()

    def lambda_1AD5():
        OP_8E(0xFE, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AD5)
    Sleep(600)

    def lambda_1AF5():

        label("loc_1AF5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1AF5")

    QueueWorkItem2(0x8, 1, lambda_1AF5)
    OP_8E(0x102, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x102, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x44, 0x1, 0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3114   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12A end

    SaveToFile()

Try(main)
