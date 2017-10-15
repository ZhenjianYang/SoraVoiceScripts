from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3110.x',
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
        'Cassius',                              # 9
        'General Morgan',                       # 10
        'Lt. Colonel Cid',                      # 11
        'Royal Army Officer',                   # 12
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT27/CH03590 ._CH',             # 02
        'ED6_DT07/CH01600 ._CH',             # 03
        'ED6_DT27/CH03673 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT27/CH03590P._CP',             # 02
        'ED6_DT07/CH01600P._CP',             # 03
        'ED6_DT27/CH03673P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_18E",          # 01, 1
        "Function_2_18F",          # 02, 2
        "Function_3_446",          # 03, 3
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_171")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_18D")

    label("loc_171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_18D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_18D")

    Return()

    # Function_0_152 end

    def Function_1_18E(): pass

    label("Function_1_18E")

    Return()

    # Function_1_18E end

    def Function_2_18F(): pass

    label("Function_2_18F")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 4)
    SetChrPos(0x8, 20700, 250, 262750, 180)
    SetChrPos(0x9, 21260, 0, 260470, 0)
    SetChrPos(0xA, 19790, 0, 260399, 45)
    OP_6D(21850, 0, 262980, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(247, 0)
    FadeToBright(2000, 0)
    OP_22(0x85, 0x0, 0x64)

    def lambda_242():

        label("loc_242")

        OP_7C(0x32, 0x0, 0x3E8, 0xBB8)
        OP_48()
        Jump("loc_242")

    QueueWorkItem2(0x101, 3, lambda_242)
    OP_0D()

    ChrTalk(    #0
        0xA,
        "#702F#5PGeneral Cassius, you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#1128F#6PHrmmm. It seems I was right.\x02\x03",

            "Ordering a work stoppage at\x01",
            "the port was the right idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#163F#2PIncredible. I didn't actually think\x01",
            "there would be an earthquake as\x01",
            "you predicted...\x02\x03",

            "#160FCassius, just what kind of magic\x01",
            "did you use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1120F#6PWhat magic? It's just logic, Morgan.\x01",
            "The logic of our foes' desires.\x02\x03",

            "#1125FAfter three 'rehearsals'...it was\x01",
            "simply a question of what made the\x01",
            "most tempting target.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3119   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_18F end

    def Function_3_446(): pass

    label("Function_3_446")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(21350, 0, 262510, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    SetChrPos(0x8, 20620, 300, 262810, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 20620, 0, 260040, 0)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0xB,
        (
            "...And that's the situation on\x01",
            "all fronts, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "I think we can say that we're gaining\x01",
            "ground everywhere, including with the\x01",
            "bracers on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "#1120F#6PMmm. Good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "If I may, sir? I personally don't really\x01",
            "think there's a chance we'll lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        (
            "This 'society' is just a bunch of\x01",
            "puffed-up criminals and jaegers.\x01",
            "They'll never beat the Royal Army!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1125F#6PDon't underestimate them.\x01",
            "They're 'criminals' with an airship the\x01",
            "size of a small town, to start with.\x02\x03",

            "#1122FHave the air units continue\x01",
            "their patrol over all regions.\x02\x03",

            "Also, dispatch Emergency Order\x01",
            "One to all divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        "Understood, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    def lambda_767():
        OP_6D(21810, 0, 258019, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_767)

    def lambda_77F():
        OP_67(0, 5000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77F)

    def lambda_797():
        OP_8E(0xFE, 0x515E, 0x32, 0x3DA72, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_797)
    WaitChrThread(0xB, 0x1)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_7CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7CC)
    OP_8E(0xB, 0x5140, 0x0, 0x3D284, 0x9C4, 0x0)
    OP_22(0xE6, 0x0, 0x64)
    ClearChrFlags(0xB, 0x80)
    Sleep(500)
    Fade(500)
    OP_6D(21350, 0, 262510, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x8,
        (
            "#1128F#6PEmergency Order One. The order\x01",
            "we invoke in times of extreme crisis.\x02\x03",

            "#1125FI hope I'm just being paranoid, but...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)

    def lambda_8D9():
        OP_6D(20350, 0, 262510, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D9)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 19790, 0, 263160, 270)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    OP_0D()
    Sleep(1000)

    def lambda_926():
        OP_6D(20640, 0, 265150, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_926)
    OP_8E(0x8, 0x4DE4, 0x0, 0x40AEC, 0x7D0, 0x0)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 19800, 1180, 265350, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #12
        0x8,
        (
            "#1125F#6PYes, this is Cassius Bright.\x02\x03",

            "#1120FI apologize for the surprise,\x01",
            "but please bring him up.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_446 end

    SaveToFile()

Try(main)
